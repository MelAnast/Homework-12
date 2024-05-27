import time

from selenium.webdriver.common.by import By

from conftest import driver
from page_objects.garage_page import GaragePage, AddCarModel, AddAnExpenses
from page_objects.home_page import HomePage, Registration
from page_objects.account import Profile, DeleteAccount, SignInAsUser
from page_objects.variables import Variables

variables = Variables()


def test_registration_as_user_success(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.click_user_login_button()
    home_page.click_registration_button()
    time.sleep(3)
    registration = Registration(driver)
    registration.sign_up_name(f"{variables.name}")
    registration.sign_up_last_name(f"{variables.last_name}")
    registration.enter_signup_email(f"{variables.email}")
    registration.enter_signup_password(f"{variables.password}")
    registration.repeat_signup_password(f"{variables.password}")
    registration.click_register_button()
    time.sleep(3)
    element = driver.find_element(By.TAG_NAME, "h1")
    assert element.text == "Garage"


def test_same_registration_profile_names(driver):
    home_page = HomePage(driver)
    home_page.open()
    sign_in = SignInAsUser(driver)
    sign_in.click_sign_in_button()
    sign_in.enter_signin_email(f"{variables.email}")
    sign_in.enter_signin_password(f"{variables.password}")
    sign_in.click_login_button()
    profile = Profile(driver)
    time.sleep(3)
    profile.go_to_profile()
    time.sleep(3)
    compare_registration_name = driver.find_element(By.XPATH,
                                                    "/html/body/app-root/app-global-layout/div/div/div/app-panel"
                                                    "-layout/div/div/div/div[2]/div/app-profile/div/div[2]/div/p")
    assert compare_registration_name.text == variables.registration_name


def test_created_car_correct(driver):
    home_page = HomePage(driver)
    home_page.open()
    sign_in = SignInAsUser(driver)
    sign_in.click_sign_in_button()
    sign_in.enter_signin_email(f"{variables.email}")
    sign_in.enter_signin_password(f"{variables.password}")
    sign_in.click_login_button()
    garage_page = GaragePage(driver)
    time.sleep(3)
    garage_page.click_add_car_button()
    add_car_model = AddCarModel(driver)
    time.sleep(3)
    add_car_model.select_car_brand(f"{variables.car_brand_name}")
    time.sleep(3)
    add_car_model.select_car_model(f"{variables.car_model_name}")
    time.sleep(3)
    add_car_model.set_car_mileage(variables.car_mileage)
    add_car_model.click_add_button()
    time.sleep(3)
    compare_added_car = driver.find_element(By.XPATH,
                                            "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div"
                                            "/div/div/div[2]/div/app-garage/div/div[2]/div/ul/li/app-car/div/div["
                                            "1]/div[1]/div[2]/p")
    assert compare_added_car.text == variables.added_car


def test_new_expenses_added(driver):
    home_page = HomePage(driver)
    home_page.open()
    sign_in = SignInAsUser(driver)
    sign_in.click_sign_in_button()
    sign_in.enter_signin_email(f"{variables.email}")
    sign_in.enter_signin_password(f"{variables.password}")
    sign_in.click_login_button()
    garage_page = GaragePage(driver)
    time.sleep(3)
    expenses = AddAnExpenses(driver)
    expenses.click_add_fuel_expense_button()
    time.sleep(3)
    expenses.set_new_car_mileage(f"{variables.new_car_mileage}")
    expenses.set_number_of_liters(f"{variables.number_of_liters}")
    expenses.set_total_cost(f"{variables.total_cost}")
    time.sleep(3)
    expenses.click_add_button()
    compare_new_mileage = driver.find_element(By.XPATH,
                                              "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div"
                                              "/div/div/div[2]/div/app-garage/div/div[2]/div/ul/li["
                                              "1]/app-car/div/div[2]/app-update-mileage-form/form/input")
    assert compare_new_mileage.text != variables.car_mileage


def test_deleting_account(driver):
    home_page = HomePage(driver)
    home_page.open()
    sign_in = SignInAsUser(driver)
    sign_in.click_sign_in_button()
    sign_in.enter_signin_email(f"{variables.email}")
    sign_in.enter_signin_password(f"{variables.password}")
    sign_in.click_login_button()
    time.sleep(3)
    delete_account = DeleteAccount(driver)
    delete_account.go_to_settings()
    delete_account.remove_account()
    time.sleep(3)
    delete_account.confirmation_of_removing_account()
    time.sleep(3)
    error_message = driver.find_element(By.PARTIAL_LINK_TEXT, "/div/app-alert/div/div/p")
    assert error_message.text == "User account has been removed"

