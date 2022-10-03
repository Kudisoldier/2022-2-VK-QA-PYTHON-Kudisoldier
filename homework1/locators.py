from selenium.webdriver.common.by import By

ACCOUNT_BUTTON = (By.XPATH, "//div[contains(@class, 'right-module-rightButton')]")
LOGOUT_BUTTON = (By.XPATH, "//a[contains(@class, 'rightMenu-module-rightMenuLink') and @href = '/logout']")
LOGIN_FORM_BUTTON = (By.XPATH, "//div[contains(@class, 'responseHead-module-button')]")
LOGIN_INPUT = (By.XPATH, "//input[@name = 'email']")
PASSWORD_INPUT = (By.XPATH, "//input[@name = 'password']")
LOGIN_BUTTON = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")
