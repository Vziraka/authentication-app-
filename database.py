from sqlalchemy import create_engine #create engine is from the sqlalchemy library and it craetes the connetions 
from sqlalchemy.orm import sessionmaker, declarative_base # we import sessionmaker for opening and closing connectiosn 
from dotenv import load_dotenv# used to read our .env to connect to our database        # declarative base is the base class for the database table classes 
import os #lets python interact with operating system

# --- 1. Connection URL (read from .env) ---
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL") 
# so it makes varibles to store our database url and in the varible we use the Os library 
# to interaact and get the database url from the .env file 

# --- 2. Engine and session (open/close connections) ---
engine = create_engine(DATABASE_URL) #connets us to the database using our url varible 
SessionLocal = sessionmaker(bind=engine) 

# session local variblecreates a session to the database and binds it to the engine 

def get_db(): 
    db = SessionLocal()
    try: 
        yield db #tells the endpoint to use this database session
    finally: #finally is used to close the session after the endpoint is used or crashes
        db.close() #closes the session after the endpoint is used 


# --- 3. Base class (the "uniform" for database table classes) ---
Base = declarative_base()
