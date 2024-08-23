from lib.app_utils import wait_for_error
from lib.app_utils import SNInvalid


# FORD
def ford_figo(app, sn):
    # Selectare tab FORD
    app.RadioCodeDatabaseV20.child_window(title="FORD", control_type="TabItem").select()
    # Introducere cod radio
    app.RadioCodeDatabaseV20.child_window(
        title="S/N last 6 digits", auto_id="textBox27", control_type="Edit"
    ).set_edit_text(sn)
    # Calculare pin
    app.RadioCodeDatabaseV20.child_window(
        title="Calculate", auto_id="button18", control_type="Button"
    ).click_input()
    # Verificam daca apare dialogul de eroare
    if err := wait_for_error(app):
        raise SNInvalid(
            f"Eroare la calcularea pinului pentru S/N: {sn} in ford_figo: {err}"
        )
    # Obtinere pin
    r_edit = app.RadioCodeDatabaseV20.child_window(
        auto_id="textBox11", control_type="Edit"
    )
    r_text = r_edit.legacy_properties()["Value"]
    return r_text


def top_power(app, sn):
    # Selectare tab FORD
    app.RadioCodeDatabaseV20.child_window(title="FORD", control_type="TabItem").select()
    # Introducere cod radio
    app.RadioCodeDatabaseV20.child_window(
        title="6 digits", auto_id="textBox26", control_type="Edit"
    ).set_edit_text(sn)
    # Calculare pin
    app.RadioCodeDatabaseV20.child_window(
        title="Calculate", auto_id="button17", control_type="Button"
    ).click_input()
    # Verificam daca apare dialogul de eroare
    if err := wait_for_error(app):
        raise SNInvalid(
            f"Eroare la calcularea pinului pentru S/N: {sn} in top_power: {err}"
        )
    # Obtinere pin
    r_edit = app.RadioCodeDatabaseV20.child_window(
        auto_id="textBox11", control_type="Edit"
    )
    r_text = r_edit.legacy_properties()["Value"]
    return r_text


def ford_sanyo(app, sn):
    # Selectare tab FORD
    app.RadioCodeDatabaseV20.child_window(title="FORD", control_type="TabItem").select()
    # Introducere cod radio
    app.RadioCodeDatabaseV20.child_window(
        title="S/N 12 digits", auto_id="textBox41", control_type="Edit"
    ).set_edit_text(sn)
    # Calculare pin
    app.RadioCodeDatabaseV20.child_window(
        title="Calculate", auto_id="button25", control_type="Button"
    ).click_input()
    # Verificam daca apare dialogul de eroare
    if err := wait_for_error(app):
        raise SNInvalid(
            f"Eroare la calcularea pinului pentru S/N: {sn} in ford_sanyo: {err}"
        )
    # Obtinere pin
    r_edit = app.RadioCodeDatabaseV20.child_window(
        auto_id="textBox11", control_type="Edit"
    )
    r_text = r_edit.legacy_properties()["Value"]
    return r_text


# BLAUPUNKT
def bp_standard(app, sn):
    # Selectare tab BLAUPUNKT
    app.RadioCodeDatabaseV20.child_window(
        title="BLAUPUNKT", control_type="TabItem"
    ).select()
    # Selectare standard radio option
    app.RadioCodeDatabaseV20.child_window(
        title="Standard", auto_id="radioButton14", control_type="RadioButton"
    ).click()
    # Introducere cod radio
    app.RadioCodeDatabaseV20.child_window(
        title="17 characters", auto_id="textBox34", control_type="Edit"
    ).set_edit_text(sn)
    # Calculare pin
    app.RadioCodeDatabaseV20.child_window(
        title="Calculate", auto_id="button21", control_type="Button"
    ).click_input()
    # Verificam daca apare dialogul de eroare
    if err := wait_for_error(app):
        raise SNInvalid(
            f"Eroare la calcularea pinului pentru S/N: {sn} in bp_standard: {err}"
        )
    # Obtinere pin
    b_tab_response = app.RadioCodeDatabaseV20.child_window(
        auto_id="textBox35", control_type="Edit"
    )
    raspuns = b_tab_response.legacy_properties()["Value"]
    return raspuns


def bp_10(app, sn):
    # Selectare tab BLAUPUNKT
    app.RadioCodeDatabaseV20.child_window(
        title="BLAUPUNKT", control_type="TabItem"
    ).select()
    # Selectare 1/0 radio option
    app.RadioCodeDatabaseV20.child_window(
        title="1/0", auto_id="radioButton15", control_type="RadioButton"
    ).click()
    # Introducere cod radio
    app.RadioCodeDatabaseV20.child_window(
        title="17 characters", auto_id="textBox34", control_type="Edit"
    ).set_edit_text(sn)
    # Calculare pin
    app.RadioCodeDatabaseV20.child_window(
        title="Calculate", auto_id="button21", control_type="Button"
    ).click_input()
    # Verificam daca apare dialogul de eroare
    if err := wait_for_error(app):
        raise SNInvalid(
            f"Eroare la calcularea pinului pentru S/N: {sn} in bp_10: {err}"
        )
    # Obtinere pin
    b_tab_response = app.RadioCodeDatabaseV20.child_window(
        auto_id="textBox35", control_type="Edit"
    )
    raspuns = b_tab_response.legacy_properties()["Value"]
    return raspuns


