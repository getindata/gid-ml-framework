import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def candidates_dummy_df():
    candidates_dict = {
        "customer_id": {
            0: "0d1a47760911611b4c5ac7d33df54003659933c307a5ef3d65e0bba2ba7d77d5",
            1: "4faa82eaaa6db4f2265651700370c9161e445703bd8d6771f219d08e9fec27f4",
            2: "8b9d95062f01a3466a0a71de0f974ff3a082924c9551bfe3b1a9f3ccb6dbe393",
            3: "a0006a00a5917966bd2ba60b8991fa25b643f1f0cd4d273d0785646e1017fb8d",
            4: "ad34c941ebcd1db25f65504f4a95640e105df3f6b8829aca929aedb8f95d0ca0",
            5: "dd98fec0a17270aaa20f6c9f541855853aa6928553d4f1275c017642df10e2a6",
            6: "deb4cc7f7924765b3ed7e6c7fec2c5be094dc5d3d65dfaa820dfe673f89e10c0",
            7: "e02846d1991ca4714125313c15870d54b20193592afe46975b212d59aace1a04",
            8: "e2d7f9daeb26891537d77b2a7078cccb1801d8e04b1427afe155e763461a77af",
            9: "ec2106342f4e1f2756369a402cfb21d2065f982ce7524eb53a9607ad686223b2",
        },
        "global_articles": {
            0: np.array(
                [
                    "0554479001",
                    "0904571001",
                    "0869331006",
                    "0902528006",
                    "0852775004",
                    "0698276009",
                    "0884319009",
                    "0832481002",
                    "0688728023",
                    "0158340001",
                    "0706016015",
                ],
                dtype=object,
            ),
            1: np.array(
                [
                    "0554479001",
                    "0904571001",
                    "0869331006",
                    "0902528006",
                    "0852775004",
                    "0698276009",
                    "0884319009",
                    "0832481002",
                    "0688728023",
                    "0158340001",
                    "0706016015",
                ],
                dtype=object,
            ),
            2: np.array(
                [
                    "0554479001",
                    "0904571001",
                    "0869331006",
                    "0902528006",
                    "0852775004",
                    "0698276009",
                    "0884319009",
                    "0832481002",
                    "0688728023",
                    "0158340001",
                    "0706016015",
                ],
                dtype=object,
            ),
            3: np.array(
                [
                    "0554479001",
                    "0904571001",
                    "0869331006",
                    "0902528006",
                    "0852775004",
                    "0698276009",
                    "0884319009",
                    "0832481002",
                    "0688728023",
                    "0158340001",
                    "0706016015",
                ],
                dtype=object,
            ),
            4: np.array(
                [
                    "0554479001",
                    "0904571001",
                    "0869331006",
                    "0902528006",
                    "0852775004",
                    "0698276009",
                    "0884319009",
                    "0832481002",
                    "0688728023",
                    "0158340001",
                    "0706016015",
                ],
                dtype=object,
            ),
            5: np.array(
                [
                    "0554479001",
                    "0904571001",
                    "0869331006",
                    "0902528006",
                    "0852775004",
                    "0698276009",
                    "0884319009",
                    "0832481002",
                    "0688728023",
                    "0158340001",
                    "0706016015",
                ],
                dtype=object,
            ),
            6: np.array(
                [
                    "0554479001",
                    "0904571001",
                    "0869331006",
                    "0902528006",
                    "0852775004",
                    "0698276009",
                    "0884319009",
                    "0832481002",
                    "0688728023",
                    "0158340001",
                    "0706016015",
                ],
                dtype=object,
            ),
            7: np.array(
                [
                    "0554479001",
                    "0904571001",
                    "0869331006",
                    "0902528006",
                    "0852775004",
                    "0698276009",
                    "0884319009",
                    "0832481002",
                    "0688728023",
                    "0158340001",
                    "0706016015",
                ],
                dtype=object,
            ),
            8: np.array(
                [
                    "0554479001",
                    "0904571001",
                    "0869331006",
                    "0902528006",
                    "0852775004",
                    "0698276009",
                    "0884319009",
                    "0832481002",
                    "0688728023",
                    "0158340001",
                    "0706016015",
                ],
                dtype=object,
            ),
            9: np.array(
                [
                    "0554479001",
                    "0904571001",
                    "0869331006",
                    "0902528006",
                    "0852775004",
                    "0698276009",
                    "0884319009",
                    "0832481002",
                    "0688728023",
                    "0158340001",
                    "0706016015",
                ],
                dtype=object,
            ),
        },
        "segment_articles": {
            0: np.array(
                [
                    "0904571001",
                    "0869331006",
                    "0792469001",
                    "0902528006",
                    "0852775004",
                    "0698276009",
                    "0758002011",
                    "0928040002",
                    "0832481002",
                    "0688728023",
                    "0158340001",
                ],
                dtype=object,
            ),
            1: np.array(
                [
                    "0904571001",
                    "0869331006",
                    "0792469001",
                    "0902528006",
                    "0852775004",
                    "0698276009",
                    "0758002011",
                    "0928040002",
                    "0832481002",
                    "0688728023",
                    "0158340001",
                ],
                dtype=object,
            ),
            2: np.array(
                [
                    "0678942058",
                    "0895423005",
                    "0904571001",
                    "0902528006",
                    "0301656029",
                    "0851780001",
                    "0884319009",
                    "0698276009",
                    "0751471027",
                    "0832481002",
                    "0922381002",
                ],
                dtype=object,
            ),
            3: np.array(
                [
                    "0678942058",
                    "0664074039",
                    "0768921001",
                    "0904571001",
                    "0848420007",
                    "0554479001",
                    "0776237019",
                    "0869331006",
                    "0792469001",
                    "0903790001",
                    "0698276009",
                ],
                dtype=object,
            ),
            4: np.array(
                [
                    "0678942058",
                    "0895423005",
                    "0904571001",
                    "0902528006",
                    "0301656029",
                    "0851780001",
                    "0884319009",
                    "0698276009",
                    "0751471027",
                    "0832481002",
                    "0922381002",
                ],
                dtype=object,
            ),
            5: np.array(
                [
                    "0678942058",
                    "0895423005",
                    "0904571001",
                    "0902528006",
                    "0301656029",
                    "0851780001",
                    "0884319009",
                    "0698276009",
                    "0751471027",
                    "0832481002",
                    "0922381002",
                ],
                dtype=object,
            ),
            6: np.array(
                [
                    "0678942058",
                    "0895423005",
                    "0904571001",
                    "0902528006",
                    "0301656029",
                    "0851780001",
                    "0884319009",
                    "0698276009",
                    "0751471027",
                    "0832481002",
                    "0922381002",
                ],
                dtype=object,
            ),
            7: np.array(
                [
                    "0678942058",
                    "0664074039",
                    "0768921001",
                    "0904571001",
                    "0848420007",
                    "0554479001",
                    "0776237019",
                    "0869331006",
                    "0792469001",
                    "0903790001",
                    "0698276009",
                ],
                dtype=object,
            ),
            8: np.array(
                [
                    "0904571001",
                    "0869331006",
                    "0792469001",
                    "0902528006",
                    "0852775004",
                    "0698276009",
                    "0758002011",
                    "0928040002",
                    "0832481002",
                    "0688728023",
                    "0158340001",
                ],
                dtype=object,
            ),
            9: np.array(
                [
                    "0678942058",
                    "0895423005",
                    "0904571001",
                    "0902528006",
                    "0301656029",
                    "0851780001",
                    "0884319009",
                    "0698276009",
                    "0751471027",
                    "0832481002",
                    "0922381002",
                ],
                dtype=object,
            ),
        },
        "previously_bought": {
            0: None,
            1: np.array(
                ["0606395030", "0850871002", "0860819001", "0773049001", "0712924016"],
                dtype=object,
            ),
            2: None,
            3: None,
            4: None,
            5: np.array(
                ["0835768002", "0843012002", "0822158001", "0791223006"], dtype=object
            ),
            6: np.array(["0811907006", "0688105016"], dtype=object),
            7: np.array(["0861583008"], dtype=object),
            8: np.array(["0759469001", "0829045009", "0880060003"], dtype=object),
            9: None,
        },
        "previously_bought_prod_name": {
            0: None,
            1: np.array(
                [
                    "0850871003",
                    "0850871001",
                    "0850871002",
                    "0773049001",
                    "0860819001",
                    "0606395030",
                    "0712924016",
                ],
                dtype=object,
            ),
            2: None,
            3: None,
            4: None,
            5: np.array(
                ["0822158003", "0822158001", "0791223006", "0835768002", "0843012002"],
                dtype=object,
            ),
            6: np.array(
                ["0811907001", "0811907003", "0811907006", "0688105016"], dtype=object
            ),
            7: np.array(["0861583008", "0861583002"], dtype=object),
            8: np.array(["0759469001", "0829045009", "0880060003"], dtype=object),
            9: None,
        },
        "closest_image_embeddings": {
            0: None,
            1: np.array(
                [
                    "0568478014",
                    "0785822001",
                    "0752432002",
                    "0903381002",
                    "0875736003",
                    "0683770001",
                    "0575347009",
                    "0775150001",
                    "0672625005",
                    "0775505002",
                    "0769269001",
                    "0775405001",
                    "0656868003",
                    "0657276002",
                    "0603145009",
                    "0744717001",
                    "0737994002",
                    "0679484003",
                    "0711297006",
                    "0681381009",
                ],
                dtype=object,
            ),
            2: None,
            3: None,
            4: None,
            5: np.array(
                [
                    "0851094008",
                    "0735607011",
                    "0710548001",
                    "0696974002",
                    "0752814003",
                    "0745091003",
                    "0779781012",
                    "0658978003",
                    "0741115004",
                    "0779324006",
                    "0632982033",
                    "0806840002",
                    "0914960001",
                    "0706896001",
                    "0747373001",
                    "0794320007",
                ],
                dtype=object,
            ),
            6: np.array(
                [
                    "0905254011",
                    "0468480035",
                    "0635392001",
                    "0719687005",
                    "0522461003",
                    "0671189001",
                    "0899364002",
                    "0905889002",
                ],
                dtype=object,
            ),
            7: np.array(
                ["0724164001", "0688546001", "0677809001", "0779341001"], dtype=object
            ),
            8: np.array(
                [
                    "0917288001",
                    "0673638007",
                    "0679853003",
                    "0218354047",
                    "0651289005",
                    "0892699003",
                    "0710091003",
                    "0640662004",
                    "0629692002",
                    "0783217004",
                    "0908466001",
                    "0862104018",
                ],
                dtype=object,
            ),
            9: None,
        },
        "closest_text_embeddings": {
            0: None,
            1: np.array(
                [
                    "0712924003",
                    "0712924012",
                    "0712924008",
                    "0712924001",
                    "0712924006",
                    "0860819002",
                    "0823505002",
                    "0823505001",
                    "0582480001",
                    "0828556001",
                    "0759139002",
                    "0872514001",
                    "0841668001",
                    "0850871001",
                    "0850871003",
                    "0880123001",
                    "0736190001",
                    "0606395003",
                    "0606395011",
                    "0606395014",
                    "0606395001",
                    "0606395006",
                ],
                dtype=object,
            ),
            2: None,
            3: None,
            4: None,
            5: np.array(
                [
                    "0791223007",
                    "0791223002",
                    "0791223001",
                    "0734112002",
                    "0822158002",
                    "0822158003",
                    "0844390001",
                    "0639136001",
                    "0843012001",
                    "0696987001",
                    "0621410002",
                    "0621410001",
                    "0835768001",
                    "0795720003",
                    "0822224001",
                    "0858453002",
                ],
                dtype=object,
            ),
            6: np.array(
                [
                    "0688105002",
                    "0688105008",
                    "0688105004",
                    "0688105003",
                    "0688105007",
                    "0811907001",
                    "0811907003",
                    "0811907005",
                    "0811907004",
                ],
                dtype=object,
            ),
            7: np.array(
                ["0861583002", "0861583001", "0861583009", "0891630001"], dtype=object
            ),
            8: np.array(
                [
                    "0856949001",
                    "0638256003",
                    "0759479001",
                    "0695584001",
                    "0880060002",
                    "0829145004",
                    "0829145003",
                    "0829145005",
                    "0829045004",
                    "0829045006",
                    "0829045003",
                    "0829045005",
                ],
                dtype=object,
            ),
            9: None,
        },
    }
    df = pd.DataFrame(candidates_dict)
    return df


