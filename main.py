"""The Battery's Last Text to Its Charger — a make.fun entry.

Prints exactly one line of plain text of at most 200 characters: the
phone battery's last text message to the charger it waited for.
"""

LINE = (
    "If I don't make it to the charger, tell the 1% I loved being "
    "the reason you panicked at brunch every Sunday. — your battery, at 2%"
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 200, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
