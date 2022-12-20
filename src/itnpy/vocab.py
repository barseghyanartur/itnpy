import pandas as pd

__all__ = (
    "get_dataframe",
    "get_number2class_dict",
    "get_word2class_dict",
    "get_word2number_dict",
    "number2word_dict",
)

GITHUB_CSV = (
    "https://raw.githubusercontent.com/barseghyanartur/itnpy/master/"
    "assets/vocab.csv"
)


def get_dataframe(path: str = GITHUB_CSV) -> pd.DataFrame:
    return pd.read_csv(path, dtype={"number": object})


def get_word2number_dict(df: pd.DataFrame) -> dict:
    return {k: v for k, v in zip(df["word"], df["number"])}


def number2word_dict(df: pd.DataFrame) -> dict:
    return {k: v for k, v in zip(df["number"], df["word"])}


def get_word2class_dict(df: pd.DataFrame) -> dict:
    return {k: v for k, v in zip(df["word"], df["class"])}


def get_number2class_dict(df: pd.DataFrame) -> dict:
    return {k: v for k, v in zip(df["number"], df["class"])}
