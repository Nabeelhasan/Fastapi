

from jose import JWTError,jwt
from datetime import datetime,timedelta
from . import schemas,database,models
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings

#SECRET KEY
#ALGORITHM
#EXPIRATION TIME

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'login')

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict):
	to_encode = data.copy()
	expire = datetime.utcnow()+timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)

	to_encode.update({"exp":expire})
	encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm = ALGORITHM)
	return encoded_jwt


def verify_access_token(token:str,credentials_exception):
	try:
		#the jwt access token will be decoded here and its id will be fetched
		payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
		id: str = payload.get("user_id")

		if id is None:
			raise credentials_exception

		token_data = schemas.TokenData(id = id)
	except JWTError:
		raise credentials_exception

	return token_data

#when i mention current user in the request method i get redirected here and it call oauth2_scheme where login URL is mentioned 
#then it reads user credentials from the url form also db is mentioned which created a session with the database
#the token datatype mentioned here in the function paramter will store the access token 
def get_current_user(token: str = Depends(oauth2_scheme),db: Session = Depends(database.get_db)):
	credentials_exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,detail=f"could not validate credentials",headers = {"WWW-Authenticate":"Bearer"})
	
	#the created jwt token will be verified using this function
	token = verify_access_token(token,credentials_exception)
	user = db.query(models.User).filter(models.User.id == token.id).first() #here that returned token id from verifiy_access_token function will be matched

	return user






