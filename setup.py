#coding:utf-8

from tkinter import messagebox
import json

JSON_FILE_NAME = "config.json"

class SetupManager:

    def __init__(self):

        self.JSON_FILE_NAME = JSON_FILE_NAME
    
    def setup_config_json_file(self):
        
        """
            return TIME_TO_REFRESH, COLOR_TEXT
        """

        try:
            with open(self.JSON_FILE_NAME, "r") as config_file:
                data_config_json = json.load(config_file)
        except FileNotFoundError:
            messagebox.showwarning(f"Missing {self.JSON_FILE_NAME}", f"The {self.JSON_FILE_NAME} file was not found, we created it...")

            default_config = {
                "time_to_refresh": 5,
                "color_text": "\u001b[92m"
            }

            with open(self.JSON_FILE_NAME, "w") as config_file:
                json.dump(default_config, config_file)
            data_config_json = default_config

        TIME_TO_REFRESH = data_config_json.get("time_to_refresh", 5)
        COLOR_TEXT      = data_config_json.get("color_text", "\u001b[92m")

        return TIME_TO_REFRESH, COLOR_TEXT
