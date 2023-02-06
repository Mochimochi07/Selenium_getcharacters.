
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


driver.get("https://capcom.fandom.com/wiki/Mega_Man:_The_Power_Battle")


characters_table = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//table[@class='article-table']"))
)

rows = characters_table.find_elements(By.XPATH, "./tbody/tr")

characters = [row.find_element(By.XPATH, "./td[1]").text for row in rows]

print(characters)

driver.quit()
