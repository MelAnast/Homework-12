from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class GaragePage(BasePage):

    def go_to_garage(self):
        self._driver.find_element(
            By.XPATH,
            "//body/app-root/app-global-layout/div["
            "@class='global-layout']//app-panel-layout//nav/a[@href='/panel/garage']",
        ).click()

    def click_add_car_button(self):
        self._driver.find_element(
            By.XPATH, "//button[@class='btn btn-primary']"
        ).click()


class AddCarModel(BasePage):

    def select_car_brand(self, car_brand_name: str):
        self._driver.find_element(By.XPATH, "//select[@id='addCarBrand']").send_keys(
            car_brand_name
        )

    def select_car_model(self, car_model_name: str):
        self._driver.find_element(By.XPATH, "//select[@id='addCarModel']").send_keys(
            car_model_name
        )

    def set_car_mileage(self, car_mileage: int):
        self._driver.find_element(By.XPATH, "//input[@id='addCarMileage']").send_keys(
            car_mileage
        )

    def click_add_button(self):
        self._driver.find_element(
            By.XPATH, "//div[@class ='modal-content']//button[@class='btn btn-primary']"
        ).click()


class AddAnExpenses(BasePage):

    def click_add_fuel_expense_button(self):
        self._driver.find_element(
            By.XPATH,
            "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[2]/div/ul/li/app-car/div/div[1]/div[2]/button[2]").click()

    def set_new_car_mileage(self, new_car_mileage):
        self._driver.find_element(
            By.XPATH, "//input[@id='addExpenseMileage']"
        ).send_keys(new_car_mileage)

    def set_number_of_liters(self, number_of_liters):
        self._driver.find_element(
            By.XPATH, "//input[@id='addExpenseLiters']"
        ).send_keys(number_of_liters)

    def set_total_cost(self, total_cost):
        self._driver.find_element(
            By.XPATH, "//input[@id='addExpenseTotalCost']"
        ).send_keys(total_cost)

    def click_add_button(self):
        self._driver.find_element(
            By.XPATH,
            "/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[3]/button[2]",
        ).click()
