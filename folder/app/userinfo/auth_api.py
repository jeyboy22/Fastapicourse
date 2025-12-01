from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, Session, create_engine, select


app = FastAPI()

sqlite_file_name = "users.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

class User(SQLModel, table=True):
    id: int | None = Field(default=None,primary_key=True)
    username: str = Field(index=True, unique=True)
    password: str

SQLModel.metadata.create_all(engine)

@app.post("/register")
def register(user: User):
  with Session(engine) as session:
        statement = select(User).where(User.username == user.username)
        existing_user = session.exec(statement).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")
        
        session.add(user)
        session.commit()
        session.refresh(user)
        return {"message": "User registered successfully!"}

@app.post("/login")
def login(user: User):
    with Session(engine) as session:
        statement = select(User).where(User.username == user.username)
        db_user = session.exec(statement).first()
        if not db_user or db_user.password != user.password:
            raise HTTPException(status_code=401, detail="Invalid username or password")
        return {"message": "Login successful"}

@app.get("/user/{username}")
def get_user(username: str):
    with Session(engine) as session:
        statement = select(User).where(User.username == username)
        db_user = session.exec(statement).first()
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        return {"username": db_user.username, "status":"Active"}