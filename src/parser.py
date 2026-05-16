import conllu
import json
import pandas as pd
from pathlib import Path


def extract_text_from_cupt(file_path):
    """process the text in cupt files and return a list of dictionaries"""
    with open(file_path, "r", encoding="utf-8") as file:
        sentences = conllu.parse(file.read())

    data = []

    for sentence in sentences:
        raw_text = sentence.metadata.get("text", "")

        # extract VMWEs
        # ID => {type: "VID", tokens: [word1, word2]}
        mwe_map = {}

        for token in sentence:
            label = token.get("parseme:mwe")

            if label and label != "*":
                parts = label.split(";")

                for part in parts:
                    if ":" in part:
                        mwe_id, mwe_type = part.split(":")

                        if mwe_id not in mwe_map:
                            mwe_map[mwe_id] = {"type": mwe_type, "tokens": []}

                    else:
                        mwe_id = part

                    mwe_map[mwe_id]["tokens"].append(
                        {
                            "text": token["form"],
                            "lemma": token["lemma"],
                            "index": token["id"],
                            "pos": token["upos"],
                        }
                    )

        data.append({"sentence": raw_text, "mwes": list(mwe_map.values())})
    return data


def export_to_jsonl(data, output_path):
    """Saves the processed list to a JSONL file for LLM use."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as f:
        for entry in data:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
