import json
from Responses_Keys import *
import Security

json_file = "C:/Users/HP/Desktop/Projects/Python/Robin_Beta_v4/Robin_AI/Data/Robin_Settings.json"
Write = False


def save_data(username, opt):
    global Write

    key_file = Security.key_file_settings
    Security.decryption_file(key_file, json_file)

    with open(json_file, "r+") as file:
        if Write:
            json.dump(default_settings_dict, file)
            Write = False
            quit()

        data = json.load(file)
        data["User_Name"] = username
        data["Voice"] = opt
        file.seek(0)

        json.dump(data, file, indent=4)
        file.truncate()

        Security.encryption_file(key_file, json_file)


def data_receiver():
    key_file = Security.key_file_settings
    Security.decryption_file(key_file, json_file)

    with open(json_file, "r") as _file:
        data_received = json.load(_file)

        Security.encryption_file(key_file, json_file)
        return data_received
