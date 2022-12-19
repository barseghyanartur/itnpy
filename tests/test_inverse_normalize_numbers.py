import pandas as pd
import pytest
import sys

sys.path.append("src")

import itnpy
import itnpy.vocab as vocab


def get_word2number_dict(path="assets/vocab.csv"):
    df = vocab.get_dataframe(path)
    return vocab.get_word2number_dict(df)


def error_message(spoken, written, output):
    df = [
        {
            "[spoken]".upper(): spoken,
            "[written]".upper(): written,
            "[output]".upper(): output,
        }
    ]
    df = pd.DataFrame(df)
    df = df.set_index("[spoken]".upper())
    df = df.T
    return "\n" + df.to_string()


@pytest.mark.parametrize(
    "path",
    [
        "tests/assets/inverse_normalize_numbers/passing.csv",
        "tests/assets/inverse_normalize_numbers/failing.csv",
    ],
)
def test_inverse_normalize_numbers(path):
    df = pd.read_csv(path, dtype={"input": object, "output": object})
    df = df.fillna("")
    word2number = get_word2number_dict()

    for _, row in df.iterrows():
        tokens = row["input"].split()
        digit = row["output"]

        tokens = itnpy.preprocess(tokens, word2number)
        output = " ".join(itnpy.inverse_normalize_numbers(tokens, word2number))
        assert output == digit, error_message(" ".join(tokens), digit, output)


@pytest.mark.parametrize(
    "path",
    [
        "tests/assets/inverse_normalize_numbers/100k.csv",
    ],
)
def test_inverse_normalize_numbers_100k(path):
    df = pd.read_csv(
        path, dtype={"data": object, "labels": object, "reference": object}
    )
    df = df.fillna("")
    word2number = get_word2number_dict()

    for _, row in df.iterrows():
        tokens = row["data"].split()
        digit = row["reference"]

        tokens = itnpy.preprocess(tokens, word2number)
        output = " ".join(itnpy.inverse_normalize_numbers(tokens, word2number))
        assert output == digit, error_message(" ".join(tokens), digit, output)

        tokens = row["labels"].split()
        digit = row["reference"]

        tokens = itnpy.preprocess(tokens, word2number)
        output = " ".join(itnpy.inverse_normalize_numbers(tokens, word2number))
        assert output == digit, error_message(" ".join(tokens), digit, output)
