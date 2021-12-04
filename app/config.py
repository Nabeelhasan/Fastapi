


from pydantic import BaseSettings

#setting up our configuration for the project 
class Settings(BaseSettings):
	database_hostname:str
	database_port:str
	database_password:str
	database_name:str
	database_username:str
	secret_key:str
	algorithm:str
	access_token_expire_minutes:int

	class Config:
		env_file = ".env" #referring to the .env file where the config is stored

settings = Settings()
