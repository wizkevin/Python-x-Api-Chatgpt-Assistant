from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database/assistant_data.db', pool_pre_ping=True)

Base = declarative_base()
get_session = sessionmaker(bind=engine)