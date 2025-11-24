from selenium.webdriver.common.by import By

def test_google_title(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

def test_example_h1(driver):
    driver.get("https://example.com")
    text = driver.find_element(By.TAG_NAME, "h1").text
    assert "Example Domain" in text
