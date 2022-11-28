import pandas as pd
import pytest


@pytest.fixture
def santander_dummy_df():
    path = "src/tests/fixtures/dataframes/santander_test_sample.csv"
    santander_df = pd.read_csv(path)
    return santander_df


@pytest.fixture
def santander_small_dummy_df():
    santander_dict = {
        "fecha_dato": {
            "0": "2015-01-28",
            "1": "2015-01-28",
            "2": "2015-01-28",
            "3": "2015-01-28",
            "4": "2015-01-28",
        },
        "ncodpers": {
            "0": 1375586,
            "1": 1050611,
            "2": 1050612,
            "3": 1050613,
            "4": 1050614,
        },
        "ind_empleado": {"0": "N", "1": "N", "2": "N", "3": "N", "4": "N"},
        "pais_residencia": {"0": "ES", "1": "ES", "2": "ES", "3": "ES", "4": "ES"},
        "sexo": {"0": "H", "1": "V", "2": "V", "3": "H", "4": "V"},
        "age": {"0": " 35", "1": " 20", "2": " 23", "3": " 22", "4": " 29"},
        "fecha_alta": {
            "0": "2015-01-12",
            "1": "2012-08-10",
            "2": "2012-08-10",
            "3": "2012-08-10",
            "4": "2012-08-10",
        },
        "ind_nuevo": {"0": " 0", "1": " 0", "2": " 0", "3": " 0", "4": " 0"},
        "antiguedad": {
            "0": "      6",
            "1": "     35",
            "2": "     35",
            "3": "     35",
            "4": "     35",
        },
        "indrel": {"0": 1, "1": 1, "2": 1, "3": 1, "4": 1},
        "ult_fec_cli_1t": {"0": None, "1": None, "2": None, "3": None, "4": None},
        "indrel_1mes": {"0": 1.0, "1": 1.0, "2": 1.0, "3": 1.0, "4": 1.0},
        "tiprel_1mes": {"0": "A", "1": "I", "2": "I", "3": "I", "4": "A"},
        "indresi": {"0": "S", "1": "S", "2": "S", "3": "S", "4": "S"},
        "indext": {"0": "N", "1": "S", "2": "N", "3": "N", "4": "N"},
        "conyuemp": {"0": None, "1": None, "2": None, "3": None, "4": None},
        "canal_entrada": {"0": "KHL", "1": "KHE", "2": "KHE", "3": "KHD", "4": "KHE"},
        "indfall": {"0": "N", "1": "N", "2": "N", "3": "N", "4": "N"},
        "tipodom": {"0": 1, "1": 1, "2": 1, "3": 1, "4": 1},
        "cod_prov": {"0": 29.0, "1": 13.0, "2": 13.0, "3": 50.0, "4": 50.0},
        "nomprov": {
            "0": "MALAGA",
            "1": "CIUDAD REAL",
            "2": "CIUDAD REAL",
            "3": "ZARAGOZA",
            "4": "ZARAGOZA",
        },
        "ind_actividad_cliente": {"0": 1, "1": 0, "2": 0, "3": 0, "4": 1},
        "renta": {
            "0": 87218.1015625,
            "1": 35548.73828125,
            "2": 122179.109375,
            "3": 119775.5390625,
            "4": None,
        },
        "segmento": {
            "0": "02 - PARTICULARES",
            "1": "03 - UNIVERSITARIO",
            "2": "03 - UNIVERSITARIO",
            "3": "03 - UNIVERSITARIO",
            "4": "03 - UNIVERSITARIO",
        },
        "ind_ahor_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_aval_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_cco_fin_ult1": {"0": 1, "1": 1, "2": 1, "3": 0, "4": 1},
        "ind_cder_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_cno_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_ctju_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_ctma_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_ctop_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_ctpp_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_deco_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 1, "4": 0},
        "ind_deme_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_dela_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_ecue_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_fond_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_hip_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_plan_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_pres_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_reca_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_tjcr_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_valo_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_viv_fin_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_nomina_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_nom_pens_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
        "ind_recibo_ult1": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0},
    }
    santander_df = pd.DataFrame(santander_dict)
    return santander_df
