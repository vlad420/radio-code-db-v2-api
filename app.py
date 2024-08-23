from flask import Flask
from lib.app_utils import get_app, wait_app_ready, SNInvalid
from lib.automatizari import (
    ford_figo,
    top_power,
    ford_sanyo,
    bp_standard,
    bp_10,
    bp_666,
    bp_car300,
    bp_sixdisk,
    chrysler_14_char_qn,
    fiat_3_dig,
    alpine_mf,
    toyota_erc,
    volvo_truck,
)
import logging
from lib.constants import WAIT_TIMEOUT_APP_READY

app = Flask(__name__)


# Endpoint-uri
# FORD
@app.get("/ford_figo/<string:sn>")
def get_pin_ford_figo(sn):
    logging.info(f"Se cauta PIN-ul pentru SN: {sn}")
    try:
        app = get_app()
        wait_app_ready(app=app, timeout=WAIT_TIMEOUT_APP_READY)
        pin = ford_figo(app, sn)
        logging.info(f"PIN-ul pentru SN: {sn} este {pin}")
        return {"success": True, "code": pin}
    except SNInvalid as e:
        logging.error(f"SN-ul {sn} este invalid")
        return {"success": False, "error": str(e)}
    except Exception as e:
        logging.error(f"A aparut o eroare: {e}")
        return {"success": False, "error": str(e)}, 500


@app.get("/top_power/<string:sn>")
def get_pin_top_power(sn):
    logging.info(f"Se cauta PIN-ul pentru SN: {sn}")
    try:
        app = get_app()
        wait_app_ready(app=app, timeout=WAIT_TIMEOUT_APP_READY)
        pin = top_power(app, sn)
        logging.info(f"PIN-ul pentru SN: {sn} este {pin}")
        return {"success": True, "code": pin}
    except SNInvalid as e:
        logging.error(f"SN-ul {sn} este invalid")
        return {"success": False, "error": str(e)}
    except Exception as e:
        logging.error(f"A aparut o eroare: {e}")
        return {"success": False, "error": str(e)}, 500


@app.get("/ford_sanyo/<string:sn>")
def get_pin_ford_sanyo(sn):
    logging.info(f"Se cauta PIN-ul pentru SN: {sn}")
    try:
        app = get_app()
        wait_app_ready(app=app, timeout=WAIT_TIMEOUT_APP_READY)
        pin = ford_sanyo(app, sn)
        logging.info(f"PIN-ul pentru SN: {sn} este {pin}")
        return {"success": True, "code": pin}
    except SNInvalid as e:
        logging.error(f"SN-ul {sn} este invalid")
        return {"success": False, "error": str(e)}
    except Exception as e:
        logging.error(f"A aparut o eroare: {e}")
        return {"success": False, "error": str(e)}, 500


# BLAUPUNKT
@app.get("/bp_standard/<string:sn>")
def get_pin_bp_standard(sn):
    logging.info(f"Se cauta PIN-ul pentru SN: {sn}")
    try:
        app = get_app()
        wait_app_ready(app=app, timeout=WAIT_TIMEOUT_APP_READY)
        pin = bp_standard(app, sn)
        logging.info(f"PIN-ul pentru SN: {sn} este {pin}")
        return {"success": True, "code": pin}
    except SNInvalid as e:
        logging.error(f"SN-ul {sn} este invalid")
        return {"success": False, "error": str(e)}
    except Exception as e:
        logging.error(f"A aparut o eroare: {e}")
        return {"success": False, "error": str(e)}, 500


@app.get("/bp_10/<string:sn>")
def get_pin_bp_10(sn):
    logging.info(f"Se cauta PIN-ul pentru SN: {sn}")
    try:
        app = get_app()
        wait_app_ready(app=app, timeout=WAIT_TIMEOUT_APP_READY)
        pin = bp_10(app, sn)
        logging.info(f"PIN-ul pentru SN: {sn} este {pin}")
        return {"success": True, "code": pin}
    except SNInvalid as e:
        logging.error(f"SN-ul {sn} este invalid")
        return {"success": False, "error": str(e)}
    except Exception as e:
        logging.error(f"A aparut o eroare: {e}")
        return {"success": False, "error": str(e)}, 500


@app.get("/bp_666/<string:sn>")
def get_pin_bp_666(sn):
    logging.info(f"Se cauta PIN-ul pentru SN: {sn}")
    try:
        app = get_app()
        wait_app_ready(app=app, timeout=WAIT_TIMEOUT_APP_READY)
        pin = bp_666(app, sn)
        logging.info(f"PIN-ul pentru SN: {sn} este {pin}")
        return {"success": True, "code": pin}
    except SNInvalid as e:
        logging.error(f"SN-ul {sn} este invalid")
        return {"success": False, "error": str(e)}
    except Exception as e:
        logging.error(f"A aparut o eroare: {e}")
        return {"success": False, "error": str(e)}, 500


