import os
import dotenv
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

# Loads the env variables to use for the connection string
dotenv.load_dotenv("secrets.env")
user = os.getenv("DBUSER")
host = os.getenv("DBHOST")
name = os.getenv("DBNAME")
port = os.getenv("DBPORT")
password = os.getenv("DBPASS")

# Creates an engine object to connect to the database
engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{name}", echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# An object for the games table
class Games(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    developer = Column(String)
    started = Column(Boolean)
    finished = Column(Boolean)
