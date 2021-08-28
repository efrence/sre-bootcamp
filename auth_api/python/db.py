from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql+pymysql://secret:noPow3r@bootcamp-tht.sre.wize.mx/bootcamp_tht?charset=utf8mb4")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