@app.get("/bp_car300/<string:sn>")
def get_pin_bp_car300(sn):
    logging.info(f"Se cauta PIN-ul pentru SN: {sn}")
    try:
        app = get_app()
        wait_app_ready(app=app, timeout=WAIT_TIMEOUT_APP_READY)
        pin = bp_car300(app, sn)
        logging.info(f"PIN-ul pentru SN: {sn} este {pin}")
        return {"success": True, "code": pin}
    except SNInvalid as e:
        logging.error(f"SN-ul {sn} este invalid")
        return {"success": False, "error": str(e)}
    except Exception as e:
        logging.error(f"A aparut o eroare: {e}")
        return {"success": False, "error": str(e)}, 500


@app.get("/bp_sixdisk/<string:sn>")
def get_pin_bp_sixdisk(sn):
    logging.info(f"Se cauta PIN-ul pentru SN: {sn}")
    try:
        app = get_app()
        wait_app_ready(app=app, timeout=WAIT_TIMEOUT_APP_READY)
        pin = bp_sixdisk(app, sn)
        logging.info(f"PIN-ul pentru SN: {sn} este {pin}")
        return {"success": True, "code": pin}
    except SNInvalid as e:
        logging.error(f"SN-ul {sn} este invalid")
        return {"success": False, "error": str(e)}
    except Exception as e:
        logging.error(f"A aparut o eroare: {e}")
        return {"success": False, "error": str(e)}, 500


# CHRYSLER
@app.get("/chrysler_14_char_qn/<string:sn>")
def get_pin_chrysler_14_char_qn(sn):
    logging.info(f"Se cauta PIN-ul pentru SN: {sn}")
    try:
        app = get_app()
        wait_app_ready(app=app, timeout=WAIT_TIMEOUT_APP_READY)
        pin = chrysler_14_char_qn(app, sn)
        logging.info(f"PIN-ul pentru SN: {sn} este {pin}")
        return {"success": True, "code": pin}
    except SNInvalid as e:
        logging.error(f"SN-ul {sn} este invalid")
        return {"success": False, "error": str(e)}
    except Exception as e:
        logging.error(f"A aparut o eroare: {e}")
        return {"success": False, "error": str(e)}, 500


# FIAT
@app.get("/fiat_3_dig/<string:sn>")
def get_pin_fiat_3_dig(sn):
    logging.info(f"Se cauta PIN-ul pentru SN: {sn}")
    try:
        app = get_app()
        wait_app_ready(app=app, timeout=WAIT_TIMEOUT_APP_READY)
        pin = fiat_3_dig(app, sn)
        logging.info(f"PIN-ul pentru SN: {sn} este {pin}")
        return {"success": True, "code": pin}
    except SNInvalid as e:
        logging.error(f"SN-ul {sn} este invalid")
        return {"success": False, "error": str(e)}
    except Exception as e:
        logging.error(f"A aparut o eroare: {e}")
        return {"success": False, "error": str(e)}, 500


# ALPINE
@app.get("/alpine_mf/<string:sn>")
def get_pin_alpine_mf(sn):
    logging.info(f"Se cauta PIN-ul pentru SN: {sn}")
    try:
        app = get_app()
        wait_app_ready(app=app, timeout=WAIT_TIMEOUT_APP_READY)
        pin = alpine_mf(app, sn)
        logging.info(f"PIN-ul pentru SN: {sn} este {pin}")
        return {"success": True, "code": pin}
    except SNInvalid as e:
        logging.error(f"SN-ul {sn} este invalid")
        return {"success": False, "error": str(e)}
    except Exception as e:
        logging.error(f"A aparut o eroare: {e}")
        return {"success": False, "error": str(e)}, 500


# TOYOTA
@app.get("/toyota_erc/<string:sn>")
def get_pin_toyota_erc(sn):
    logging.info(f"Se cauta PIN-ul pentru SN: {sn}")
    try:
        app = get_app()
        wait_app_ready(app=app, timeout=WAIT_TIMEOUT_APP_READY)
        pin = toyota_erc(app, sn)
        logging.info(f"PIN-ul pentru SN: {sn} este {pin}")
        return {"success": True, "code": pin}
    except SNInvalid as e:
        logging.error(f"SN-ul {sn} este invalid")
        return {"success": False, "error": str(e)}
    except Exception as e:
        logging.error(f"A aparut o eroare: {e}")
        return {"success": False, "error": str(e)}, 500


# VOLVO
@app.get("/volvo_truck/<string:sn>")
def get_pin_volvo_truck(sn):
    logging.info(f"Se cauta PIN-ul pentru SN: {sn}")
    try:
        app = get_app()
        wait_app_ready(app=app, timeout=WAIT_TIMEOUT_APP_READY)
        pin = volvo_truck(app, sn)
        logging.info(f"PIN-ul pentru SN: {sn} este {pin}")
        return {"success": True, "code": pin}
    except SNInvalid as e:
        logging.error(f"SN-ul {sn} este invalid")
        return {"success": False, "error": str(e)}
    except Exception as e:
        logging.error(f"A aparut o eroare: {e}")
        return {"success": False, "error": str(e)}, 500


if __name__ == "__main__":
    app.run(debug=True)
