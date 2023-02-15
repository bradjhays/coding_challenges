"""."""
import sys
import argparse
import logging
import pprint

import db

pp = pprint.PrettyPrinter(indent=4)
logger = logging.getLogger("search")


def main(col_name, col_value):
    """."""
    qry = (
        db.get_session()
        .query(db.Entity)
        .filter(getattr(db.Entity, col_name).like(col_value))
    )
    for entity in qry.all():
        # print out for now
        pp.pprint(entity.__dict__)


def get_arg(cmd_args, cols):
    """."""
    for column in cols:
        try:
            if vars(cmd_args)[column]:
                return column, vars(cmd_args)[column]
        except KeyError:
            continue
    return None, None


def build_args(group):
    """."""
    cols = []
    for column in db.Entity.__table__.columns:
        col_name = str(column.name)
        group.add_argument(
            f"--{col_name}",
            dest=f"{col_name}",
            help=f"Entity {col_name} ({column.type})",
        )
        cols.append(col_name)
    return cols


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, force=True)
    parser = argparse.ArgumentParser(description="Query database")
    g = parser.add_mutually_exclusive_group()
    columns = build_args(group=g)
    args = parser.parse_args()
    logger.info("ARGS: %s", args)

    column_name, value = get_arg(args, columns)
    if not column_name:
        print("No options selected...")
        parser.print_help(sys.stderr)
        sys.exit(1)
    print(f"search for {column_name}: {value}")
    main(col_name=column_name, col_value=value)
