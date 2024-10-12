from re import match
from sys import stdin


def _read_ascii_image_from_stdin() -> list[str]:
    nlines: int = 1
    ascii_image: list[str] = []
    for line in stdin:
        if nlines > 3:
            raise ValueError(f"Wrong number of lines: ({nlines}), expected 3")
        line_ = line.strip()
        if len(line_) != 5:
            raise ValueError(f"Wrong length of line {nlines}: '{len(line_)}', expected 5")
        ascii_image.append(line_)
        nlines += 1
    if nlines < 3:
        raise ValueError(f"Wrong number of lines: ({nlines}), expected 3")    
    return ascii_image


def _has_m_letter(image: list[str]) -> bool:     
    if (
        match(r"^\*[^*]{3}\*$", image[0])
        and match(r"^\*{2}[^*]\*{2}$", image[1])
        and match(r"^\*[^*]\*[^*]\*$", image[2])
    ):
        return True
    return False


def main() -> None:
    img: list[str] = _read_ascii_image_from_stdin()
    print(_has_m_letter(img))


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"Error: {err}")