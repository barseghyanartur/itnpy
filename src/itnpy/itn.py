import itertools
from typing import List, Union

__all__ = (
    "BACKGROUND_CLASS",
    "inverse_normalize_numbers",
    "group_tokens",
    "spokens2digit",
    "tokens2digit",
    "number_length",
    "number_of_trailing_zeros",
    "inverse_normalize_classes",
)

BACKGROUND_CLASS = "self"


# region NUMBERS
def inverse_normalize_numbers(
    spoken_tokens: List[str], word2number: dict, output_nested: bool = False
) -> Union[List[str], List[List[str]]]:
    groups = _inverse_normalize_numbers(spoken_tokens, word2number)
    if output_nested:
        return groups

    tokens = [token.strip() for group in groups for token in group]
    return tokens


def _inverse_normalize_numbers(
    spoken_tokens: List[str], word2number: dict
) -> List[List[str]]:
    mask = [True if token in word2number else False for token in spoken_tokens]
    groups = group_tokens(spoken_tokens, mask)
    groups = [
        [spokens2digit(v, word2number)] if k else v
        for group in groups
        for k, v in group.items()
    ]
    return groups


def group_tokens(tokens: List[str], mask: List[int]) -> List[dict]:
    groups = []
    start = 0

    for i, _ in enumerate(tokens):
        if i:
            if value != mask[i]:
                groups.append({value: tokens[start:i]})
                start = i

        value = mask[i]

    if tokens:
        groups.append({value: tokens[start : i + 1]})

    return groups


def spokens2digit(spoken_numbers: List[str], word2number: dict) -> str:
    tokens = [word2number[token] for token in spoken_numbers]
    return tokens2digit(tokens)


def tokens2digit(tokens: List[str]) -> str:
    num_tokens = len(tokens)
    if num_tokens == 1:
        return tokens[0]

    digit = ""
    for i in range(num_tokens - 1, 0, -1):
        curr_token = tokens[i]
        prev_token = tokens[i - 1]
        curr_digit = digit if i < num_tokens - 1 else curr_token

        len_prev = number_length(prev_token)
        len_curr = number_length(curr_token)
        len_digit = number_length(curr_digit)
        len_zeros = number_of_trailing_zeros(prev_token)

        if len_zeros < len_curr:
            digit = prev_token + curr_digit
        else:
            if len_prev == 1:
                digit = prev_token + curr_digit
            elif curr_digit[0] == "0":
                digit = prev_token + curr_digit
            elif not curr_digit[0].isdigit():
                digit = prev_token + curr_digit
            elif prev_token == "10":
                digit = prev_token + curr_digit
            elif len_prev == len_zeros:
                if len_prev < len_digit:
                    digit = prev_token[: len_prev - len_curr] + curr_digit
                else:
                    digit = prev_token[: len_prev - len_digit] + curr_digit
            else:
                digit = prev_token[: len_prev - len_zeros] + curr_digit

    return digit


def number_length(number: str) -> int:
    return sum(
        1 for _ in (itertools.takewhile(lambda digit: digit.isdigit(), number))
    )


def number_of_trailing_zeros(digit: str) -> int:
    len_digit = len(digit)
    zeros = 0

    for i in range(1, len_digit + 1):
        if digit[-i] == "0":
            zeros += 1
        else:
            return zeros

    return zeros


# endregion

# region CLASSES
def inverse_normalize_classes(
    spoken_tokens: List[str], word2class: dict, output_nested: bool = False
) -> Union[List[str], List[List[str]]]:
    groups = _inverse_normalize_classes(spoken_tokens, word2class)
    if output_nested:
        return groups

    tokens = [token.strip() for group in groups for token in group]
    return tokens


def _inverse_normalize_classes(
    spoken_tokens: List[str], word2class: dict
) -> List[List[str]]:
    mask = [True if token in word2class else False for token in spoken_tokens]
    groups = group_tokens(spoken_tokens, mask)
    groups = [
        [word2class[t] for t in v] if k else [BACKGROUND_CLASS for _ in v]
        for group in groups
        for k, v in group.items()
    ]
    return groups


# endregion
