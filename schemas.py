# Pydantic schemas — validate what comes IN to each endpoint and filter what goes OUT
# These don't touch the database. They sit between the user and your endpoint code.

from pydantic import BaseModel, EmailStr  # BaseModel is the base class for all schemas and we attach it to all our schemas, EmailStr validates email format
from uuid import UUID  # so we can use UUID type in our schemas


# we use schema.py is used to validate the input data that the user sends to the endpoint

# the output schemas are used to define the response format or how the response should look like for each endpoint
# and which data should be sent back to the frontend

# ---- INPUT SCHEMAS (what the user sends to us) ----

class SignupRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str  # "supplier" or "restaurant"


class VerifyCodeRequest(BaseModel):
    user_id: UUID # we need user_id to know which user to verify the code for
    code: str


class ResendCodeRequest(BaseModel):
    user_id: UUID # we need user_id to know which user to resend the code to


class LoginRequest(BaseModel):
    username: str
    password: str


# ---- OUTPUT SCHEMAS (what we send back to the user) ----

class MessageResponse(BaseModel):
    message: str


class SignupResponse(BaseModel):
    user_id: UUID # we user_Id as an output because we need it for the frontend to display the user's information
    message: str # we use it to display a message to the user like "User created successfully"


class LoginResponse(BaseModel):
    user_id: UUID
    message: str


class VerifyLoginResponse(BaseModel):
    user_id: UUID # know which user is logged in
    role: str # know which role the user has
    token: str # token for there webrowser so they dont have to constantly login every time they visit the website
    message: str # message to display to the user like "Login successful"


class DashboardResponse(BaseModel):
    user_id: UUID 
    username: str 
    role: str 
# when you interact with the dasboard t would always under the user. And, obviously, 
# it would be under the username and their role.