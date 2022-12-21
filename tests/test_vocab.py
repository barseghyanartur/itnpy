import pandas as pd
import pytest

import itnpy

from .helpers import error_message, get_word2number_dict


@pytest.mark.parametrize(
    "path",
    [
        "tests/assets/vocab/passing.csv",
        "tests/assets/vocab/failing.csv",
    ],
)
def test_vocab(path):
    df = pd.read_csv(path, dtype={"input": object, "output": object})
    df = df.fillna("")
    # --- Get the vocab for converting spoken-form text into written-form text
    word2number = get_word2number_dict()

    for _, row in df.iterrows():
        tokens = row["input"].strip()
        output = row["output"].strip()
        # NOTE: This can be modified depending on your needs
        spoken2 = itnpy.preprocess(tokens.split(), word2number)
        # --- Convert spoken-form tokens to written-form tokens
        digit = itnpy.inverse_normalize_numbers(spoken2, word2number)
        # --- Convert tokens to string
        digit = " ".join(digit)
        assert output == digit, error_message(" ".join(tokens), digit, output)
