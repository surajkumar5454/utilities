import requests
import json


class MakeApiCall:

    def get_user_data_with_parameter(self, api, parameters):
        response = requests.get(f"{api}", params=parameters)
        if response.status_code == 200:
            print("sucessfully fetched the data with parameters provided")
            self.formatted_print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")

    def get_user_data(self, api):
        response = requests.get(f"{api}")
        if response.status_code == 200:
            print("sucessfully fetched the data with parameters provided")
            self.formatted_print(response.json())
        else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")

    def formatted_print(self, obj):
        text = json.dumps(obj, sort_keys=False, indent=4)
        print(text)
        data = json.loads(text)
        # for data in parsedData:
        print(data["number"])
        print(data["square"])

    def __init__(self, api):
        # self.get_data(api)

        parameters = {
            "username": "kedark"
        }
        self.get_user_data(api)


if __name__ == "__main__":
    # number = input("Enter your number:  ")
    api_call = MakeApiCall("https://todo-surajcode.herokuapp.com/api/5")
# api_call = MakeApiCall("https://dev.to/api/articles")
# api_call = MakeApiCall("http://127.0.0.1:5000/NAMEAPI/suraj")
