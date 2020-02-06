from sqlalchemy import create_engine, Column, Integer, String, Boolean

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:////home/codyjackson/PycharmProjects/Fantasy_RPG/Adv_Dark_Deep/Tables/Classes.sqlite")
Base.metadata.bind = engine
# engine.connect()
db_session = sessionmaker(bind=engine)
session = db_session()


class AcceptableCharClass(Base):
    """Create the SQLAlchemy structure for the existing DB"""
    __tablename__ = "rvc"  # Race vs. Class
    rvc_class = Column(String, primary_key=True)
    gray_dwarf = Column(Boolean, default=False)
    hill_dwarf = Column(Boolean, default=False)
    mtn_dwarf = Column(Boolean, default=False)
    drow_male = Column(Boolean, default=False)
    drow_female = Column(Boolean, default=False)
    gray_elf = Column(Boolean, default=False)
    half_elf = Column(Boolean, default=False)
    high_elf = Column(Boolean, default=False)
    wild_elf = Column(Boolean, default=False)
    wood_elf = Column(Boolean, default=False)
    deep_gnome = Column(Boolean, default=False)
    forest_gnome = Column(Boolean, default=False)
    hill_gnome = Column(Boolean, default=False)
    halfling = Column(Boolean, default=False)
    half_orc = Column(Boolean, default=False)
    human = Column(Boolean, default=True)

