import os

LINE = "I bought a planner to get my life together, and it worked: now every plan I've ever abandoned is in one convenient place."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
