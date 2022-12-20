from typing import List

from .itn import number_of_trailing_zeros

__all__ = (
    "postprocess",
    "postprocess_dollar",
    "postprocess_money",
    "preprocess",
)


# region PREPROCESS
def preprocess(tokens: List[str], word2number: dict):
    num_tokens = len(tokens)
    if num_tokens == 1:
        if tokens[0] in word2number and word2number[tokens[0]][:2] == "00":
            return ["one"] + tokens
        else:
            return tokens

    _tokens = []
    for i in range(num_tokens - 1):
        prev_token = tokens[i - 1]
        curr_token = tokens[i]
        next_token = tokens[i + 1]

        # ---- Converts cases such as "hundred and twenty" -> "hundred twenty"
        if (
            i
            and curr_token == "and"
            and next_token in word2number
            and prev_token in word2number
            and word2number[prev_token][:2] == "00"
            and number_of_trailing_zeros(word2number[prev_token])
            > number_of_trailing_zeros(word2number[next_token])
        ):
            continue

        # ---- Converts cases such as "hundred" -> "one hundred"
        elif (
            i
            and (
                not word2number.get(prev_token, [""])[0].isdigit()
                or word2number.get(prev_token, [""]) == "0"
            )
            and curr_token in word2number
            and word2number[curr_token][:2] == "00"
        ) or (
            not i
            and curr_token in word2number
            and word2number[curr_token][:2] == "00"
        ):
            _tokens.append("one")
            _tokens.append(curr_token)

        # ---- Converts cases such as "double zero" -> "zero zero"
        elif curr_token == "double" and (
            (next_token in word2number and word2number[next_token].isdigit())
            or len(next_token) == 1
        ):
            _tokens.append(next_token)

        # ---- Converts cases such as "triple zero" -> "zero zero zero"
        elif curr_token == "triple" and (
            (next_token in word2number and word2number[next_token].isdigit())
            or len(next_token) == 1
        ):
            _tokens.append(next_token)
            _tokens.append(next_token)

        # ---- Converts cases such as "quadruple zero" -> "zero zero zero zero"
        elif curr_token == "quadruple" and (
            (next_token in word2number and word2number[next_token].isdigit())
            or len(next_token) == 1
        ):
            _tokens.append(next_token)
            _tokens.append(next_token)
            _tokens.append(next_token)

        else:
            _tokens.append(curr_token)

    if _tokens:
        if (
            (
                not word2number.get(curr_token, [""])[0].isdigit()
                or word2number.get(curr_token, [""]) == "0"
            )
            and next_token in word2number
            and word2number[next_token][:2] == "00"
        ):
            _tokens.append("one")
        _tokens.append(next_token)

    return _tokens


# endregion

# region POSTPROCESS
def postprocess(tokens: List[str]):
    tokens = [chars for token in tokens for chars in token.split()]
    tokens = postprocess_dollar(tokens)
    tokens = postprocess_money(tokens)
    tokens = postprocess_money(tokens)
    return tokens


def postprocess_dollar(tokens: List[str]):
    tokens = [
        (
            f"{token[-1]}{token[:-1]}"
            if token[0] != "-" and token[0] != "+"
            else f"{token[0]}{token[-1]}{token[1:-1]}"
        )
        if token[-1] == "$"
        else token
        for token in tokens
    ]
    return tokens


def postprocess_money(tokens: List[str]):
    num_tokens = len(tokens)
    if num_tokens == 1:
        return tokens

    _tokens = []
    for i in range(num_tokens - 1):
        prev_token = tokens[i - 1]
        curr_token = tokens[i]
        next_token = tokens[i + 1]

        # ---- Converts cases such as $1 1¢ -> $1.01
        if "$" in curr_token and "¢" in next_token:
            dollar = curr_token
            cent = next_token[:-1]
            if len(cent) <= 1:
                cent = f"0{cent}"
            _tokens.append(f"{dollar}.{cent}")

        elif i and "¢" in curr_token and "$" in prev_token:
            continue

        # ---- Converts cases such as $1 and 1¢ -> $1 1¢
        elif (
            i
            and curr_token == "and"
            and "¢" in next_token
            and "$" in prev_token
        ):
            continue

        else:
            _tokens.append(curr_token)

    if _tokens:
        if "¢" not in next_token or (
            "$" not in curr_token and "¢" in next_token
        ):
            _tokens.append(next_token)

    return _tokens


# endregion
