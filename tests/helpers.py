import pandas as pd

import itnpy.vocab as vocab

__all__ = (
    "get_word2number_dict",
    "error_message",
)


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
