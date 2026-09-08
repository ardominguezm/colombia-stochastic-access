import ast
import json
from pathlib import Path


def test_notebook_code_cells_are_syntactically_valid():
    notebook = json.loads(
        Path("notebooks/00_data_audit_and_pilot.ipynb").read_text(encoding="utf-8")
    )
    for index, cell in enumerate(notebook["cells"]):
        if cell.get("cell_type") != "code":
            continue
        source = "".join(cell.get("source", []))
        if source.lstrip().startswith(("%", "!")):
            continue
        try:
            ast.parse(source)
        except SyntaxError as exc:
            raise AssertionError(f"Invalid Python in notebook cell {index}: {exc}") from exc
