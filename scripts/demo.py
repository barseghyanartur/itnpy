import pandas as pd
import sys

sys.path.append("../src")

import itnpy
import itnpy.vocab as vocab


if __name__ == "__main__":
    df = vocab.get_dataframe()
    word2number = vocab.get_word2number_dict(df)

    while True:
        spoken = input("Enter spoken form text here: ")
        spoken = spoken.strip()

        spoken2 = spoken.split()
        spoken2 = itnpy.preprocess(spoken2, word2number)

        digit = itnpy.inverse_normalize_numbers(spoken2, word2number)

        spoken2 = " ".join(spoken2)
        digit = " ".join(digit)

        print()
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
