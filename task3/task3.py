import json
from pathlib import Path
import sys


def load_json(path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def fill_values(node, values_map):
    if isinstance(node, dict):
        node_id = node.get("id")
        if node_id in values_map:
            node["value"] = values_map[node_id]

        if "values" in node:
            for inside in node["values"]:
                fill_values(inside, values_map)
    elif isinstance(node, list):
        for item in node:
            fill_values(item, values_map)


if len(sys.argv) < 4:
    print('Для использования: python task3.py <tests_path> <values_path> <report_path>')
    sys.exit(1)

tests_path = Path(sys.argv[1])
values_path = Path(sys.argv[2])
report_path = Path(sys.argv[3])

values = load_json(values_path)
tests = load_json(tests_path)

values_map = {entry["id"]: entry["value"] for entry in values["values"]}

fill_values(tests["tests"], values_map)

save_json(report_path, tests)
