from typing import Callable, List, Union

from itnpy import vocab
from itnpy._version import __version__
from itnpy.custom import (
    postprocess,
    postprocess_dollar,
    postprocess_money,
    preprocess,
)
from itnpy.itn import (
    group_tokens,
    inverse_normalize_classes,
    inverse_normalize_numbers,
    number_length,
    number_of_trailing_zeros,
    spokens2digit,
    tokens2digit,
)

__all__ = (
    "__version__",
    "group_tokens",
    "inverse_normalize",
    "inverse_normalize_classes",
    "inverse_normalize_numbers",
    "number_length",
    "number_of_trailing_zeros",
    "postprocess",
    "postprocess_dollar",
    "postprocess_money",
    "preprocess",
    "spokens2digit",
    "tokens2digit",
    "vocab",
)


def inverse_normalize(
    spoken_tokens: List[str],
    word2number: dict,
    output_nested: bool = False,
    normalize_func: Callable[
        [List[str]], List[str]
    ] = inverse_normalize_numbers,
    preprocess_func: Callable[[List[str]], List[str]] = preprocess,
    postprocess_func: Callable[[List[str]], List[str]] = postprocess,
) -> Union[List[str], List[List[str]]]:
    pass

    spoken_tokens = preprocess_func(spoken_tokens, word2number)
    written_tokens = normalize_func(spoken_tokens, word2number)

    if output_nested:
        output_tokens = [postprocess_func(tokens) for tokens in written_tokens]
    else:
        output_tokens = postprocess_func(written_tokens)

    return output_tokens
