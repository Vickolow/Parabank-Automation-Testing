from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

class HomePage(BasePage):
    def go_to_register_page(self):
        register_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_link.click()

class RegisterPage(BasePage):
    def register_new_user(self, first_name, last_name, address, city, state, zip_code, phone, ssn, username, password):
        self.driver.find_element(By.ID, "customer.firstName").send_keys(first_name)
        self.driver.find_element(By.ID, "customer.lastName").send_keys(last_name)
        self.driver.find_element(By.ID, "customer.address.street").send_keys(address)
        self.driver.find_element(By.ID, "customer.address.city").send_keys(city)
        self.driver.find_element(By.ID, "customer.address.state").send_keys(state)
        self.driver.find_element(By.ID, "customer.address.zipCode").send_keys(zip_code)
        self.driver.find_element(By.ID, "customer.phoneNumber").send_keys(phone)
        self.driver.find_element(By.ID, "customer.ssn").send_keys(ssn)
        self.driver.find_element(By.ID, "customer.username").send_keys(username)
        self.driver.find_element(By.ID, "customer.password").send_keys(password)
        self.driver.find_element(By.ID, "repeatedPassword").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@value='Register']").click()

class LoginPage(BasePage):
    def login(self, username, password):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@value='Log In']").click()

class AccountPage(BasePage):
    def open_new_account(self):
        self.driver.find_element(By.LINK_TEXT, "Open New Account").click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "type"))).click()
        self.driver.find_element(By.XPATH, "//option[@value='1']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Open New Account']").click()

    def transfer_funds(self, amount, from_account, to_account):
        self.driver.find_element(By.LINK_TEXT, "Transfer Funds").click()
        self.driver.find_element(By.ID, "amount").send_keys(amount)
        self.driver.find_element(By.ID, "fromAccountId").send_keys(from_account)
        self.driver.find_element(By.ID, "toAccountId").send_keys(to_account)
        self.driver.find_element(By.XPATH, "//input[@value='Transfer']").click()

    def request_loan(self, amount, down_payment, from_account):
        self.driver.find_element(By.LINK_TEXT, "Request Loan").click()
        self.driver.find_element(By.ID, "amount").send_keys(amount)
        self.driver.find_element(By.ID, "downPayment").send_keys(down_payment)
        self.driver.find_element(By.ID, "fromAccountId").send_keys(from_account)
        self.driver.find_element(By.XPATH, "//input[@value='Apply Now']").click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Log Out").click()

# Main script
def main():
    driver = webdriver.Chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    driver.maximize_window()

    try:
        # Home Page
        home_page = HomePage(driver)
        home_page.go_to_register_page()

        # Register Page
        register_page = RegisterPage(driver)
        register_page.register_new_user(
            first_name="John",
            last_name="Doe",
            address="123 Elm Street",
            city="Springfield",
            state="IL",
            zip_code="62704",
            phone="5551234567",
            ssn="123-45-6789",
            username="johndoe",
            password="password123"
        )

        # Login Page
        login_page = LoginPage(driver)
        login_page.login(username="johndoe", password="password123")

        # Account Page
        account_page = AccountPage(driver)
        account_page.open_new_account()
        account_page.transfer_funds(amount="500", from_account="12345", to_account="67890")
        account_page.request_loan(amount="1000", down_payment="200", from_account="12345")
        account_page.logout()
    #Quit the browser
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
