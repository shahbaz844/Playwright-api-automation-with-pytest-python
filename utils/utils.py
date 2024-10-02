import json
import time
import random
import string


class Utils:

    @staticmethod
    def get_test_data(file_path):
        with open(file_path) as f:
            return json.load(f)

    @staticmethod
    def generate_unique_register_data():
        base_email = "user"
        timestamp = int(time.time())
        random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        unique_email = f"{base_email}_{timestamp}_{random_str}@yopmail.com"
        return {"username": base_email + random_str, "unique_email": unique_email}

    @staticmethod
    def generate_random_str():
        random_str = random.randint(1, 100000)
        return random_str
