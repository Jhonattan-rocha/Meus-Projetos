import subprocess
import sys

result = subprocess.run(
    [sys.executable, f"InitProcess.java {'notepad'}"], capture_output=True, text=True
)
print(result)
