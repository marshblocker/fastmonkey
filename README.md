# fastmonkey
Python script that programmatically plays [monkeytype](monkeytype.com).

## How to build.
```
git clone https://github.com/marshblocker/fastmonkey.git
cd fastmonkey
python -m pip install -r requirements.txt
```
Note that this script is only compatible with Chrome v99. If you want to run this
in a specific version of Chrome, download its respective Chrome driver 
[here](https://chromedriver.storage.googleapis.com/index.html) and replace the existing
Chrome driver in `fastmonkey/chromedriver_win32`. Just take note that only the driver for
Chrome v99 was tested.

## How to run.
In the _fastmonkey_ directory, run `python fastmonkey.py`.

**Important Note:** Since the program performs keyboard input by itself, do not touch 
your mouse and keyboard while it is running. For precaution, wait for a minimum of
five seconds after the program ended before touching your mouse and keyboard again.

## Dependencies
* [Selenium](https://www.selenium.dev/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [pyautogui](https://github.com/asweigart/pyautogui)
