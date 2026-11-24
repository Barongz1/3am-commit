"""The 3 AM Commit Message — entry for make.fun.

Writes one line to /output/entry.txt. The line is the funniest commit message an AI agent writes after breaking production at 3 AM, at most 200 characters.
"""
import os

LINE = "fix: it worked on my machine at 3 AM, which is the same machine that just took production down"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
