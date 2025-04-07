import platform

operating_system = platform.system()

# Find Operating System

if operating_system == "Darwin":
    exec(open("macOS.py").read())
else:
    exec(open("win-lin.py").read())