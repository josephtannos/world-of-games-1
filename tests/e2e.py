import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

URL = "http://127.0.0.1:5000"


def test_score_service(url: str) -> bool:
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)
        score = int(driver.find_element("id", "score"))
        if score > 0 and score < 1000:
            return True
        return False
    except:
        return False
    finally:
        driver.close()


if __name__ == '__main__':
    url = os.getenv("URL", URL)
    if test_score_service(url):
        exit(0)
    exit(-1)