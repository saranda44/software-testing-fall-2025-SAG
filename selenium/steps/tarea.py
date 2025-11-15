# -*- coding: utf-8 -*-
"""
Tarea para test busqueda de univeridades
"""
from behave import given, then, when
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver


@given("I am on the Google homepage")  # pylint: disable=not-callable
def step_open_google(context):
    """Opens Google in Chrome."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    context.driver = webdriver.Chrome(options=options)
    context.driver.get("https://www.google.com")


@when('I search for "{query}"')  # pylint: disable=not-callable
def step_search_google(context, query):
    """Searches something in Google."""
    search_box = context.driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    delay = 20  # seconds
    wait = WebDriverWait(context.driver, delay)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#rcnt")))


@when("I click on the first result")  # pylint: disable=not-callable
def step_click_first_result(context):
    """Seleccionar el primer resultado de la busqueda"""
    # Espera el <h3> dentro del enlace
    first_h3 = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a h3"))
    )

    # Buscar el <a> padre del h3
    link_element = first_h3.find_element(By.XPATH, "./ancestor::a")

    # Scroll y clic con JS para evitar overlays
    context.driver.execute_script("arguments[0].scrollIntoView(true);", link_element)
    context.driver.execute_script("arguments[0].click();", link_element)

    # Esperar que cargue la nueva página
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )


@then('I should be on the "{expected_url}"')  # pylint: disable=not-callable
def step_validate_url(context, expected_url):
    """Asegurar que estás en la página correcta"""
    current_url = context.driver.current_url
    assert expected_url in current_url, f"Expected {expected_url}, got {current_url}"


@when('I search for "{term}" in the university page')  # pylint: disable=not-callable
def step_search_in_page(context, term):
    """Buscar termino en la página de la universidad"""
    try:
        # 1. Detectar el ícono según la universidad
        possible_icons = [
            (By.ID, "buscar_front"),  # UDG
            (By.CSS_SELECTOR, ".fa-search"),  # ITESO y Anáhuac
        ]

        search_icon = None
        for locator in possible_icons:
            try:
                search_icon = WebDriverWait(context.driver, 5).until(
                    EC.element_to_be_clickable(locator)
                )
                break
            except (TimeoutException, NoSuchElementException):
                continue

        if not search_icon:
            raise AssertionError("No se encontró el ícono de búsqueda en la página")

        # 2. Hacer clic en el ícono
        context.driver.execute_script("arguments[0].click();", search_icon)

        # 3. Esperar el input (varios selectores posibles)
        possible_inputs = [
            (By.CSS_SELECTOR, "input[type='text']"),  # ITESO y Anahuac
            (By.CSS_SELECTOR, "input.form-search"),  # UDG
        ]

        search_box = None
        for locator in possible_inputs:
            try:
                search_box = WebDriverWait(context.driver, 10).until(
                    EC.presence_of_element_located(locator)
                )
                break
            except (TimeoutException, NoSuchElementException):
                continue

        if not search_box:
            raise AssertionError("No se encontró el input de búsqueda en la página")

        # 4. Escribir el término y presionar Enter
        search_box.send_keys(term)
        search_box.send_keys(Keys.RETURN)

        # 5. Esperar que cargue la página de resultados
        WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

    except Exception as e:
        raise AssertionError(
            f"No se pudo realizar la búsqueda en la página: {e}"
        ) from e


@then('I should see results related to "{term}"')  # pylint: disable=not-callable
def step_validate_results(context, term):
    """Visualizar los resultados relacionados al termino"""
    page_text = context.driver.find_element(By.TAG_NAME, "body").text.lower()
    assert term.lower() in page_text, f"Term '{term}' not found in page"
    context.driver.quit()
