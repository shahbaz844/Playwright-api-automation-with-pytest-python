import json
import os

from helpers.api import APIManager
from utils.utils import Utils

search_test_data = Utils.get_test_data("test_data/search_pdl_test_data.json")
get_json_test_data = Utils.get_test_data("test_data/get_json_from_script_test_data.json")


class Helpers:

    @staticmethod
    def get_json_data(response, key):
        return json.loads(response.get(key))

    @staticmethod
    def get_data(response, key):
        for item in response:
            return item.get(key)

    @staticmethod
    def get_axis_value(main_key, key, axis):
        return main_key.get(key).get(axis)

    @staticmethod
    def get_json_id(response_data):
        json_ids = [response.get("render_sequence").get("output_name") for response in response_data]
        return json_ids

    @staticmethod
    def search_json_id(json_id, data_manager, headers):
        search_endpoint = f'{os.getenv("BASE_URL")}{search_test_data.get("endpoint")}{json_id}'
        APIManager.request("GET", search_endpoint, headers)
        response = data_manager.get_data(search_endpoint)
        response_data = response.json()
        return response_data

    @staticmethod
    def get_json_id_from_script(data_manager, headers, script):
        data = {
            "script": script,
            "isTestMode": "false",
            "project_id": 80,
            "scene_id": 425
        }

        endpoint = f'{os.getenv("BASE_URL")}{get_json_test_data.get("endpoint")}'

        APIManager.request("POST", endpoint, headers=headers, data=data, timeout=60)
        response = data_manager.get_data(endpoint)
        response_data = response.json()

        json_ids = [resp.get("render_sequence").get("output_name") for resp in response_data]

        return json_ids
