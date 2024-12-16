from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://www.olx.com")
    categories = driver.find_elements(By.XPATH, "//div[@data-testid='home-categories-menu-row']/a")
    if not categories:
        print("Категорії не знайдено!")
        driver.quit()
        exit()
    category_links = []
    for category in categories:
        category_links.append(category.get_attribute("href"))

    driver.get(random.choice(category_links))
    print('Категорія - ', driver.find_element(By.XPATH, "//div[@data-cy='category-dropdown']").text)
    top_product = driver.find_elements(By.XPATH, "//div[@data-cy='l-card' and .//*[contains(text(), 'ТОП')]]")
    if not top_product:
        print("ТОП продукти не знайдено.")
        exit()
    for product in top_product:
        name = product.find_element(By.XPATH, ".//h4").text
        price_el = product.find_element(By.XPATH, ".//p[@data-testid='ad-price']")
        price = price_el.text
        for child in price_el.find_elements(By.XPATH, "./*"):
            price = price.replace(child.text, "").strip()
        print(f'{name:50}    {price:10}')
finally:
    driver.quit()
