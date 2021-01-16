import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import BASE_URL, TEST_SEARCH_TERMS


def create_query(term):
    single_term_for_query = term.replace(' ', '+')
    url = BASE_URL + single_term_for_query
    print(f"Using Youtube URL: {url}")
    return url


def get_link(url):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(chrome_options=options, executable_path='chromedriver.exe')
    driver.get(url)
    driver.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
    all_links = [my_href.get_attribute("href") for my_href in WebDriverWait(driver, 5).until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.ytd-video-renderer#video-title")))]
    link = all_links[0]
    print(f"Extracted link: {link}")
    return link


def single_term_to_yt_link(term):
    url = create_query(term)
    link = get_link(url)
    return link


def search_terms_to_yt_link(search_terms):
    result_links = []
    for term in search_terms:
        link = single_term_to_yt_link(term)
        result_links.append(link)
    return result_links


if __name__ == '__main__':
    SEARCH_TERMS = sys.argv[1:]
    search_terms_to_yt_link(SEARCH_TERMS)
