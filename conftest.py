import os
import pytest
import logging
from dotenv import load_dotenv
from helpers.api import APIManager
from helpers.data_manager import DataManager

load_dotenv()


@pytest.fixture(autouse=True)
def configure_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)


@pytest.fixture(scope="session")
def data_manager():
    data_manager = DataManager()
    yield data_manager


@pytest.fixture(scope="session")
def headers():
    access_token = APIManager.get_auth_token(os.getenv("USERNAME"), os.getenv("PASSWORD"))
    headers = {
        "Authorization": f'Bearer {access_token}'
    }
    yield headers
