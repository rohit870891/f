import asyncio
from pyppeteer import launch

LOGIN_URL = "https://www.terabox.com"  # You can change to https://www.1024tera.com if needed

async def login_and_extract_cookies():
    print("[*] Launching browser...")
    browser = await launch(headless=False, args=['--no-sandbox'])
    page = await browser.newPage()

    print(f"[*] Navigating to {LOGIN_URL}")
    await page.goto(LOGIN_URL, {"waitUntil": "networkidle2"})

    print("[!] Please log in manually and solve any CAPTCHA if shown.")
    print("[*] You have 60 seconds...")

    await asyncio.sleep(60)  # Wait for user to complete login manually

    print("[*] Extracting cookies...")
    cookies = await page.cookies()
    for c in cookies:
        print(f"{c['name']}={c['value']}")

    await browser.close()
    print("[+] Done.")

if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(login_and_extract_cookies())
    except Exception as e:
        print(f"[!] Error: {e}")