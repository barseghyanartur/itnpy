import pandas as pd
import pytest
import sys

sys.path.append("src")

import itnpy


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
        "tests/assets/tokens2digit/passing.csv",
        "tests/assets/tokens2digit/failing.csv",
    ],
)
def test_tokens2digit(path):
    df = pd.read_csv(path, dtype={"input": object, "output": object})
    df = df.fillna("")

    for _, row in df.iterrows():
        tokens = row["input"].split()
        digit = row["output"]
        output = itnpy.tokens2digit(tokens)
        assert output == digit, error_message(" ".join(tokens), digit, output)
