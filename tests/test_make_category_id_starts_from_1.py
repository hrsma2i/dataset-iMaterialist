from imaterialist.cli.make_category_id_starts_from_1 import shift


def test_shift():
    d = {
        "categories": [{"id": 0}, {"id": 1}],
        "attributes": [
            {"id": 128},
            {"id": 325},
            {"id": 102},
            {"id": 295},
            {"id": 301},
            {"id": 142},
            {"id": 115},
            {"id": 316},
            {"id": 317},
        ],
        "annotations": [
            {
                "category_id": 0,
                "attribute_ids": [128, 325, 102, 295, 301, 142, 115, 316, 317],
            }
        ],
    }
    actual = shift(d)

    expected = {
        "categories": [{"id": 1}, {"id": 2}],
        "attributes": [
            {"id": 129},
            {"id": 326},
            {"id": 103},
            {"id": 296},
            {"id": 302},
            {"id": 143},
            {"id": 116},
            {"id": 317},
            {"id": 318},
        ],
        "annotations": [
            {
                "category_id": 1,
                "attribute_ids": [129, 326, 103, 296, 302, 143, 116, 317, 318],
            }
        ],
    }

    assert actual == expected
