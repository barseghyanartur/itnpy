import pandas as pd
import sys

sys.path.append("../src")

import itnpy
import itnpy.vocab as vocab


EXAMPLES = [
    "i payed one hundred and twenty seven dollars and twenty six cents",
    "was your birthday on march twenty ninth",
    "my phone number is nine four nine six eight two seventy fourteen",
    "i have a minus one hundred point four three balance",
    "calling to place an order of three hundred thousand sixty four hundred and eighteen parts",
    "my order id is seven eighteen fourteen fifteen nine eight zero",
    "my date of birth is three seven fifty four",
    "what is eighty percent of negative point nine four",
    "seems to cost a thousand or more maybe a few hundred or so",
]

if __name__ == "__main__":

    # --- Get the vocab for converting spoken-form text into written-form text
    df = vocab.get_dataframe()
    word2number = vocab.get_word2number_dict(df)

    for example in EXAMPLES:

        # ---- Preprocess text
        spoken = example.strip()
        spoken2 = spoken.split()
        # NOTE: This can be modified depending on your needs
        spoken2 = itnpy.preprocess(spoken2, word2number)

        # --- Convert spoken-form tokens to written-form tokens
        digit = itnpy.inverse_normalize_numbers(spoken2, word2number)

        # --- Convert tokens to string
        spoken2 = " ".join(spoken2)
        digit = " ".join(digit)

        # ---- Display results
        df = [
            {
                "[spoken]".upper(): spoken,
                "[spoken2]".upper(): spoken2,
                "[written]".upper(): digit,
            }
        ]
        df = pd.DataFrame(df)
        df = df.set_index("[spoken]".upper())
        df = df.T
        print(df.to_string())
        print()
