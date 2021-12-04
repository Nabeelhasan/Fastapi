

from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import database,schemas,models,utils,oauth2


router  = APIRouter(tags=['Authentication'])


@router.post('/login',response_model = schemas.Token)
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db: Session = Depends(database.get_db)):
	
	#OauthPasswordRequestForm has a username and a password field
	user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
	if not user:
		raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,detail = f"Invalid Credentials")

	#function implemented in utils to verify the password given in the form and the one that is stored in the database
	if not utils.verify(user_credentials.password,user.password):
		raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,detail=f"Invalid Credentials")

	#if the user credential are validated then this function is called  to create jwt token for the user id
	access_token = oauth2.create_access_token(data={"user_id":user.id})

	return {"access_token" : access_token,"token_type":"bearer"}