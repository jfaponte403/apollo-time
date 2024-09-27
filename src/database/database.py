import os
import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine, exc

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

if not all([POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB]):
    logger.error("One or more environment variables are missing.")
    raise ValueError("Please ensure that all environment variables are set correctly.")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

try:
    logger.info("Creating the database engine...")
    engine = create_engine(DATABASE_URL)

    with engine.connect() as connection:
        logger.info("Connection to the database was successful!")
except exc.SQLAlchemyError as e:
    logger.error(f"An error occurred while connecting to the database: {e}")
    raise
except Exception as e:
    logger.error(f"An unexpected error occurred: {e}")
    raise
