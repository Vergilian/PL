import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
TESTS_PATH = BASE_DIR / "tests.json"
VALUES_PATH = BASE_DIR / "values.json"
REPORT_PATH = BASE_DIR / "report.json"


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


values = load_json(VALUES_PATH)
tests = load_json(TESTS_PATH)

values_map = {entry["id"]: entry["value"] for entry in values["values"]}

fill_values(tests["tests"], values_map)

save_json(REPORT_PATH, tests)
