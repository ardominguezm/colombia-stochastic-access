import ast
import json
from pathlib import Path


def test_all_notebook_code_cells_are_syntactically_valid():
    notebooks = sorted(Path("notebooks").glob("*.ipynb"))
    assert notebooks, "No notebooks found"

    for notebook_path in notebooks:
        notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
        for index, cell in enumerate(notebook["cells"]):
            if cell.get("cell_type") != "code":
                continue
            source = "".join(cell.get("source", []))
            if source.lstrip().startswith(("%", "!")):
                continue
            try:
                ast.parse(source)
            except SyntaxError as exc:
                raise AssertionError(
                    f"Invalid Python in {notebook_path}, cell {index}: {exc}"
                ) from exc