@pytest.fixture
def transactions_dummy_df():
    transactions_dict = {
        "t_dat": {
            0: "2020-04-01",
            1: "2020-04-01",
            2: "2020-04-03",
            3: "2020-04-11",
            4: "2020-04-22",
            5: "2020-05-02",
            6: "2020-05-20",
            7: "2020-05-21",
            8: "2020-05-27",
            9: "2020-06-01",
            10: "2020-06-11",
            11: "2020-07-05",
            12: "2020-07-13",
            13: "2020-07-14",
            14: "2020-07-16",
            15: "2020-07-17",
            16: "2020-07-17",
            17: "2020-07-23",
            18: "2020-08-29",
            19: "2020-09-20",
        },
        "customer_id": {
            0: "0d1a47760911611b4c5ac7d33df54003659933c307a5ef3d65e0bba2ba7d77d5",
            1: "deb4cc7f7924765b3ed7e6c7fec2c5be094dc5d3d65dfaa820dfe673f89e10c0",
            2: "e2d7f9daeb26891537d77b2a7078cccb1801d8e04b1427afe155e763461a77af",
            3: "deb4cc7f7924765b3ed7e6c7fec2c5be094dc5d3d65dfaa820dfe673f89e10c0",
            4: "a0006a00a5917966bd2ba60b8991fa25b643f1f0cd4d273d0785646e1017fb8d",
            5: "ec2106342f4e1f2756369a402cfb21d2065f982ce7524eb53a9607ad686223b2",
            6: "deb4cc7f7924765b3ed7e6c7fec2c5be094dc5d3d65dfaa820dfe673f89e10c0",
            7: "deb4cc7f7924765b3ed7e6c7fec2c5be094dc5d3d65dfaa820dfe673f89e10c0",
            8: "dd98fec0a17270aaa20f6c9f541855853aa6928553d4f1275c017642df10e2a6",
            9: "dd98fec0a17270aaa20f6c9f541855853aa6928553d4f1275c017642df10e2a6",
            10: "0d1a47760911611b4c5ac7d33df54003659933c307a5ef3d65e0bba2ba7d77d5",
            11: "dd98fec0a17270aaa20f6c9f541855853aa6928553d4f1275c017642df10e2a6",
            12: "dd98fec0a17270aaa20f6c9f541855853aa6928553d4f1275c017642df10e2a6",
            13: "a0006a00a5917966bd2ba60b8991fa25b643f1f0cd4d273d0785646e1017fb8d",
            14: "ec2106342f4e1f2756369a402cfb21d2065f982ce7524eb53a9607ad686223b2",
            15: "deb4cc7f7924765b3ed7e6c7fec2c5be094dc5d3d65dfaa820dfe673f89e10c0",
            16: "e2d7f9daeb26891537d77b2a7078cccb1801d8e04b1427afe155e763461a77af",
            17: "deb4cc7f7924765b3ed7e6c7fec2c5be094dc5d3d65dfaa820dfe673f89e10c0",
            18: "4faa82eaaa6db4f2265651700370c9161e445703bd8d6771f219d08e9fec27f4",
            19: "4faa82eaaa6db4f2265651700370c9161e445703bd8d6771f219d08e9fec27f4",
        },
        "article_id": {
            0: "0698276009",
            1: "0456163086",
            2: "0759469001",
            3: "0851094002",
            4: "0678942058",
            5: "0756320022",
            6: "0840475001",
            7: "0885951001",
            8: "0690936013",
            9: "0876306001",
            10: "0158340001",
            11: "0878190005",
            12: "0895582008",
            13: "0351484002",
            14: "0862433001",
            15: "0781613001",
            16: "0856949001",
            17: "0903926001",
            18: "0880553001",
            19: "0606395030",
        },
        "price": {
            0: 0.084728815,
            1: 0.010152542,
            2: 0.013542373,
            3: 0.01761017,
            4: 0.042355932,
            5: 0.033881355,
            6: 0.05083051,
            7: 0.016932203,
            8: 0.05083051,
            9: 0.02201695,
            10: 0.016932203,
            11: 0.041050848,
            12: 0.016932203,
            13: 0.02201695,
            14: 0.059305083,
            15: 0.05083051,
            16: 0.008457627,
            17: 0.0120508475,
            18: 0.02540678,
            19: 0.008457627,
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
            12: 2,
            13: 2,
            14: 1,
            15: 2,
            16: 2,
            17: 2,
            18: 2,
            19: 2,
        },
    }
    df = pd.DataFrame(transactions_dict)
    return df