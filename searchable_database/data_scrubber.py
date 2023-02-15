"""Scrub data.json of PII."""
import json
import pprint

from randomuser import RandomUser

pp = pprint.PrettyPrinter(indent=4)


def main(filename):
    """."""
    new_file = []
    with open(filename, encoding="utf-8") as json_file:
        for entity in json.load(json_file):
            user = RandomUser()
            entity["address"]: user.get_street()
            entity["age"] = user.get_age()
            entity["city"] = user.get_city()

            for contact in entity["contacts"]:
                user2 = RandomUser()
                contact["firstName"] = user2.get_first_name()
                contact["gender"] = user2.get_gender()
                contact["lastName"] = user2.get_last_name()
                contact["mmdbContactId"] = user2.get_login_md5()
            entity["firstName"] = user.get_first_name()
            entity["gender"] = user.get_gender()
            entity["lastName"] = user.get_last_name()
            entity["nameCombined"] = user.get_full_name()
            entity["postalCode"] = user.get_postcode()
            entity["stateProvince"] = user.get_state()
            new_file.append(entity)
    pp.pprint(json.dumps(new_file))


if __name__ == "__main__":
    main(filename="data.json")
