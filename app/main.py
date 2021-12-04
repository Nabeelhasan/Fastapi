from fastapi import FastAPI,Response,status,HTTPException,Depends
# from fastapi.params import Body
# from typing import Optional,List
# from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
from . import models,schemas,utils
from .database import engine,get_db
from sqlalchemy.orm import Session
from .routers import posts,users,auth,vote
from .config import settings

from fastapi.middleware.cors import CORSMiddleware




# models.Base.metadata.create_all(bind=engine) #if this is uncommented then all the tables in my models.py will be automatically created and alembic wont do much
app = FastAPI()

origins = ["*"] #here we will provide domains that can talk to our API
app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

# while True:
# 	try:
# 		conn = psycopg2.connect(host = 'localhost',database='fastapi',user='postgres',password='changedpassword',cursor_factory=RealDictCursor)
# 		cursor = conn.cursor()
# 		print("Database Success")
# 		break
# 	except Exception as error:
# 		print("FALIUREEEEE",error)
# 		time.sleep(2)






