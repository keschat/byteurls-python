# shortener_app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import get_settings

# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost/meetingbookerdb"

##Creating the SQLAlchemy ORM engine..>> above we have imported create_engine method from sqlalchemy
##Since we are using Postgres we dont need anything else

engine = create_engine(get_settings().db_url, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()