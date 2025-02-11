import json
import os


    def load_json():
        json_path = "/nas/api_project/project_metadata.json"

        if not os.path.exists(json_path):
            assignee = {}
            return assignee

        with open(json_path, "r") as file:
            assignee = json.load(file)
            return assignee

    def write_json(assignee):
        json_path = "/nas/api_project/project_metadata.json"
        with open(json_path, "w")as file:
            json.dump(assignee, file, ensure_ascii=False, indent=4)