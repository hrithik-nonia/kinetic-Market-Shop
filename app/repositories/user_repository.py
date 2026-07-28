# built in module imports
from typing import Optional


# custom module imports
from app.database.mongodb import get_database
from app.models.user_model import UserModel



class UserRepository:
  # constructor function when class is called
  def __init__(self):
    self.collection_name="users"


  # A method which create collection
  def _get_collection(self):
    db=get_database()
    return db[self.collection_name]


  # find a user in DB by email
  async def find_by_email(self , email : str )-> Optional[dict]:
    collection = self._get_collection()
    user = await collection.find_one({"email" : email})
    return user


  # insetr user into DB
  async def create(self , user : UserModel)-> dict:
    collection = self._get_collection()
    user_dict = user.model_dump(by_alias= True , exclude= {"id"})
    result = await collection.insert_one(user_dict)
    created_user = await collection.find_one({"_id" : result.inserted_id})
    return created_user


# ===========================
  # set refresh token 


# ===========================


user_repository = UserRepository()

  