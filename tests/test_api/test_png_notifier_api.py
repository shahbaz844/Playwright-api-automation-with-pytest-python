import os
import logging as logger
from helpers.api import APIManager
from helpers.helpers import Helpers
from helpers.validate_manager import ValidateManager
from test_data.test_data_factory import TestData
from utils.utils import Utils

test_data = Utils.get_test_data("test_data/png_notifier_test_data.json")
endpoint = f'{os.getenv("BASE_URL")}{test_data.get("endpoint")}'


def test_png_notifier(data_manager, headers):
    script = (
        "INT. PIE HOLE CAFE - DAY\n\n"
        "COOKIE walks slow.\n\n"
        "COOKIE\n\n"
        "(English)\n\n"
        "Hi, my name is Cookie. Welcome to my world."
    )

    json_ids = Helpers.get_json_id_from_script(data_manager, headers, script)

    data = {
        "json_id": json_ids[0],
        "png_url": test_data.get("png_url")
    }

    APIManager.request("POST", endpoint, headers=headers, data=data)
    response = data_manager.get_data(endpoint)
    response_data = response.json()

    ValidateManager.validate_status_code(response.status_code, 200)
    logger.info("Validated API correct response on given valid data.")

    ValidateManager.validate_data(response_data.get("message"), TestData.get_png_notifier_message(json_ids[0]))
    logger.info("Validated that PNG is sent successfully")


def test_png_notifier_for_invalid_id(data_manager, headers):
    data = {
        "json_id": test_data.get("invalid_id"),
        "png_url": test_data.get("png_url")
    }

    APIManager.request("POST", endpoint, headers=headers, data=data)
    response = data_manager.get_data(endpoint)
    response_data = response.json()

    ValidateManager.validate_status_code(response.status_code, 404)
    logger.info("Validated response status code for invalid json_id.")

    ValidateManager.validate_data(response_data.get("message"), test_data.get("invalid_json_id_message"))
    logger.info("Validated error message on invalid json_id response.")


def test_png_notifier_api_with_missing_json_id(data_manager, headers):
    data = {
        "png_url": test_data.get("png_url")
    }

    APIManager.request("POST", endpoint, headers=headers, data=data)
    response = data_manager.get_data(endpoint)
    response_data = response.json()

    ValidateManager.validate_status_code(response.status_code, 400)
    logger.info("Validated response code for missing json_id in the response.")

    ValidateManager.validate_data(response_data.get("message"), test_data.get("missing_json_id_message"))
    logger.info("Validated error message for missing json_id in API data.")


def test_png_notifier_api_with_missing_png_url(data_manager, headers):
    script = (
        "INT. PIE HOLE CAFE - DAY\n\n"
        "COOKIE walks slow.\n\n"
        "COOKIE\n\n"
        "(English)\n\n"
        "Hi, my name is Cookie. Welcome to my world."
    )

    json_ids = Helpers.get_json_id_from_script(data_manager, headers, script)

    data = {
        "json_id": json_ids[0]
    }

    APIManager.request("POST", endpoint, headers=headers, data=data)
    response = data_manager.get_data(endpoint)
    response_data = response.json()

    ValidateManager.validate_status_code(response.status_code, 200)
    logger.info("Validated response status code for missing 'png_url' in the API data.")

    ValidateManager.validate_data(response_data.get("message"), test_data.get("missing_png_url_message"))
    logger.info("Validated error message on missing 'png_url' in the API data.")


def test_png_notifier_api_with_invalid_png_url(data_manager, headers):
    pass
