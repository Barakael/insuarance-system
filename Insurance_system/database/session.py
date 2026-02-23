from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "mysql+pymysql://root:kelvin.2908@localhost/insurance_db"
DATABASE_URL = "sqlite:///insurance.db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)
