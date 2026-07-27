# built in module imports
from fastapi import FastAPI
from contextlib import asynccontextmanager


# custom module imports
from app.database.mongodb import connect_to_mongo, close_mongodb_connection
from app.config.setting import setting



# do db connection before starting app and close db connection after app colse 
@asynccontextmanager
async def app_lifespan(app: FastAPI):
  # connect DB
  await connect_to_mongo()

  # jab tak app run kar raha hai DB connect rahe ga function pause rahega
  yield

  # close DB conntction after app close
  await close_mongodb_connection()



app=FastAPI(title = setting.PROJECT_NAME, lifespan = app_lifespan)


@app.get("/")
def home():
  return {"hello " : "server is running"}