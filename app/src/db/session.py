from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from utils import settings

# Create the database engine
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
)

# Create a scoped session for thread-safe database operations
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

# Create a Session class for individual database sessions
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for database models
DBBase = declarative_base()


async def init_db():
    try:
        # Create all database tables based on the defined models
        DBBase.metadata.create_all(bind=engine)
    except Exception as e:
        # Handle any exceptions that occur during database initialization
        raise e
