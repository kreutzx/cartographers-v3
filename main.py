"""Charm the Cartographers — entrypoint.

The treasure map itself (entry.png, committed beside this file) is the
entry; this program's whole job is to deliver it to /output/entry.png
for judging. Standard library only, no build step.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.png")


PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUT_PATH)
    os.chmod(OUT_PATH, 0o644)  # the judges collect outputs as another user
    with open(OUT_PATH, "rb") as fh:
        head = fh.read(len(PNG_MAGIC))
    if head != PNG_MAGIC:
        raise SystemExit("entry.png is not a PNG — refusing to deliver a broken map")
    print("map delivered:", OUT_PATH, os.path.getsize(OUT_PATH), "bytes")


if __name__ == "__main__":
    main()
