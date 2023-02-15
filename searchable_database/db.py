"""SQLAlchemy Data Models."""
import os
import logging

from sqlalchemy import Column, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, String, Float, Boolean, BigInteger
from sqlalchemy.orm import sessionmaker

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = int(os.getenv("DB_PORT", "3600"))
GLOBAL_SESSION = None

logger = logging.getLogger(__name__)
logging.getLogger("sqlalchemy.engine").setLevel(logging.ERROR)

assert DB_USER
assert DB_PASS
assert DB_HOST
assert DB_NAME

server_str = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
logger.debug("connect to %s" % server_str)
engine = create_engine(server_str)


def get_session():
    """."""
    global GLOBAL_SESSION
    if not GLOBAL_SESSION:
        session = sessionmaker(bind=engine)
        GLOBAL_SESSION = session()
    return GLOBAL_SESSION


Base = declarative_base()


class Contact(Base):
    """Contact."""

    __tablename__ = "contact"

    mmdb_contact_id = Column(BigInteger, primary_key=True)  # 100000048336,
    entity_id = Column(Integer, ForeignKey("entity.id"), index=True)
    first_name = Column(String(255))  # ": "Albert",
    last_name = Column(String(255))  # ": "Burns",
    gender = Column(String(255))  # ": "Male",
    family_id = Column(BigInteger)  # ": 27296,
    age_range_code = Column(String(255))  # ": "M",
    age_range = Column(String(255))  # ": "75+"
    email_hash = Column(String(255))  #


class Entity(Base):
    """Entity."""

    __tablename__ = "entity"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    age = Column(String(255))  # "75",
    age_range = Column(String(255))  # "65+",
    age_range_code = Column(String(255))  # "M",
    area_code = Column(String(255))  # "352",
    carrier_route = Column(String(255))  # "R067",
    estimated_home_income = Column(String(255))  # "$100,000 - $124,999",
    estimated_home_value = Column(String(255))  # "$250,000 - $299,999",
    gender = Column(String(255))  # "Female",
    first_name = Column(String(255))  # "Danielle",
    home_value_range = Column(String(255))  # "$250,000 - $299,999",
    housing_type = Column(String(255))  # "Single Family Dwelling",
    income_range = Column(String(255))  # "$100,000 - $124,999",
    income_range_code = Column(String(255))  # "J",
    latitude = Column(Float)  #  29.05497,
    last_name = Column(String(255))  # "Burns",
    longitude = Column(Float)  #  -82.25809,
    own_or_rent = Column(String(255))  # "Confirmed Owner",
    own_or_rent_code = Column(String(255))  # "3",
    is_homeowner = Column(Boolean)  # true,
    name_combined = Column(String(255), unique=True)  # "Danielle Burns",
    latitude_fromatted = Column(String(255))  # "29.054970",
    longitude_fromatted = Column(String(255))  # "-82.258090",
    infogroup_id = Column(BigInteger)  # 500000048338,
    address = Column(String(255))  # "8284 SW 114th Ln",
    phone = Column(String(255))  # "Not Approved",
    city = Column(String(255))  # "Ocala",
    county = Column(String(255))  # "MARION",
    state_province = Column(String(255))  # "FL",
    postal_code = Column(String(255))  # "34481"
    is_do_not_call = Column(Boolean)  # true,


Base.metadata.create_all(engine)
