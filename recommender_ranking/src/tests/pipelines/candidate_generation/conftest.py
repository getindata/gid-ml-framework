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
            6: "c29e289842392ccf1e41e7068fba15c504267913474a025a3c6e6e854fd25bc6",
            7: "b42fab593033e8b8a5bb69f1d574881bc974e637671db542635f941b5fc27f01",
            8: "7b585cc574fe0232630f20464fffd32a660cf38fbc60b15e8bd548cc7d363089",
            9: "49b680b60e75819b1ad6e640edaf5f8679d0bda521d9ced5d9063cbacb122441",
            10: "716d31c400d20613322bf8a2ddfc621604ea9756c054de47e8220d2ad94f5e78",
            11: "8a3036e08b68a572a8738d022a9a8b83f5db9f5122a93db882e35f7b850ed984",
            12: "44e97fe442c2d0e2888440964117e495bba1af1ea91840bfcf0a6ae186789ec8",
            13: "552627c91af0ea53bf8f3a487ab1c98c138cc6aa8f725aa658ec2e9ef27edcb7",
            14: "4c5e9f28a6a074b76194355a3a43a41f28d3c40b6e7d2058c990e9e1f2845099",
            15: "22e200a42983b3423d56a9f6132474e83524156abeeebe2d1d78ad9d8fecf32f",
            16: "4284c27058ee2696f1f48a8f2374b85332e34e98547b7a8a2b4d0dfc6e115cd8",
            17: "12a774cd3087f92c962a2ab3ecb25823af90fad713de30315fe422e10e4540f7",
            18: "c29e289842392ccf1e41e7068fba15c504267913474a025a3c6e6e854fd25bc6",
            19: "64f05f5b2e57c3ad0e6f15246f45e00d7659029228851ef68f84397c7e272651",
        },
        "article_id": {
            0: "0821057001",
            1: "0821057001",
            2: "0821057001",
            3: "0821057001",
            4: "0547780025",
            5: "0547780025",
            6: "0547780025",
            7: "0744934007",
            8: "0744934007",
            9: "0875899001",
            10: "0875899001",
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


@pytest.fixture
def customers_dummy_df():
    customers_dict = {
        "customer_id": {
            0: "0eef970dea82d038c9f0a85a8ac76e001712f138bce479f934e21f9f80f74ead",
            1: "932acbb5e5dd33b2d630cebc8f17509321e2a2f8290b82e797a9606f70a5356b",
            2: "633762090ccf0672c702539978d0b8507ef33d538a8393beb54b28a014bfa51c",
            3: "6d4993166107a18eff7bd82a55c2874270db28f7526e7d2da6a33129c28b5499",
            4: "71708841d90876170535a97d647c95d9f766cb5836bc3e7769a8674222136354",
            5: "caf736a6bd5545a59a3a003ad883eefbeb9653ca1b1b00f766c3f85920635a73",
            6: "f3714e6286d025e1280deca7cd0d3ce5db8c3bbb67129a7152a034861cd29f39",
            7: "50f15803d727117a5db3b4e11f63d254496ff9d2e74e24d7f0e79bd3eaa9fcf2",
            8: "438967b6cf7d8035b2704055ca17fd1a03610bb81e12a11fb43209a706378475",
            9: "86e68da86e8411fdcc7dcc9f1ed81d1abdd87d1c387bea926d0d0a0c8f683c04",
        },
        "FN": {
            0: pd.NA,
            1: pd.NA,
            2: pd.NA,
            3: 1.0,
            4: 1.0,
            5: pd.NA,
            6: pd.NA,
            7: 1.0,
            8: pd.NA,
            9: pd.NA,
        },
        "Active": {
            0: pd.NA,
            1: pd.NA,
            2: pd.NA,
            3: 1.0,
            4: 1.0,
            5: pd.NA,
            6: pd.NA,
            7: 1.0,
            8: pd.NA,
            9: pd.NA,
        },
        "club_member_status": {
            0: "ACTIVE",
            1: "ACTIVE",
            2: "ACTIVE",
            3: "ACTIVE",
            4: "ACTIVE",
            5: "ACTIVE",
            6: "ACTIVE",
            7: "ACTIVE",
            8: "ACTIVE",
            9: "ACTIVE",
        },
        "fashion_news_frequency": {
            0: "NONE",
            1: "NONE",
            2: "NONE",
            3: "Regularly",
            4: "Regularly",
            5: "NONE",
            6: "NONE",
            7: "Regularly",
            8: "NONE",
            9: "NONE",
        },
        "age": {
            0: 34.0,
            1: 57.0,
            2: 53.0,
            3: 34.0,
            4: 41.0,
            5: 22.0,
            6: 28.0,
            7: 26.0,
            8: 35.0,
            9: 74.0,
        },
        "postal_code": {
            0: "b5d203a7c8ec8ed75bf8648239f04ce72260d510ac8f0b4aaa93ae26834f9be0",
            1: "cab69d943b164fe4aa533cc80acd57b4d5987b8df700ab18cf5473b39758e5ea",
            2: "2ec126bd9a1e0cd69f8b3e24ce347152760b195ffbbc65cf144bd0de20611df6",
            3: "2c29ae653a9282cce4151bd87643c907644e09541abc28ae87dea0d1f6603b1c",
            4: "2d558092f25166a37cf12f323157e85102e7d4acb259dc6886e7d135e37371ca",
            5: "ddcc174c8e2d42c0f083aab1792ba880cad8f7514f785356a17166407f898986",
            6: "9dedd0aa9b998c43ea633dd0d0fd960cc81274c73e4e64bd36f08237c8537d25",
            7: "5921d8dad3322e8783fc9ee77c5a065390655d8d1631c9253eeb3947b84e97c8",
            8: "2c29ae653a9282cce4151bd87643c907644e09541abc28ae87dea0d1f6603b1c",
            9: "2c29ae653a9282cce4151bd87643c907644e09541abc28ae87dea0d1f6603b1c",
        },
    }
    df = pd.DataFrame(customers_dict)
    return df


@pytest.fixture
def articles_dummy_df():
    articles_dict = {
        "article_id": {
            0: "0685814001",
            1: "0730683050",
            2: "0623522005",
            3: "0793704001",
            4: "0909911001",
            5: "0783346011",
            6: "0751471038",
            7: "0744934007",
            8: "0547780025",
            9: "0916468001",
        },
        "prod_name": {
            0: "Clark slim trs tech",
            1: "20 den 2p Tights",
            2: "Nina Strap",
            3: "GREY Scale Tee",
            4: "Robin 3pk Anchor",
            5: "Moccha brazilian",
            6: "Christina patent boot",
            7: "Mike Slim Jogger",
            8: "Fiona Ch Hipster(Poppy)4pk",
            9: "BB SVEN set",
        },
    }
    df = pd.DataFrame(articles_dict)
    return df
