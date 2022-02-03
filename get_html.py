import webbrowser
import pyautogui
import pandas as pd
# from pynput.keyboard import Key, Controller
import time
import json


def gen_html(csv):
    df = pd.read_csv(csv)
    screen_name = df["user_screen_name"][:-1]
    for i in range(len(screen_name)):
        name = screen_name[i]
        # Open browser in chrome
        webbrowser.open("https://twitter.com/{}".format(name))
        time.sleep(5)
        # Download html files with "Save Page WE"
        # TODO: Change hotkey to "ctrl", "l"
        pyautogui.hotkey('command', 'l')
        time.sleep(4)
        # Skip the pop up messages
        pyautogui.hotkey('enter')
        time.sleep(1)
        # Close the window
        pyautogui.hotkey('command','w')


def gen_remain_html(json_file):
    with open(json_file, 'r') as in_file:
        for line in in_file:
            screen_name = json.loads(line)["screen_name"]
            webbrowser.open("https://twitter.com/{}".format(screen_name))
            time.sleep(5)
            # Download html files with "Save Page WE"
            # TODO: Change hotkey to "ctrl", "l"
            pyautogui.hotkey('command', 'l')
            time.sleep(4)
            # Skip the pop up messages
            pyautogui.hotkey('enter')
            time.sleep(1)
            # Close the window
            pyautogui.hotkey('command','w')


def main():
    # gen_html(csv="twitter_ids_small.csv")
    gen_remain_html("record.jsonl")



if __name__ == '__main__':
    main()