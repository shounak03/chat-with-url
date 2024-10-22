from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup 

SBR_WEBDRIVER = 'https://brd-customer-hl_de40e538-zone-url_scrapper:zvuq58t6zlgf@brd.superproxy.io:9515'

def scrape_url(url):
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating to https://example.com...')
        driver.get(url)
        # CAPTCHA handling: If you're expecting a CAPTCHA on the target page, use the following code snippet to check the status of Scraping Browser's automatic CAPTCHA solver
        print('Waiting captcha to solve...')
        solve_res = driver.execute('executeCdpCommand', {
            'cmd': 'Captcha.waitForSolve',
            'params': {'detectTimeout': 10000},
        })
        print('Captcha solve status:', solve_res['value']['status'])
        print('Navigated! Scraping page content...')
        html = driver.page_source
        print(html)


def extract_body(content):
    soup = BeautifulSoup(content, 'html.parser')
    body = soup.body
    if body:
        return str(body)
    return ""

def clean_body(content):
    soup = BeautifulSoup(content,'html.parser')

    for s in soup(["script","style"]):
        s.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )
    return cleaned_content

def split_content(content,max_length=6000):
    return[
        content[i:i+max_length] for i in range(0, len(content),max_length)
    ]