def bp_666(app, sn):
    # Selectare tab BLAUPUNKT
    app.RadioCodeDatabaseV20.child_window(
        title="BLAUPUNKT", control_type="TabItem"
    ).select()
    # Selectare 1111-6666 radio option
    app.RadioCodeDatabaseV20.child_window(
        title="1111-6666", auto_id="radioButton16", control_type="RadioButton"
    ).click()
    # Introducere cod radio
    app.RadioCodeDatabaseV20.child_window(
        title="17 characters", auto_id="textBox34", control_type="Edit"
    ).set_edit_text(sn)
    # Calculare pin
    app.RadioCodeDatabaseV20.child_window(
        title="Calculate", auto_id="button21", control_type="Button"
    ).click_input()
    # Verificam daca apare dialogul de eroare
    if err := wait_for_error(app):
        raise SNInvalid(
            f"Eroare la calcularea pinului pentru S/N: {sn} in bp_666: {err}"
        )
    # Obtinere pin
    b_tab_response = app.RadioCodeDatabaseV20.child_window(
        auto_id="textBox35", control_type="Edit"
    )
    raspuns = b_tab_response.legacy_properties()["Value"]
    return raspuns


def bp_car300(app, sn):
    # Selectare tab BLAUPUNKT
    app.RadioCodeDatabaseV20.child_window(
        title="BLAUPUNKT", control_type="TabItem"
    ).select()
    # Selectare CAR 300 radio option
    app.RadioCodeDatabaseV20.child_window(
        title="CAR 300", auto_id="radioButton17", control_type="RadioButton"
    ).click()
    # Introducere cod radio
    app.RadioCodeDatabaseV20.child_window(
        title="17 characters", auto_id="textBox34", control_type="Edit"
    ).set_edit_text(sn)
    # Calculare pin
    app.RadioCodeDatabaseV20.child_window(
        title="Calculate", auto_id="button21", control_type="Button"
    ).click_input()
    # Verificam daca apare dialogul de eroare
    if err := wait_for_error(app):
        raise SNInvalid(
            f"Eroare la calcularea pinului pentru S/N: {sn} in bp_car300: {err}"
        )
    # Obtinere pin
    b_tab_response = app.RadioCodeDatabaseV20.child_window(
        auto_id="textBox35", control_type="Edit"
    )
    raspuns = b_tab_response.legacy_properties()["Value"]
    return raspuns


def bp_sixdisk(app, sn):
    # Selectare tab BLAUPUNKT
    app.RadioCodeDatabaseV20.child_window(
        title="BLAUPUNKT", control_type="TabItem"
    ).select()
    # Selectam optiunea SIX DISK
    app.RadioCodeDatabaseV20.child_window(
        title="SIX DISK", auto_id="radioButton19", control_type="RadioButton"
    ).click()
    # Introducere cod radio
    app.RadioCodeDatabaseV20.child_window(
        title="17 characters", auto_id="textBox34", control_type="Edit"
    ).set_edit_text(sn)
    # Calculare pin
    app.RadioCodeDatabaseV20.child_window(
        title="Calculate", auto_id="button21", control_type="Button"
    ).click_input()
    # Verificam daca apare dialogul de eroare
    if err := wait_for_error(app):
        raise SNInvalid(
            f"Eroare la calcularea pinului pentru S/N: {sn} in bp_sixdisk: {err}"
        )
    # Obtinere pin
    b_tab_response = app.RadioCodeDatabaseV20.child_window(
        auto_id="textBox35", control_type="Edit"
    )
    raspuns = b_tab_response.legacy_properties()["Value"]
    return raspuns


# CHRYSLER
def chrysler_14_char_qn(app, sn):
    # Selectare tab CHRYSLER
    app.RadioCodeDatabaseV20.child_window(
        title="CHRYSLER", control_type="TabItem"
    ).select()
    # Selectam optiunea 14 cahr
    app.RadioCodeDatabaseV20.child_window(
        title="14 char, QN Continental",
        auto_id="radioButton10",
        control_type="RadioButton",
    ).click()
    # Introducere S/N radio
    app.RadioCodeDatabaseV20.child_window(
        title="S/N Last 4 digits", auto_id="textBox3", control_type="Edit"
    ).set_edit_text(sn)
    # Calculare pin
    app.RadioCodeDatabaseV20.child_window(
        title="Calculate", auto_id="button6", control_type="Button"
    ).click_input()
    # Verificam daca apare dialogul de eroare
    if err := wait_for_error(app):
        raise SNInvalid(
            f"Eroare la calcularea pinului pentru S/N: {sn} in chrysler_14_char_qn: {err}"
        )
    # Obtinere pin
    pin_edit = app.RadioCodeDatabaseV20.child_window(
        auto_id="textBox6", control_type="Edit"
    )
    pin_text = pin_edit.legacy_properties()["Value"]
    return pin_text


