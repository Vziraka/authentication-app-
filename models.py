# Python classes that mirror your SQL tables. 
# SQLAlchemy uses these classes so you can talk to the database in Python instead of writing raw SQL


from sqlalchemy import Column, String, Boolean, DateTime, Integer, ForeignKey # data types used to define table columns in Python so SQLAlchemy can map them to PostgreSQL

from sqlalchemy.dialects.postgresql import UUID  # imports the UUID data type from postgresql 
from database import Base # imports base class from database.py
import uuid # used create UUID instructions for the database 
from datetime import datetime #imports the datetime module to use the current date and time 

#types and tools that let you describe your table's structure in Python, 
#so SQLAlchemy knows how to map your Python classes to the tables that already exist in PostgreSQL

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) # the stuff after default are bacailly instructions to generate the uuid 4 everytime a new user is created
    username = Column(String(50), unique=True, nullable=False) # nullable means the column cant be empty 
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False)
    email_verified = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    # utcnow means the current date and time 

    # why do we use column()?
    # to mirror the database table structure to the python code


class VerificationCode(Base):
    __tablename__ = "verification_codes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    code = Column(String(6), nullable=False)
    purpose = Column(String(10), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    attempts = Column(Integer, nullable=False, default=0)
    is_active = Column(Boolean, nullable=False, default=True)
    used = Column(Boolean, nullable=False, default=False)
