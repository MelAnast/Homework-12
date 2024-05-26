from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class Profile(BasePage):

    def go_to_profile(self):
        self._driver.find_element(
            By.XPATH,
            "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div"
            "/div[1]/nav/div/a[1]",
        ).click()

    def check_name_lastname_are_the_same_as_registration(self, expected_name_last_name):
        registration_name = self._driver.find_element(
            By.XPATH, "//p[@class='profile_name display-4']"
        ).text
        assert expected_name_last_name == registration_name


class DeleteAccount(BasePage):

    def go_to_settings(self):
        self._driver.find_element(
            By.XPATH,
            "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div"
            "/div[1]/nav/div/a[2]",
        ).click()

    def remove_account(self):
        self._driver.find_element(
            By.XPATH, "//button[@class='btn btn-danger-bg']"
        ).click()

    def confirmation_of_removing_account(self):
        self._driver.find_element(By.XPATH, "//button[@class='btn btn-danger']").click()
