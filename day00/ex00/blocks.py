from sys import argv
from typing import Any, Callable


def _validate_args(args: list[str]) -> int:
    if len(args) > 1:
        raise ValueError("Too many arguments. Expected 1")
    nbr: str = (args[0]).strip() if args else "0"
    if not nbr.isdigit():
        raise TypeError(f"The {nbr} is not digits-only.")
    return int(nbr)


def _validate_hash(hash_: str) -> bool:
    if (len(hash_) == 32) and hash_.startswith("00000") and hash_[5] != "0":
        return True
    return False


def main(
    num_of_lines: int, hash_valid: Callable[[str], Any] = _validate_hash
):
    try:
        for _ in range(num_of_lines):
            hash_ = input()
            if hash_valid(hash_):
                print(hash_)
    except EOFError:
        pass


if __name__ == "__main__":
    try:
        nlines = _validate_args(argv[1:])
        main(nlines)
    except Exception as err:
        print(f"Error: {err}")