# FIAT
def fiat_3_dig(app, sn):
    # selectare tab
    app.RadioCodeDatabaseV20.child_window(title="FIAT", control_type="TabItem").select()
    # Introducere S/N
    app.RadioCodeDatabaseV20.child_window(
        title="E.g. A123", auto_id="textBox17", control_type="Edit"
    ).set_edit_text(sn)
    # Calculare pin
    app.RadioCodeDatabaseV20.child_window(
        title="Calculate", auto_id="button11", control_type="Button"
    ).click_input()
    # Verificam daca apare dialogul de eroare
    if err := wait_for_error(app):
        raise SNInvalid(
            f"Eroare la calcularea pinului pentru S/N: {sn} in fiat_3_dig: {err}"
        )
    # Obtinere pin
    pin_edit = app.RadioCodeDatabaseV20.child_window(
        auto_id="textBox16", control_type="Edit"
    )
    pin_text = pin_edit.legacy_properties()["Value"]
    return pin_text


# ALPINE
def alpine_mf(app, sn):
    # Selectare tab
    app.RadioCodeDatabaseV20.child_window(
        title="ALPINE", control_type="TabItem"
    ).select()
    # Introducere S/N
    sn_edit = app.RadioCodeDatabaseV20.child_window(
        title="4 digits", auto_id="textBox20", control_type="Edit"
    )
    sn_edit.set_edit_text(sn)
    # Calculare pin
    app.RadioCodeDatabaseV20.child_window(
        title="Search", auto_id="button14", control_type="Button"
    ).click_input()
    # Verificam daca apare dialogul de eroare
    if err := wait_for_error(app):
        raise SNInvalid(
            f"Eroare la calcularea pinului pentru S/N: {sn} in alpine_mf: {err}"
        )
    # Obtinere pin
    r_edit = app.RadioCodeDatabaseV20.child_window(
        auto_id="textBox22", control_type="Edit"
    )
    r_text = r_edit.legacy_properties()["Value"]

    # ALPINE BACKUP
    if r_text == "- - - -":
        # selectam ultimile 4 caractere  din S/N
        last_4_digits = sn[-4:]
        # Introducem codu in controlu edit din  grupul ALPINE
        app.RadioCodeDatabaseV20.child_window(
            auto_id="textBox24", control_type="Edit"
        ).set_edit_text(last_4_digits)
        # Calculam pinul
        app.RadioCodeDatabaseV20.child_window(
            title="Calculate", auto_id="button16", control_type="Button"
        ).click_input()
        # Verificam daca apare dialogul de eroare
        if err := wait_for_error(app):
            raise SNInvalid(
                f"Eroare la calcularea pinului pentru S/N: {sn} in alpine_mf: {err}"
            )
        # Obtinere pin
        r_text = r_edit.legacy_properties()["Value"]
    return r_text


# TOYOTA
def toyota_erc(app, sn):
    # Selectare tab
    app.RadioCodeDatabaseV20.child_window(
        title="   ERC   ", control_type="TabItem"
    ).select()
    # Introducere S/N
    app.RadioCodeDatabaseV20.child_window(
        title="10 digits", auto_id="textBox36", control_type="Edit"
    ).set_edit_text(sn)
    # Calculare pin
    app.RadioCodeDatabaseV20.child_window(
        title="Calculate", auto_id="button22", control_type="Button"
    ).click_input()
    # Verificam daca apare dialogul de eroare
    if err := wait_for_error(app):
        raise SNInvalid(
            f"Eroare la calcularea pinului pentru S/N: {sn} in toyota_erc: {err}"
        )
    # Obtinere pin
    r_edit = app.RadioCodeDatabaseV20.child_window(
        auto_id="textBox37", control_type="Edit"
    )
    r_text = r_edit.legacy_properties()["Value"]
    return r_text


# VOLVO
def volvo_truck(app, sn):
    # Selectare tab
    app.RadioCodeDatabaseV20.child_window(
        title="VOLVO", control_type="TabItem"
    ).select()
    # Introducere S/N
    app.RadioCodeDatabaseV20.child_window(
        title="16 characters", auto_id="textBox39", control_type="Edit"
    ).set_edit_text(sn)
    # Calculare pin
    app.RadioCodeDatabaseV20.child_window(
        title="Calculate", auto_id="button24", control_type="Button"
    ).click_input()
    # Verificam daca apare dialogul de eroare
    if err := wait_for_error(app):
        raise SNInvalid(
            f"Eroare la calcularea pinului pentru S/N: {sn} in volvo_truck: {err}"
        )
    # Obtinere pin
    r_edit = app.RadioCodeDatabaseV20.child_window(
        auto_id="textBox40", control_type="Edit"
    )
    r_text = r_edit.legacy_properties()["Value"]
    return r_text
