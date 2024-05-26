import time

from page_objects.garage_page import GaragePage, AddCarModel, AddAnExpenses
from page_objects.home_page import HomePage, Registration
from page_objects.account import Profile, DeleteAccount
from page_objects.variables import Variables


def test_login_as_guest_user(driver):
    home_page = HomePage(driver)

    home_page.open()
    home_page.click_user_login_button()
    home_page.click_registration_button()
    time.sleep(3)

    registration = Registration(driver)
    variables = Variables()
    registration.sign_up_name(f"{variables.name}")
    registration.sign_up_last_name(f"{variables.last_name}")
    registration.enter_signup_email(f"{variables.email}")
    registration.enter_signup_password(f"{variables.password}")
    registration.repeat_signup_password(f"{variables.password}")
    registration.click_register_button()
    time.sleep(3)

    profile = Profile(driver)
    profile.go_to_profile()
    time.sleep(3)
    profile.check_name_lastname_are_the_same_as_registration(
        f"{variables.name} {variables.last_name}"
    )
    time.sleep(3)

    garage_page = GaragePage(driver)
    garage_page.go_to_garage()
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

    expenses = AddAnExpenses(driver)
    expenses.click_add_fuel_expense_button()
    time.sleep(3)
    expenses.set_new_car_mileage(f"{variables.new_car_mileage}")
    expenses.set_number_of_liters(f"{variables.number_of_liters}")
    expenses.set_total_cost(f"{variables.total_cost}")
    time.sleep(3)
    expenses.click_add_button()

    delete_account = DeleteAccount(driver)
    delete_account.go_to_settings()
    delete_account.remove_account()
    time.sleep(3)
    delete_account.confirmation_of_removing_account()
    time.sleep(3)
