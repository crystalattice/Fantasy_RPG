from typing import List

from sqlalchemy import create_engine, Column, String, Boolean
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker, Session

Base: DeclarativeMeta = declarative_base()
# engine: Engine = create_engine(
#     "sqlite:////home/codyjackson/PycharmProjects/Fantasy_RPG/Adv_Dark_Deep/Tables/Classes.sqlite")
engine: Engine = create_engine(
    "sqlite:///../Tables/Classes.sqlite")
Base.metadata.bind = engine
db_session: sessionmaker = sessionmaker(bind=engine)
session: Session = db_session()


class AcceptableMultiClass(Base):
    """Create the SQLAlchemy structure for the existing DB

    The tablename needs to match the table name previously created.
    The column names need to match the names assigned in the table.
    """
    __tablename__: str = "Multi_Class_by_Race"  # Race vs. Class
    Multi_class: str = Column(String, primary_key=True)
    Dwarf: bool = Column(Boolean, default=False)
    Elf_Dark: bool = Column(Boolean, default=False)
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


def get_classes(race: str) -> list:
    """Get character classes available to a particular race

    Note: Half-elves are subject to the same restrictions as their parent elf stock.
    """
    global classes
    char_classes: List[tuple] = []
    if race == "Dwarf":
        classes = session.query(AcceptableMultiClass.Multi_class).filter(AcceptableMultiClass.Dwarf)
    elif race == "Dark Elf":
        classes = session.query(AcceptableMultiClass.Multi_class).filter(AcceptableMultiClass.Elf_Dark)
    elif race == "Grey Elf":
        classes = session.query(AcceptableMultiClass.Multi_class).filter(AcceptableMultiClass.Elf_Gray)
    elif race == "Half-Elf":
        classes = session.query(AcceptableMultiClass.Multi_class).filter(AcceptableMultiClass.Elf_Half)
    elif race == "High Elf":
        classes = session.query(AcceptableMultiClass.Multi_class).filter(AcceptableMultiClass.Elf_High)
    elif race == "Wild Elf":
        classes = session.query(AcceptableMultiClass.Multi_class).filter(AcceptableMultiClass.Elf_Wild)
    elif race == "Wood Elf":
        classes = session.query(AcceptableMultiClass.Multi_class).filter(AcceptableMultiClass.Elf_Wood)
    elif race == "Deep Gnome":
        classes = session.query(AcceptableMultiClass.Multi_class).filter(AcceptableMultiClass.Gnome_Deep)
    elif race == "Forest Gnome":
        classes = session.query(AcceptableMultiClass.Multi_class).filter(AcceptableMultiClass.Gnome_Forest)
    elif race == "Hill Gnome":
        classes = session.query(AcceptableMultiClass.Multi_class).filter(AcceptableMultiClass.Gnome_Hill)
    elif race == "Halfling":
        classes = session.query(AcceptableMultiClass.Multi_class).filter(AcceptableMultiClass.Halfling)
    elif race == "Half-Orc":
        classes = session.query(AcceptableMultiClass.Multi_class).filter(AcceptableMultiClass.Orc_Half)

    for avail_classes in classes:
        char_classes.append(avail_classes)

    return char_classes


if __name__ == "__main__":
    vals = get_classes("Wood Elf")
    print(vals)
    for val in vals:
        print(val[0])
