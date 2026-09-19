import json
from pathlib import Path


root = Path(input("请输入要格式化的目录: ").strip())

if not root.is_dir():
    print(f"目录不存在: {root}")
    raise SystemExit(1)

for path in root.rglob("*.json"):
    try:
        with path.open("r", encoding="utf-8-sig") as f:
            data = json.load(f)

        with path.open("w", encoding="utf-8", newline="\n") as f:
            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=2,
                separators=(",", ": ")
            )
            f.write("\n")

        print(f"formatted: {path}")

    except json.JSONDecodeError as e:
        print(f"invalid json: {path} ({e})")
    except Exception as e:
        print(f"failed: {path} ({e})")

print("完成")