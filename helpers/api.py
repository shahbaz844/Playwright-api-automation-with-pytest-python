import os
import requests
from helpers.data_manager import DataManager
from utils.utils import Utils

data_manager = DataManager()
login_test_data = Utils.get_test_data("test_data/login_test_data.json")


class APIManager:

    @staticmethod
    def request(method, url, headers=None, params=None, data=None, json=None, timeout=60):

        """
        Makes an API call using the requests library.

        Args:
            method (str): The HTTP method ('GET', 'POST', 'PUT', 'DELETE', etc.).
            url (str): The URL for the API endpoint.
            headers (dict, optional): Dictionary of HTTP headers to send with the request.
            params (dict, optional): Dictionary of URL parameters to append to the URL.
            data (dict or str, optional): Data to send in the body of the request (for 'POST', 'PUT', etc.).
            json (dict, optional): JSON data to send in the body of the request (for 'POST', 'PUT', etc.).
            timeout (int, optional): Timeout for the request in seconds. Defaults to 30.

        Returns:
            dict: The JSON response from the API, if the request was successful.
            None: If the request failed or the response could not be decoded as JSON.
        """
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                data=data,
                json=json,
                timeout=timeout
            )

            data_manager = DataManager.get_instance()
            data_manager.set_data(url, response)

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"An error occurred: {req_err}")
        except ValueError as json_err:
            print(f"JSON decode error occurred: {json_err}")

        return None

    @staticmethod
    def get_auth_token(username, password):
        endpoint = f'{os.getenv("BASE_URL")}{login_test_data["endpoint"]}'

        data = {
            "username": username,
            "password": password
        }

        headers = {
            "Content-Type": "application/json",
            "Host": os.getenv("HOST"),
            "Origin": os.getenv("ORIGIN_URL")
        }

        APIManager.request("POST", endpoint, headers=headers, json=data)
        response = data_manager.get_data(endpoint)
        return response.json()["token_access"]
