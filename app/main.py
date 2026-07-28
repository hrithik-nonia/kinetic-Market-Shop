# built in module imports
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


# custom module imports
from app.database.mongodb import connect_to_mongo, close_mongodb_connection
from app.config.setting import setting
from app.custom_exception.exception_handler import register_exception_handlers
from app.routes.auth_route import router as auth_router




# do db connection before starting app and close db connection after app colse 
@asynccontextmanager
async def app_lifespan(app: FastAPI):
  # connect DB
  await connect_to_mongo()

  # jab tak app run kar raha hai DB connect rahe ga function pause rahega
  yield

  # close DB conntction after app close
  await close_mongodb_connection()


# create a fastapi instanse
app=FastAPI(title = setting.PROJECT_NAME, lifespan = app_lifespan)

# add cors middleware
app.add_middleware(
  CORSMiddleware,
  allow_origins=[
    "http://localhost:5173",   # react dev server
    "http://localhost:5174"    # react buile server
  ],
  allow_credentials=True,
  allow_headers=["*"],
  allow_methods=["*"]
)


# register exception handler
register_exception_handlers(app)


# register auth routes
app.include_router(auth_router)



@app.get("/")
def home():
  return {"hello " : "server is running"}