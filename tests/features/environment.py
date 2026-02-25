import allure
from allure_commons.types import AttachmentType
from utils.browser import select_browser


def before_all(context):
    browser = context.config.userdata.get('browser', 'chrome')
    options = context.config.userdata.get("options", "").split(",")

    try:
        context.driver = select_browser(browser, options)
    except Exception as e:
        print(f"Error al iniciar el navegador {browser}: {e}")
        raise e


def after_all(context):
    if hasattr(context, 'drivers') and context.driver:
        context.driver.quit()


def after_step(context, step):
    # Solo tomamos captura si el paso falló y el driver existe
    if step.status == "failed":
        if hasattr(context, 'driver') and context.driver:
            allure.attach(
                context.driver.get_screenshot_as_png(),
                name=f"Error_{step.name}",
                attachment_type=AttachmentType.PNG
            )
