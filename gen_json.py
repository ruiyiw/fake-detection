import pandas as pd
import json


def gen_json(csv, json_name, img_dir):
    df = pd.read_csv(csv)\
    new_id = df["id"][:-1]
    name = df["user_name"][:-1]
    screen_name = df["user_screen_name"][:-1]
    description = df["user_description"][:-1]
    lang = df["lang"][:-1]
    total_len = len(new_id)
    
        
    for i in range(total_len):
        dict = {}
        dict["id"] = new_id


    with open(json_name, 'w') as f:
        json.dump(data, f)





gen_json("twitter_ids_small.csv", "")