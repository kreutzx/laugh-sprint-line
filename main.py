import os

LINE = (
    "I bought a planner to get my life together, and it worked: "
    "now every plan I've ever abandoned is in one convenient place."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
