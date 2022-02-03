FILES:
- get_html.py
- extract_id.py
- twitter_ids_small.csv
- twitter_ids.csv

install:
- pandas
- pyautogui
- webbrowser

1. Go to the link: https://chrome.google.com/webstore/detail/save-page-we/dhhpefjklgkmgeafimnjhojgjamoafof
2. Create hot key for this extension (ctrl+L)
3. Make sure you login your facebook using chrome.google.com
4. Run get_html.py (please first try on the "twitter_ids_small.csv")
5. After getting all htmls (this may take longer than 10 hours), run image_extraction.pyautogui
6. Send two folders containing all the htmls and avatars, along with the json file. 
