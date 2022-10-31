import pandas as pd
import pytest


@pytest.fixture
def transactions_dummy_df():
    transactions_dict = {
        "t_dat": {
            0: "2020-04-16",
            1: "2020-04-30",
            2: "2020-05-05",
            3: "2020-05-11",
            4: "2020-05-14",
            5: "2020-05-25",
            6: "2020-06-02",
            7: "2020-06-08",
            8: "2020-06-13",
            9: "2020-06-15",
            10: "2020-06-27",
            11: "2020-07-02",
            12: "2020-07-11",
            13: "2020-07-20",
            14: "2020-07-22",
            15: "2020-07-30",
            16: "2020-07-31",
            17: "2020-08-27",
            18: "2020-09-10",
            19: "2020-09-11",
        },
        "customer_id": {
            0: "510cc6913bb6a9356b726274483f376450458db9a2bfd77fef72a0392be1d0d1",
            1: "552627c91af0ea53bf8f3a487ab1c98c138cc6aa8f725aa658ec2e9ef27edcb7",
            2: "4284c27058ee2696f1f48a8f2374b85332e34e98547b7a8a2b4d0dfc6e115cd8",
            3: "278ef6dddd46310b25f527474d816187e04870ef035213cc0cef874e06dde994",
            4: "2369b0e9d31c8176a755cdae2c0a54e74618d569e8ba2709ba162404f6f6a8e4",
            5: "20854b2caee0e89f3916a3fe32a298751b357f84da10422e474da063b396c756",
            6: "764b8665ae1a26235988a6b7044f5fea5ecdc663b003c6793e244abb3a05c60b",
            7: "b42fab593033e8b8a5bb69f1d574881bc974e637671db542635f941b5fc27f01",
            8: "7b585cc574fe0232630f20464fffd32a660cf38fbc60b15e8bd548cc7d363089",
            9: "49b680b60e75819b1ad6e640edaf5f8679d0bda521d9ced5d9063cbacb122441",
            10: "716d31c400d20613322bf8a2ddfc621604ea9756c054de47e8220d2ad94f5e78",
            11: "8a3036e08b68a572a8738d022a9a8b83f5db9f5122a93db882e35f7b850ed984",
            12: "44e97fe442c2d0e2888440964117e495bba1af1ea91840bfcf0a6ae186789ec8",
            13: "cfe2f9531825845c090e15a6cae23bb14d354af32d655fe94a731f675e19c18a",
            14: "4c5e9f28a6a074b76194355a3a43a41f28d3c40b6e7d2058c990e9e1f2845099",
            15: "22e200a42983b3423d56a9f6132474e83524156abeeebe2d1d78ad9d8fecf32f",
            16: "7ccd1c972798457a721116c9af16d3baed4065dfb78b13d1c39f1b0bafc23352",
            17: "12a774cd3087f92c962a2ab3ecb25823af90fad713de30315fe422e10e4540f7",
            18: "c29e289842392ccf1e41e7068fba15c504267913474a025a3c6e6e854fd25bc6",
            19: "64f05f5b2e57c3ad0e6f15246f45e00d7659029228851ef68f84397c7e272651",
        },
        "article_id": {
            0: "0821057001",
            1: "0783346024",
            2: "0858992001",
            3: "0685606010",
            4: "0820960003",
            5: "0547780025",
            6: "0502660002",
            7: "0874676003",
            8: "0744934007",
            9: "0875899001",
            10: "0875469005",
            11: "0458239022",
            12: "0570319054",
            13: "0851094002",
            14: "0776237020",
            15: "0921226002",
            16: "0732429003",
            17: "0865444002",
            18: "0831282001",
            19: "0860620002",
        },
        "price": {
            0: 0.033881355,
            1: 0.022864407,
            2: 0.045745764,
            3: 0.02879661,
            4: 0.013542373,
            5: 0.02540678,
            6: 0.021711864,
            7: 0.02540678,
            8: 0.016932203,
            9: 0.015237289,
            10: 0.008457627,
            11: 0.02201695,
            12: 0.02201695,
            13: 0.02201695,
            14: 0.02540678,
            15: 0.016932203,
            16: 0.015237289,
            17: 0.030491525,
            18: 0.029440679,
            19: 0.024915254,
        },
        "sales_channel_id": {
            0: 2,
            1: 2,
            2: 2,
            3: 2,
            4: 2,
            5: 2,
            6: 2,
            7: 2,
            8: 2,
            9: 2,
            10: 2,
            11: 2,
            12: 1,
            13: 2,
            14: 2,
            15: 1,
            16: 2,
            17: 2,
            18: 1,
            19: 2,
        },
    }
    df = pd.DataFrame(transactions_dict)
    return df