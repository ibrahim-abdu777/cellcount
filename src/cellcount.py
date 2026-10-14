"""Count table-like rows in text."""


def count_rows(lines, sep="|"):
    return sum(1 for line in lines if line.count(sep) >= 1)


def count_file(path, sep="|"):
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        return count_rows(handle, sep)
