# This script extracts information and saves it as memo.json

import json
import os
from extract_memo import extract_information


TRANSCRIPT_PATH = "../transcripts/demo_call_1.txt"
OUTPUT_FOLDER = "../outputs/accounts/account_001/v1"


def main():

    # read transcript
    with open(TRANSCRIPT_PATH, "r", encoding="utf-8") as f:
        transcript = f.read()

    # extract information
    memo = extract_information(transcript)

    # ensure output folder exists
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # save json
    output_path = os.path.join(OUTPUT_FOLDER, "memo.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(memo, f, indent=4)

    print("\nMemo saved successfully at:")
    print(output_path)


if __name__ == "__main__":
    main()