from sqlalchemy import Column, String, Boolean, DateTime, Integer, ForeignKey # data types used to define table columns in Python so SQLAlchemy can map them to PostgreSQL

from sqlalchemy.dialects.postgresql import UUID 
from database import Base # imports base class from database.py
import uuid 
from datetime import datetime #imports the datetime module to use the current date and time 


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) # the stuff after default are bacailly instructions to the database to generate the uuid 4 everytime a new user is created
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
