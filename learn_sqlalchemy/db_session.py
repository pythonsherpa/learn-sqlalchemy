"""
Set up the connection to the database & create the tables.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from learn_sqlalchemy.models import Base

engine = create_engine(
    "sqlite:///database.db",
    connect_args={"check_same_thread": False},
    echo=False,
)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine, checkfirst=True)
