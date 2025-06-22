import os
import ast

# Optional filters
EXCLUDE_DUNDER = True      # ⛔ Exclude __init__, __str__, etc.
ONLY_CUSTOM = False        # ⛔ Ignore Django built-in files like admin.py, apps.py, migrations/

# Set your base directory (current working directory)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Files/folders to skip
SKIP_FILES = ['__init__.py', 'settings.py', 'wsgi.py', 'asgi.py', 'manage.py']
SKIP_DIRS = ['venv', 'env', 'migrations', '__pycache__']

function_data = []

for root, dirs, files in os.walk(BASE_DIR):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

    for file in files:
        if file.endswith('.py') and file not in SKIP_FILES:
            full_path = os.path.join(root, file)

            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    node = ast.parse(f.read(), filename=full_path)
                    functions = [n.name for n in ast.walk(node) if isinstance(n, ast.FunctionDef)]

                    if EXCLUDE_DUNDER:
                        functions = [fn for fn in functions if not fn.startswith('__')]

                    if functions:
                        rel_path = os.path.relpath(full_path, BASE_DIR)
                        function_data.append((rel_path, functions))

            except Exception as e:
                print(f"⚠️ Skipped {file} due to error: {e}")

# ✅ Output result
print("\n🔍 Function Report")
print("=" * 50)

total = 0
for file, funcs in function_data:
    print(f"\n📄 {file}")
    for func in funcs:
        print(f"   - def {func}()")
        total += 1

print("\n🧮 Total functions found:", total)
