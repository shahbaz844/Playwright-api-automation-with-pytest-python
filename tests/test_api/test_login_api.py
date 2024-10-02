import os
import re
import pytest
import logging as logger
from helpers.api import APIManager
from helpers.validate_manager import ValidateManager
from utils.utils import Utils

login_test_data = Utils.get_test_data("test_data/login_test_data.json")
token_test_data = Utils.get_test_data("test_data/token_validation_test_data.json")
endpoint = f'{os.getenv("BASE_URL")}{login_test_data["endpoint"]}'
token_endpoint = f'{os.getenv("BASE_URL")}{token_test_data["endpoint"]}'


@pytest.fixture
def request_headers():
    yield {
        "Content-Type": "application/json",
        "Host": os.getenv("HOST"),
        "Origin": os.getenv("ORIGIN_URL")
    }


def test_login_api_with_valid_data(request_headers, data_manager):
    msg_regex = re.compile(login_test_data["message_pattern"])
    token_regex = re.compile(login_test_data["access_token_pattern"])

    data = {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD")
    }

    APIManager.request("POST", endpoint, headers=request_headers, json=data)
    response = data_manager.get_data(endpoint)
    response_data = response.json()

    ValidateManager.validate_status_code(response.status_code, 200)
    ValidateManager.validate_value_is_not_null(response)
    logger.info("Validated response is correct and not null.")

    ValidateManager.validate_value_is_not_null(response_data.get("message"))
    ValidateManager.validate_string_against_regex(response_data.get("message"), msg_regex)
    logger.info("Validated 'message' exist in response with correct value.")

    ValidateManager.validate_value_is_not_null(response_data.get("username"))
    ValidateManager.validate_is_value_string(response_data.get("username"))
    logger.info("Validated 'username' exist in response with correct value.")

    ValidateManager.validate_value_is_not_null(response_data.get("token_access"))
    ValidateManager.validate_string_against_regex(response_data.get("token_access"), token_regex)
    logger.info("Validated 'access token' exist in response with correct value.")

    ValidateManager.validate_value_is_not_null(response_data.get("user_id"))
    ValidateManager.validate_is_value_number(response_data.get("user_id"))
    logger.info("Validated 'user_id' exist in response with correct value.")

    headers = {
        "Authorization": f'Bearer {response_data.get("token_access")}'
    }

    APIManager.request("GET", token_endpoint, headers=headers)
    response = data_manager.get_data(token_endpoint)
    response_data = response.json()

    ValidateManager.validate_status_code(response.status_code, 200)
    ValidateManager.validate_is_value_true(response_data.get("isValidToken"))
    logger.info("Validated 'access token' in response via token validation API.")


def test_login_api_with_invalid_data(request_headers, data_manager):
    data = {
        "username": os.getenv("USERNAME"),
        "password": login_test_data.get("invalid_password")
    }

    APIManager.request("POST", endpoint, headers=request_headers, json=data)
    response = data_manager.get_data(endpoint)
    response_data = response.json()

    ValidateManager.validate_status_code(response.status_code, 401)
    ValidateManager.validate_value_is_not_null(response)
    logger.info("Validated response is correct for invalid login data.")

    ValidateManager.validate_key_exclusion(response, "message")
    ValidateManager.validate_key_exclusion(response, "username")
    ValidateManager.validate_key_exclusion(response, "token_access")
    logger.info("Validated response contain no access token, username with invalid data passed in login.")

    ValidateManager.validate_value_is_not_null(response_data.get("error"))
    ValidateManager.validate_key_value(response, "error", login_test_data["invalid_data_error"])
    logger.info("Validated generated error on invalid data for login.")


def test_login_with_missing_password(request_headers, data_manager):
    data = {
        "username": os.getenv("USERNAME")
    }

    APIManager.request("POST", endpoint, headers=request_headers, json=data)
    response = data_manager.get_data(endpoint)

    ValidateManager.validate_status_code(response.status_code, 401)
    ValidateManager.validate_value_is_not_null(response)
    logger.info("Validated response is correct for missing password in login data.")

    ValidateManager.validate_key_in_response(response, "error")
    ValidateManager.validate_key_value(response, "error", login_test_data["missing_data_error"])
    logger.info("Validated generated error on missing password in login data.")


def test_login_with_missing_username(request_headers, data_manager):
    data = {
        "password": os.getenv("PASSWORD")
    }

    APIManager.request("POST", endpoint, headers=request_headers, json=data)
    response = data_manager.get_data(endpoint)

    ValidateManager.validate_status_code(response.status_code, 401)
    ValidateManager.validate_value_is_not_null(response)
    logger.info("Validated response is correct for missing username in login data.")

    ValidateManager.validate_key_value(response, "error", login_test_data["missing_data_error"])
    logger.info("Validated generated error on missing username in login data.")
