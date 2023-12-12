#coding:utf-8

import os
import json
import datetime
from tkinter import messagebox

APP_VERSION     = "0.3"

JSON_FILE_NAME  = "config.json"
LOG_FILE_NAME   = "monitor.log"

class SetupManager:

    def __init__(self):

        self.JSON_FILE_NAME = JSON_FILE_NAME
        self.LOG_FILE_NAME  = LOG_FILE_NAME
        self.APP_VERSION    = APP_VERSION
    

    def setup_config_json_file(self):
        """
            return time_to_refresh, color_text, log_file
        """
        try:
            with open(self.JSON_FILE_NAME, "r") as config_file:
                data_config_json = json.load(config_file)
        except FileNotFoundError:
            messagebox.showwarning(f"Missing {self.JSON_FILE_NAME}", f"The {self.JSON_FILE_NAME} file was not found, we created it...")

            # create the deffault config.json
            default_config = {
                "time_to_refresh": 5,
                "max_process": 10,
                "log_file": False,
                "color_keys": "\u001b[95m",
                "color_values": "\u001b[92m"
            }

            with open(self.JSON_FILE_NAME, "w") as config_file:
                json.dump(default_config, config_file)
            data_config_json = default_config

        return data_config_json
    

    def create_log_file(self):
        if not os.path.exists(self.LOG_FILE_NAME):
            with open(self.LOG_FILE_NAME, 'w') as log_file:
                log_file.write("PID,Name,CPU %,Memory %\n")

    def log_process_info(self, process):
        if self.setup_config_json_file()["log_file"]:
            current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
            with open(LOG_FILE_NAME, 'a') as log_file:
                log_file.write(
                    f"{current_time}: {process.info['pid']}, {process.info['name']}, {process.info['cpu_percent']}, {process.info['memory_percent']}\n"
                )