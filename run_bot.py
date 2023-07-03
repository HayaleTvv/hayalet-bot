import yaml
import os

with open("config.yml", "r") as f:
    config = yaml.safe_load(f)

room_id = config.get("room_id")
api_token = config.get("api_token")
file_name = config.get("file_name")

if not room_id or not api_token:
    print("Please set the room_id and api_token in config.yml.")
else:
    os.system(f"highrise {file_name}:Bot {room_id} {api_token}")
