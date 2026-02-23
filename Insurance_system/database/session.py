from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# If root has NO password
DATABASE_URL = "mysql+pymysql://root:kelvin.2908@localhost/insurance_db"

# If you have password:
# DATABASE_URL = "mysql+pymysql://root:YOUR_PASSWORD@localhost/insurance_db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)
