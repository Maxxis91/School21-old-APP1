from sys import argv


def main(strings: list[str]):
    for string in strings:
        answer = "".join([word[0] for word in string.split()])
    print(answer)


if __name__ == "__main__":
    try:
        main(argv[1:])
    except Exception as err:
        print(f"Error: {err}")