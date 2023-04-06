# SCRIPT NAME: Get Data
# DEFINITION: 
# AUTHOR: JTA
# LAST MODIFIED: april 5th, 2023

#Libraries
import os #file management
from dotenv import load_dotenv, find_dotenv #load secrets

#Functions
def getSecrets()->None:
    """
    # Definition
    Loads env variables from .env file
    # Parameters
    - path(str): path to .env file
    # Return
    None
    """
    load_dotenv(find_dotenv()) #searches and loads .env file into runtime
    secrets = {"API_KEY":os.environ.get("API_KEY"),
               "DB_USER":os.environ.get("DB_USER"),
               "DB_PSW":os.environ.get("DB_PSW"),
               "DB_HOST":os.environ.get("DB_HOST"),
               "DB_PORT":os.environ.get("DB_PORT")}
    
    return secrets

#Main Process
secrets = getSecrets() #Loads env variables
print(secrets)