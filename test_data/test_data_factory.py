class TestData:
    @staticmethod
    def get_time_position_error(value):
        return "Value '" + value + "' is not a valid choice."

    @staticmethod
    def get_invalid_search_id_error(search_id):
        return "JSON generate object having PDL id " + search_id + " doesn't exist"

    @staticmethod
    def get_png_notifier_message(json_id):
        return f'PNG sent successfully: {json_id}'
