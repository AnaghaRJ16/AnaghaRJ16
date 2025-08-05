from datetime import datetime

with open("README.md", "a") as f:
    f.write(f"\n\nLast updated automatically on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
