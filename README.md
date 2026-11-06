# Automatización de pruebas de la aplicación web URBAN ROUTES

## Descripción del proyecto

Este proyecto automatiza, con **Selenium WebDriver** y **Pytest**, el proceso completo de pedir un taxi en la aplicación web **Urban Routes**. Cada paso del flujo se valida con una prueba independiente, de modo que un fallo en una funcionalidad no oculte el estado de las demás.


| # | Prueba | Qué se valida |
|---|---|---|
| 1 | `test_1_set_route` | Las direcciones "Desde" y "Hasta" quedan configuradas |
| 2 | `test_2_select_comfort_tariff` | La tarifa activa es "Comfort" |
| 3 | `test_3_fill_phone_number` | El número de teléfono queda registrado tras confirmar el código SMS |
| 4 | `test_4_add_credit_card` | La tarjeta queda agregada como método de pago |
| 5 | `test_5_write_message_for_driver` | El mensaje para el conductor queda escrito |
| 6 | `test_6_order_blanket_and_tissues` | La opción "Manta y pañuelos" queda activada |
| 7 | `test_7_order_two_ice_creams` | El contador de helados marca exactamente 2 |
| 8 | `test_8_search_taxi_modal_appears` | Aparece el modal de búsqueda de taxi |
| 9 | `test_9_driver_info_appears` | El modal muestra la información del conductor tras la cuenta regresiva |

Cada prueba prepara sus propias precondiciones, no depende de otra y puede ejecutarse por separado.

## Estructura del proyecto

```
urban_routes/
├── data.py        # URL de la aplicación y datos de prueba
├── helpers.py     # retrieve_phone_code(): obtiene el código de confirmación del teléfono
├── page.py        # Clase UrbanRoutesPage (Page Object): localizadores y métodos
├── test_main.py   # Clase TestUrbanRoutes: las 9 pruebas
└── README.md
```

| Archivo | Contenido |
|---|---|
| `data.py` | URL de Urban Routes, direcciones, teléfono, datos de la tarjeta y mensaje para el conductor. |
| `helpers.py` | Función `retrieve_phone_code(driver)`, que lee los registros de rendimiento del navegador y devuelve el código SMS como texto. Es código de apoyo proporcionado y no se modifica. |
| `page.py` | `UrbanRoutesPage`, con todos los localizadores y las acciones sobre la página. |
| `test_main.py` | `TestUrbanRoutes`, con `setup_method()`, `teardown_method()` y las nueve pruebas. |

## Tecnologías y técnicas utilizadas

**Tecnologías**
- **Python 3**
- **Selenium WebDriver** con Google Chrome, para interactuar con la interfaz
- **Pytest**, como framework de ejecución de pruebas y aserciones
- **PyCharm**, como entorno de desarrollo

**Técnicas**
- **Page Object Model (POM)**: los localizadores y las acciones sobre la página viven en `page.py`; las pruebas solo describen precondiciones, acciones y aserciones.
- **Localizadores variados**: `By.ID`, `By.CLASS_NAME`, `By.XPATH` y `By.CSS_SELECTOR`.
- **Esperas explícitas**: `WebDriverWait` con `visibility_of_element_located` y `element_to_be_clickable`, sin `time.sleep()`.
- **Aislamiento de pruebas**: `setup_method()` abre un navegador nuevo antes de cada prueba y `teardown_method()` lo cierra con `driver.quit()`. No se comparte sesión entre pruebas.
- **Registros de rendimiento de Chrome**: el driver se crea con `options.set_capability("goog:loggingPrefs", {"performance": "ALL"})`, lo que permite a `retrieve_phone_code()` leer el código de confirmación.
- **Aserciones significativas**: cada prueba valida su resultado esperado con un `assert` sobre un valor concreto de la interfaz.
- **Reutilización de precondiciones**: métodos auxiliares como `route_and_comfort()` y `ready_to_order()` evitan duplicar pasos sin crear dependencias entre pruebas.
- **Datos separados del código**: la URL, el teléfono y demás datos viven en `data.py`, no dentro de las pruebas.

## Requisitos previos

- Python 3 instalado
- Google Chrome instalado
- PyCharm

## Cómo ejecutar las pruebas

1. **Clonar el repositorio del proyecto en la computadora**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   (este fue el usado por mi: git clone git@github.com:larissharell-netizen/qa-project-Urban-Routes-es.git)
   ```
2. Abrir el proyecto en **PyCharm**: `Archivo → Abrir` y selecciona la carpeta `qa-project-Urban-Routes-es`.
3. Instalar las dependencias del proyecto (`pytest`, `requests`).
4. Verificar que el archivo `data.py` tenga la URL correcta del entorno de pruebas.
5. Ejecutar toda la suite de pruebas consignada en el archivo de pruebas test_main.py.
6. Cada ejecución abre y cierra su propio navegador. 


## Resultado esperado de la ejecución

Al finalizar la ejecución, las 9 pruebas deben pasar (`passed`), confirmando que cada prueba valide lo ya especificado para cada una.