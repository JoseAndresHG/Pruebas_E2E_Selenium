from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from utils.locators import RegistrationLocators


@step("el usuario navega a la página pagina {url}")
def step_impl(context, url):
    context.driver.get(url)


@step('el usuario selecciona "{nombre_boton}"')
def step_impl(context, nombre_boton):
    wait = WebDriverWait(context.driver, 10)
    elementos = {
        "INICIAR_SESION": "//a[contains(.,'Log in')]",
        "BOTON_LOGIN" : "//button[@onclick='logIn()']",
        "HOME_CATALOGO": "//a[contains(.,'Home (current)')]",
        "PRODUCTO1": "//a[contains(.,'Nexus 6')]",
        "PRODUCTO2": "//a[contains(.,'Samsung galaxy s6')]",
        "REALIZAR_PEDIDO": "//button[contains(.,'Place Order')]",
        "COMPRAR" : "//button[contains(.,'Purchase')]"

    }
    xpath = elementos.get(nombre_boton)

    if not xpath:
        raise ValueError(f"El botón '{nombre_boton}' no está definido en el diccionario.")

    boton = WebDriverWait(context.driver, 20).until(
        ec.element_to_be_clickable((By.XPATH, xpath))
    )
    boton.click()


@step('el usuario ingresa "{texto}" en el campo "{nombre_variable}"')
def step_impl(context, texto, nombre_variable):
    xpath = getattr(RegistrationLocators, nombre_variable)

    elemento = WebDriverWait(context.driver, 5).until(
        ec.element_to_be_clickable((By.XPATH, xpath))
    )
    elemento.clear()
    elemento.send_keys(texto)


@then('el usuario debería ver su nombre de usuario en el menú')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//a[contains(.,'Welcome JoseH')]")))
