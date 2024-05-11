import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import random
import json
import time
from datetime import datetime
from termcolor import colored

class IDA:
    def __init__(self):
        self.proxy_key = None
        self.proxy_url = 'https://advanced.name/freeproxy/'
        self.open_proxy_link()
        self.username = input(colored('[?] Username: ', 'blue'))
        self.username = self.username.replace('@', '')  
        self.server_log = None
        self.data_json = None
        self.admin()

    def open_proxy_link(self):
        print(colored(
            f"To Get The Key Enter This URL And solve the captcha ex.({self.proxy_url}<key>)",
            'red'
        ))
        self.proxy_key = input('Key: ')
        self.proxy_url += self.proxy_key

    def admin(self):
        self.send_request()
        self.to_json()
        self.output()

    def send_request(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 IDA'
        }
        self.response = requests.get(f"https://www.tiktok.com/@{self.username}", headers=headers)
        self.server_log = self.response.text

    def to_json(self):
        try:
            soup = BeautifulSoup(self.response.text, 'html.parser')
            script_tag = soup.find('script', id='__UNIVERSAL_DATA_FOR_REHYDRATION__')
            script_text = script_tag.text.strip()
            self.json_data = json.loads(script_text)['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']
        except Exception:
            print(colored('[X] Error: Username Not Found.', 'red'))
            exit()

    def get_user_id(self):
        try:
            data = self.json_data
            return data["user"]["id"]
        except Exception:
            return 'Unknown'

    def secUid(self):
        try:
            data = self.json_data
            return data["user"]["secUid"]
        except Exception:
            return 'Unknown'

    def generate_report_url(self):
        base_url = 'https://www.tiktok.com/aweme/v2/aweme/feedback/?'

        browser_name = random.choice(['Mozilla', 'Chrome', 'Safari', 'Firefox'])
        browser_platform = random.choice(['Win32', 'Mac', 'Linux'])
        browser_version = f"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) {browser_name}/{random.randint(80, 120)}.0 Safari/537.36"
        current_region = random.choice(['US', 'UK', 'CA', 'AU', 'IN', 'BR', 'FR', 'DE', 'IT', 'ES'])
        device_id = str(random.randint(10**18, 10**19))
        is_fullscreen = str(random.choice([True, False])).lower()
        os = random.choice(['windows', 'mac', 'linux'])
        priority_region = random.choice(['US', 'UK', 'CA', 'AU', 'IN', 'BR', 'FR', 'DE', 'IT', 'ES'])
        region = random.choice(['US', 'UK', 'CA', 'AU', 'IN', 'BR', 'FR', 'DE', 'IT', 'ES'])
        screen_height = str(random.randint(600, 1080))
        screen_width = str(random.randint(800, 1920))
        tz_name = random.choice(['America/New_York', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney', 'Asia/Kolkata', 'America/Los_Angeles', 'Europe/Paris', 'Asia/Dubai', 'America/Sao_Paulo', 'Asia/Shanghai'])
        webcast_language = random.choice(['en', 'es', 'fr', 'de', 'ja', 'pt', 'it', 'ru', 'ar', 'hi'])

        params = {
            'aid': '1988',
            'app_language': 'en',
            'app_name': 'tiktok_web',
            'browser_language': 'en-US',
            'browser_name': browser_name,
            'browser_online': 'true',
            'browser_platform': browser_platform,
            'browser_version': browser_version,
            'channel': 'tiktok_web',
            'cookie_enabled': 'true',
            'current_region': current_region,
            'device_id': device_id,
            'device_platform': 'web_pc',
            'focus_state': 'true',
            'from_page': 'user',
            'history_len': '1',
            'is_fullscreen': is_fullscreen,
            'is_page_visible': 'true',
            'lang': 'en',
            'nickname': quote(self.username),
            'object_id': self.get_user_id(),
            'os': os,
            'priority_region': priority_region,
            'reason': '9010',
            'referer': 'https://www.tiktok.com/',
            'region': region,
            'report_type': 'user',
            'reporter_id': self.get_user_id(),
            'root_referer': 'https://www.tiktok.com/',
            'screen_height': screen_height,
            'screen_width': screen_width,
            'secUid': self.secUid(),
            'target': self.get_user_id(),
            'tz_name': tz_name,
            'webcast_language': webcast_language
        }

        report_url = base_url + '&'.join([f"{k}={v}" for k, v in params.items()])
        return report_url

    def output(self):
        report_url = self.generate_report_url()
        tiktok_url = report_url

        while True:
            proxies = requests.get(self.proxy_url).text.splitlines()

            for proxy in proxies:
                try:
                    current_time = datetime.now().strftime('%H:%M:%S')
                    response = requests.post(
                        tiktok_url,
                        proxies={'http': f'http://{proxy}'},
                        timeout=2
                    )
                    print(
                        colored(f"[{current_time}]", 'red') + 
                        f" {colored(f'Proxy: {proxy}', 'blue')} Report Sent To {colored(self.username, 'green')}"
                    )
                except Exception as e:
                    print(colored(f"Something went wrong: {e}", 'red'))
            time.sleep(1)

if __name__ == "__main__":
    print(colored(
        """
████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗   ██████╗  █████╗ ███╗   ██╗
╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝   ██╔══██╗██╔══██╗████╗  ██║
   ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝    ██████╔╝███████║██╔██╗ ██║
   ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗    ██╔══██╗██╔══██║██║╚██╗██║
   ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗██╗██████╔╝██║  ██║██║ ╚████║
   ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
                               GitHub: LeetIDA                                    
""", 'magenta'))
    IDA()
