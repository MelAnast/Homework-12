from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class HomePage(BasePage):

    def open(self):
        self._driver.get("https://guest:welcome2qauto@qauto.forstudy.space/")

    def click_user_login_button(self):
        self._driver.find_element(
            By.XPATH, "//button[@class='btn btn-outline-white header_signin']"
        ).click()

    def click_registration_button(self):
        self._driver.find_element(
            By.XPATH,
            "/html/body/ngb-modal-window/div/div/app-signin-modal/div[3]/button[1]",
        ).click()


class Registration(BasePage):

    def sign_up_name(self, name: str):
        self._driver.find_element(By.XPATH, "//input[@id='signupName']").send_keys(name)

    def sign_up_last_name(self, last_name: str):
        self._driver.find_element(By.XPATH, "//input[@id='signupLastName']").send_keys(
            last_name
        )

    def enter_signup_email(self, email: str):
        self._driver.find_element(By.XPATH, "//input[@id='signupEmail']").send_keys(
            email
        )

    def enter_signup_password(self, password: str):
        self._driver.find_element(By.XPATH, "//input[@id='signupPassword']").send_keys(
            password
        )

    def repeat_signup_password(self, password: str):
        self._driver.find_element(
            By.XPATH, "//input[@id='signupRepeatPassword']"
        ).send_keys(password)

    def click_register_button(self):
        self._driver.find_element(
            By.XPATH, "//div[@class='modal-footer']//button[@class='btn btn-primary']"
        ).click()


