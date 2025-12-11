# test.py
import sys

if len(sys.argv) >= 3:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
else:
    # fallback defaults
    a = 0.0
    b = 0.0

print("Sum:", a + b)
