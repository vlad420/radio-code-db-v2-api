from pywinauto.application import Application
from pywinauto.timings import TimeoutError
import logging
from lib.constants import WAIT_TIMEOUT_DIALOG_EROARE
from lib.utils import gaseste_pid_radiocodedb


class SNInvalid(Exception):
    pass


def get_app():
    logging.info("Se cauta apicatia RadioCodeDatabase v2.0...")
    if pid := gaseste_pid_radiocodedb():
        logging.info(f"Aplicatia a fost gasita. PID: {pid}")
        return Application(backend="uia").connect(process=pid)
    else:
        logging.info("Aplicatia nu a fost gasita, se porneste...")
        return Application(backend="uia").start(
            r"C:\Users\galu\Desktop\RadioCodeDatabase v2.0"
        )


def wait_app_ready(app, timeout):
    logging.info(
        f"Se asteapta aplicatia sa fie gata cu timeout-ul de {timeout} secunde"
    )
    try:
        window = app.window(title="RadioCodeDatabase v2.0")
        window.wait("ready", timeout=timeout)
        return True
    except TimeoutError:
        return False


def wait_for_error(app, timeout=WAIT_TIMEOUT_DIALOG_EROARE):
    try:
        dialog_eroare = app.RadioCodeDatabaseV20.child_window(
            control_type="Window"
        ).wait("visible", timeout=timeout)
        # Obținem textul mesajului de eroare
        mesaj_eroare = dialog_eroare.descendants(control_type="Text")[0].window_text()
        # Găsim și apăsăm butonul OK
        buton_ok = dialog_eroare.descendants(title="OK", control_type="Button")[0]
        buton_ok.click_input()

        return mesaj_eroare

    except TimeoutError:
        return False
