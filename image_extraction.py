from bs4 import BeautifulSoup
import os
import wget
import json
import requests

# TODO: Change file directory and image directory
file_dir = "/Users/pamela/Documents/research/fake-detection/twitter_html/"
img_dir = "/Users/pamela/Documents/research/fake-detection/avatar/"

avatar = {}

for file in os.listdir(file_dir):
    filename = os.fsdecode(file)
    if filename.endswith(".html"):
        # Define soup
        soup = BeautifulSoup(open(os.path.join(file_dir,filename)), "html.parser")
        # Extract image url from html
        img_div = soup.find(property="og:image")
        # Check if img_url exists
        if not img_div:
            continue
        if img_div.has_attr("content"):
            img_url = img_div["content"]
            # Download the image with higher resolution: from "..._normal.jpg" to "..._400x400.jpg"
            img_surfix = img_url[len(img_url)-10:len(img_url)]
            img_url_high = img_url[0:len(img_url)-10] + "400x400" + img_surfix[len(img_surfix)-4:len(img_surfix)]
        else:
            img_url_high = "https://abs.twimg.com/sticky/default_profile_images/default_profile_400x400.png"
            print("No image file shown in the HTML")

        screen_name = os.path.splitext(filename)[0]
        # Include avatar to a json file
        avatar[screen_name] = img_url
        destination = img_dir + screen_name + ".jpg"
        # Check if the destination already exists in the avatar folder:
        if os.path.exists(destination):
            print("Img file already exists.")
            continue
        # Check if the url exists
        if requests.get(img_url_high).status_code != 200:
            print("URL not exists.")
            img_url_high = "https://abs.twimg.com/sticky/default_profile_images/default_profile_400x400.png"
            # Use default avatar
        msg = wget.download(img_url_high, out=destination)
        print(msg)

# TODO: Change file directory
# with open("profile/avatar_small.json", 'w') as outfile:
#     json.dump(avatar, outfile)
