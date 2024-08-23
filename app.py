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

endpoints_map = {
    "ford_figo": ford_figo,
    "top_power": top_power,
    "ford_sanyo": ford_sanyo,
    "bp_standard": bp_standard,
    "bp_10": bp_10,
    "bp_666": bp_666,
    "bp_car300": bp_car300,
    "bp_sixdisk": bp_sixdisk,
    "chrysler_14_char_qn": chrysler_14_char_qn,
    "fiat_3_dig": fiat_3_dig,
    "alpine_mf": alpine_mf,
    "toyota_erc": toyota_erc,
    "volvo_truck": volvo_truck,
}

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


# Endpoint centralizat pentru toate endpoint-urile
@app.get("/<string:endpoint>/<string:sn>")
def get_pin(endpoint, sn):
    if endpoint in endpoints_map:
        logging.info(f"Se cauta PIN-ul pentru SN: {sn} endpoint: {endpoint}")
        try:
            app = get_app()
            logging.info(f"Se asteapta aplicatia sa fie pregatita")
            wait_app_ready(app=app, timeout=WAIT_TIMEOUT_APP_READY)
            logging.info(f"Aplicatia este pregatita")
            pin = endpoints_map[endpoint](app, sn)
            logging.info(f"PIN-ul pentru SN: {sn} este {pin}")
            return {"success": True, "code": pin}
        except SNInvalid as e:
            logging.error(f"SN-ul {sn} este invalid")
            return {"success": False, "error": str(e)}
        except Exception as e:
            logging.error(f"A aparut o eroare: {e}")
            return {"success": False, "error": str(e)}, 500
    else:
        logging.error(f"Endpointul {endpoint} nu exista")
        return {"success": False, "error": "Endpointul nu exista"}, 404


if __name__ == "__main__":
    app.run(debug=True)
