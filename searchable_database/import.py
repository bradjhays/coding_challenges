"""Import json to DB."""
import json
import pprint
import logging

from sqlalchemy.sql.expression import select

import db


pp = pprint.PrettyPrinter(indent=4)
logger = logging.getLogger(__name__)
ENTITY_ALREADY_IMPORTED = []
CONTACT_ALREADY_IMPORTED = []


def convert_case(str_camelcase):
    """This function takes in a string in camelCase and converts it to snake_case."""
    str_snake_case = ""
    for ele in list(str_camelcase):
        if ele.islower():
            str_snake_case = str_snake_case + ele
        else:
            str_snake_case = str_snake_case + "_" + ele.lower()
    return str_snake_case


def convert_dict_case(camel_dict):
    """return dict with snake case from camelCase."""
    return {convert_case(key): value for key, value in camel_dict.items()}


def import_entity(entity, session):
    """."""
    global ENTITY_ALREADY_IMPORTED, CONTACT_ALREADY_IMPORTED
    contacts = entity.pop("contacts")
    if entity["nameCombined"] in ENTITY_ALREADY_IMPORTED:
        logger.warning("%s already imported" % entity["nameCombined"])
        entity_id = ENTITY_ALREADY_IMPORTED[entity["nameCombined"]]
    else:
        entity = convert_dict_case(entity)
        pp.pprint(entity)

        new_entity = db.Entity(**entity)
        session.add(new_entity)
        session.commit()  # Commit, because we need the id
        entity_id = new_entity.id
        ENTITY_ALREADY_IMPORTED[entity["name_combined"]] = entity_id
    assert entity_id
    added = False
    for contact in contacts:
        if contact["mmdbContactId"] in CONTACT_ALREADY_IMPORTED:
            logger.warning("contact %s already in DB" % contact["mmdbContactId"])
            continue

        contact = convert_dict_case(camel_dict=contact)
        contact["entity_id"] = entity_id
        new_contact = db.Contact(**contact)
        session.add(new_contact)
        CONTACT_ALREADY_IMPORTED.append(contact["mmdb_contact_id"])
        added = True
    if added:
        session.commit()

    # pp.pprint(contacts)


def main(filename):
    """."""
    global ENTITY_ALREADY_IMPORTED, CONTACT_ALREADY_IMPORTED
    session = db.get_session()
    # assume unique combined name
    ENTITY_ALREADY_IMPORTED = {
        x[0]: x[1]
        for x in session.query()
        .with_entities(db.Entity.name_combined, db.Entity.id)
        .all()
    }
    CONTACT_ALREADY_IMPORTED = [
        x[0] for x in session.query().with_entities(db.Contact.mmdb_contact_id).all()
    ]
    # Import JSON file
    count = 0
    with open(filename, encoding="utf-8") as json_file:
        try:
            for entity in json.load(json_file):
                import_entity(entity, session)
                # break
                count += 1
        finally:
            print(f"imported {count}")


if __name__ == "__main__":
    main(filename="./data.json")
