from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker , scoped_session

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
#SQLALCHEMY_DATABASE_URL = "mariadb+mariadbconnector://root:@localhost:3306/fastapi"
SQLALCHEMY_DATABASE_URL ="mysql://cskt3ep99hq9r9w3:pohquqlhu0lhuqbz@iu51mf0q32fkhfpl.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/mtw0sc05n360kuww"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = scoped_session(SessionLocal)
Base = declarative_base()
