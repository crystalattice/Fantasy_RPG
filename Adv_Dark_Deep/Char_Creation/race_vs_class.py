from typing import List

from sqlalchemy import create_engine, Column, String, Boolean
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker, Session

Base: DeclarativeMeta = declarative_base()
engine: Engine = create_engine("sqlite:////home/codyjackson/PycharmProjects/Fantasy_RPG/Adv_Dark_Deep/Tables/Classes.sqlite")
Base.metadata.bind = engine
db_session: sessionmaker = sessionmaker(bind=engine)
session: Session = db_session()

class AcceptableCharClass(Base):
    """Create the SQLAlchemy structure for the existing DB

    The tablename needs to match the table name previously created.
    The column names need to match the names assigned in the table.
    """
    __tablename__: str = "Class_by_Race"  # Race vs. Class
    Char_Class: str = Column(String, primary_key=True)
    Dwarf_Gray: bool = Column(Boolean, default=False)
    Dwarf_Hill: bool = Column(Boolean, default=False)
    Dwarf_Mountain: bool = Column(Boolean, default=False)
    Elf_Dark_Male: bool = Column(Boolean, default=False)
    Elf_Dark_Female: bool = Column(Boolean, default=False)
    Elf_Gray: bool = Column(Boolean, default=False)
    Elf_Half: bool = Column(Boolean, default=False)
    Elf_High: bool = Column(Boolean, default=False)
    Elf_Wild: bool = Column(Boolean, default=False)
    Elf_Wood: bool = Column(Boolean, default=False)
    Gnome_Deep: bool = Column(Boolean, default=False)
    Gnome_Forest: bool = Column(Boolean, default=False)
    Gnome_Hill: bool = Column(Boolean, default=False)
    Halfling: bool = Column(Boolean, default=False)
    Orc_Half: bool = Column(Boolean, default=False)
    Human: bool = Column(Boolean, default=True)


def get_classes(race: str, gender: str) -> list:
    """Get character classes available to a particular race"""
    global classes
    char_classes: List[tuple] = []
    if race == "Hill Dwarf":
        classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Dwarf_Hill)
    elif race == "Gray Dwarf":
        classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Dwarf_Gray)
    elif race == "Mountain Dwarf":
        classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Dwarf_Mountain)
    elif race == "Dark Elf" and gender == "Male":
        classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Elf_Dark_Male)
    elif race == "Dark Elf" and gender == "Female":
        classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Elf_Dark_Female)
    elif race == "Gray Elf":
        classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Elf_Gray)
    elif race == "Half-Elf":
        classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Elf_Half)
    elif race == "High Elf":
        classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Elf_High)
    elif race == "Wild Elf":
        classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Elf_Wild)
    elif race == "Wood Elf":
        classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Elf_Wood)
    elif race == "Deep Gnome":
        classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Gnome_Deep)
    elif race == "Forest Gnome":
        classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Gnome_Forest)
    elif race == "Hill Gnome":
        classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Gnome_Hill)
    elif race == "Halfling":
        classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Halfling)
    elif race == "Half-Orc":
        classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Orc_Half)
    else:  # Assume human as default
        classes = session.query(AcceptableCharClass.Char_Class).filter(AcceptableCharClass.Human)

    for avail_classes in classes:
        char_classes.append(avail_classes)

    return char_classes


if __name__ == "__main__":
    vals = get_classes("Hill Dwarf", "Male")
    print(vals)
    for val in vals:
        print(val[0])
