import json
from pathlib import Path
import re
from typing import Literal, Optional
from fire import Fire

def main(
    workspace: str
):
    workspace = Path(workspace)
    playground = workspace / "playground"
    for subfolder in sorted(playground.iterdir(), key=lambda p: p.stat().st_mtime):
        if not subfolder.is_dir():
            continue

        instance_path = subfolder / "instance.json"
        result_path = subfolder / "result.json"

        if not instance_path.exists():
            continue

        result = {}
        if result_path.exists():
            result_str = result_path.read_text(encoding="utf-8")
            if result_str.strip():
                result = json.loads(result_str)
        
        if result.get("organize_completed",False) and not result["test_status"]:
            print(result["instance_id"], result["test_status"])
            result["organize_completed"] = False
            result["exception"] = ""


        #with open(result_path, "w") as f:
        #    json.dump(result, f, indent = True)

if __name__ == "__main__":
    Fire(main)