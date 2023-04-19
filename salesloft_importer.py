from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SalesLoftImporter:
    def __init__(self, username, password, csv_file_path):
        self.username = username
        self.password = password
        self.csv_file_path = csv_file_path
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def locators(self):
        return {
            'email_input': (By.NAME, 'user[email]'),
            'password_input': (By.NAME, 'user[password]'),
            'import_button': (By.CSS_SELECTOR, '.import-people-button'),
            'file_upload_input': (By.CSS_SELECTOR, '.file-upload-input'),
            'start_import_button': (By.CSS_SELECTOR, '.start-import-button'),
            'import_status_message': (By.CSS_SELECTOR, '.import-status-message')
        }

    def login(self):
        self.driver.get("https://accounts.salesloft.com/users/sign_in")
        self.driver.find_element(*self.locators()['email_input']).send_keys(self.username)
        self.driver.find_element(*self.locators()['password_input']).send_keys(self.password)
        self.driver.find_element(*self.locators()['password_input']).send_keys(Keys.RETURN)
        self.wait.until(EC.url_contains("app.salesloft.com"))

    def import_csv(self):
        self.driver.get("https://app.salesloft.com/app/people")
        self.wait.until(EC.element_to_be_clickable(self.locators()['import_button'])).click()
        self.wait.until(EC.presence_of_element_located(self.locators()['file_upload_input'])).send_keys(self.csv_file_path)
        self.driver.find_element(*self.locators()['start_import_button']).click()
        self.wait.until(EC.text_to_be_present_in_element(self.locators()['import_status_message'], "Import completed"))
        print("Import successful!")

    def run(self):
        try:
            self.login()
            self.import_csv()
        except Exception as e:
            print("An error occurred during the import process:", e)
        finally:
            self.driver.quit()
