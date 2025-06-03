import requests
#from config import TERABOX_EMAIL, TERABOX_PASSWORD

TERABOX_EMAIL = "gurugaming385@gmail.com"
TERABOX_PASAWORD = "Aquib#4154"

def login_and_get_cookies():
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    data = {
        "login_email": TERABOX_EMAIL,
        "login_pwd": TERABOX_PASSWORD,
        "login_type": "1"
    }

    print("[*] Logging in...")
    response = session.post("https://www.1024tera.com/api/user/login", data=data, headers=headers)

    if response.status_code == 200:
        cookies = session.cookies.get_dict()
        if "ndus" in cookies:
            print("[+] Login successful. Cookies:")
            for key, value in cookies.items():
                print(f"{key}={value}")
            return cookies
        else:
            raise Exception("Login succeeded but expected cookies not found.")
    else:
        raise Exception(f"Login failed with status code {response.status_code}: {response.text}")

if __name__ == "__main__":
    try:
        login_and_get_cookies()
    except Exception as e:
        print(f"[!] Error: {e}")