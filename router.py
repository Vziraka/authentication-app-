# Router — where endpoints live
# Each function here handles one URL (like /signup, /login, etc.)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User, VerificationCode
from schemas import SignupRequest, SignupResponse
from utils import hash_password, generate_code, send_email

router = APIRouter()


# ---- SIGNUP ----

@router.post("/signup", response_model=SignupResponse)
def signup(request: SignupRequest, db: Session = Depends(get_db)):

    # 1. Check if username already exists
    existing_user = db.query(User).filter(User.username == request.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username is not available")

    # 2. Check if email already exists
    existing_email = db.query(User).filter(User.email == request.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="An account with this email already exists")

    # 3. Hash the password
    hashed = hash_password(request.password)

    # 4. Create the user and save to database
    new_user = User(
        username=request.username,
        email=request.email,
        password_hash=hashed,
        role=request.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # 5. Generate verification code and save to database
    code = generate_code()
    verification = VerificationCode(
        user_id=new_user.id,
        code=code,
        purpose="signup"
    )
    db.add(verification)
    db.commit()

    # 6. Send the code to the user's email
    send_email(new_user.email, code)

    # 7. Return response
    return SignupResponse(
        user_id=new_user.id,
        message="Account created. Check your email for a verification code."
    )
