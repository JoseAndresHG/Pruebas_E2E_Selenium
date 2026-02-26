from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from utils.locators import RegistrationLocators, CartLocators
from selenium.common.exceptions import StaleElementReferenceException
from  utils.locators import CartLocators


@step('el usuario agrega el producto al "{variable}"')
def step_impl(context, variable):
    try:
        xpath_value = getattr(CartLocators, variable)
    except AttributeError:
        raise AttributeError(f"No se encontró la variable '{variable}' en CartLocators")

    wait = WebDriverWait(context.driver, 10)

    elemento = wait.until(
        ec.element_to_be_clickable((By.XPATH, xpath_value))
    )
    elemento.click()


@step('el usuario acepta el popup de confirmación')
def step_impl(context):
    wait = WebDriverWait(context.driver, 5)
    alerta = wait.until(ec.alert_is_present())
    alerta.accept()


@step('el usuario visualiza los productos en el "{variable}"')
def step_impl(context, variable):
    try:
        xpath_value = getattr(CartLocators, variable)
    except AttributeError:
        raise AttributeError(f"No se encontró la variable '{variable}' en CartLocators")

    wait = WebDriverWait(context.driver, 10)

    elemento = wait.until(
        ec.element_to_be_clickable((By.XPATH, xpath_value))
    )
    elemento.click()


@step('el usuario diligencia el formulario con los siguientes datos')
def step_impl(context):
    for row in context.table:
        for campo in row.headings:
            valor = row[campo]
            xpath = getattr(CartLocators, campo)

            elemento = WebDriverWait(context.driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, xpath))
            )

            elemento.clear()
            elemento.send_keys(valor)