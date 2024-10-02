import re

from utils.utils import Utils

get_validations_test_data = Utils.get_test_data("test_data/common_test_data.json")


class ValidateManager:

    @staticmethod
    def validate_status_code(actual_status, expected_status):
        ValidateManager.validate_data(actual_status, expected_status)

    @staticmethod
    def validate_key_in_response(response, key):
        assert key in response.json(), f"Key '{key}' not found in response"

    @staticmethod
    def validate_key_value(response, key, expected_value):
        assert response.json().get(
            key) == expected_value, f"Expected value for key '{key}' is '{expected_value}', " \
                                    f"but got '{response.json().get(key)}'"

    @staticmethod
    def validate_value_is_not_null(expected_value):
        assert expected_value is not None, "Expected value to not be null."

    @staticmethod
    def validate_data(actual_value, expected_value):
        assert actual_value == expected_value, f"Expected {expected_value}, but got {actual_value}."

    @staticmethod
    def validate_string_against_regex(expected_value, regular_expression):
        assert re.match(regular_expression,
                        expected_value), f"Expected {expected_value} to match pattern {regular_expression.pattern}."

    @staticmethod
    def validate_key_exclusion(response, excluded_key):
        assert excluded_key not in response, f"Expected response to not include the key '{excluded_key}'."

    @staticmethod
    def validate_key_value_in_list(response, key, index, expected_value):
        assert response.json().get(
            key)[
                   index] == expected_value, f"Expected value for key '{key}' is '{expected_value}', " \
                                             f"but got '{response.json().get(key)}'"

    @staticmethod
    def validate_is_value_true(value):
        assert value is True, 'Expected value is False'

    @staticmethod
    def validate_is_value_false(value):
        assert value is False, 'Expected value is True'

    @staticmethod
    def validate_is_value_string(value):
        assert isinstance(value, str) and value, f'value "{value}" is an empty string.'

    @staticmethod
    def validate_is_value_number(value):
        assert isinstance(value, int), f'value "{value}" is not a number.'

    @staticmethod
    def validate_url(url):
        assert url.startswith(get_validations_test_data.get("s3_url")) and \
               (url.endswith(".blend") or url.endswith(".fbx")), \
            f'Some issue with the url: {url}'

    @staticmethod
    def validate_wav_url(url):
        assert url.startswith(get_validations_test_data.get("audio_url")) and \
               (url.endswith(".wav")), f'Some issue with the url: {url}'

    @staticmethod
    def validate_blend_url(response):
        assert response.get("blend_file").startswith(get_validations_test_data.get("s3_console")) and \
               (response.get("blend_file").endswith(".blend")), f'Some issue with the url: {response.get("blend_file")}'

    @staticmethod
    def validate_axis(value):
        assert isinstance(value, (int, float)), f'Value {value} is not an integer or float'
        # assert 0 <= value <= 360, f'Value {value} is out of range'

    @staticmethod
    def validate_is_value_int_or_float(value):
        assert isinstance(value, (int, float)), f'Value {value} is not an integer or float'

    @staticmethod
    def validate_data_in_list_of_values(list_of_values, value):
        assert value in list_of_values, f'Value "{value}" does not exist in list {list_of_values}'

    @staticmethod
    def validate_is_date_valid(response, date):
        ValidateManager.validate_string_against_regex(response.get("date"), date)

    @staticmethod
    def validate_is_time_valid(response, time):
        ValidateManager.validate_string_against_regex(response.get("time"), time)

    @staticmethod
    def validate_is_json_logs_valid(response, search_id):
        json_logs = response.get("JSON_LOGS")
        assert json_logs.startswith(get_validations_test_data.get("json_logs")) and \
               (json_logs.endswith(search_id)), f'Some issue with the url: {json_logs}'

    @staticmethod
    def validate_length(data):
        assert data, f'Data is empty.'

    @staticmethod
    def validate_is_value_null(value):
        assert value is None, "Expected value to be None but got a different value."

    @staticmethod
    def validate_keys_in_response_dict(response, keys):
        for key in keys:
            assert key in response, f"Key '{key}' not found in response"

    @staticmethod
    def validate_string_contains_text(keyword, text):
        assert keyword.lower() in text.lower(), f"Expected '{text}' to contain the keyword '{keyword}'"
