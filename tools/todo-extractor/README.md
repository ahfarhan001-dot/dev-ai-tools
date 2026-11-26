# todo-extractor

Scan a codebase for `TODO`, `FIXME`, and `HACK` comments and print one tidy report, grouped by file.

## Usage

```bash
# Scan the current directory
python3 todo_extractor.py

# Scan a specific project
python3 todo_extractor.py /path/to/your/project

# Look for different tags
python3 todo_extractor.py /path/to/your/project --tags TODO,NOTE
```

Requires Python 3.8 or newer. No extra packages.

## Example output

```
Found 3 note(s) under ./myproject:

myproject/app.py
  line 42: [TODO] handle empty cart before checkout
  line 87: [FIXME] retry fails silently when the network drops
myproject/utils.py
  line 12: [HACK] hardcoded for demo, replace with config
```

## Notes

- Hidden folders (`.git`, `node_modules`, `__pycache__`, `.venv`, `dist`, `build`) are skipped automatically.
- Only common code and text files are scanned.
