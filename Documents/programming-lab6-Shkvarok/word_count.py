#!/usr/bin/env python3
# word_count.py
# Програма "Рахунок слів" — рахує кількість слів у введеному користувачем тексті.

import re
import sys

# Патерн ловить слова, що складаються з літер (латиниця та кирилиця) або цифр,
# допускає внутрішні апострофи або дефіси (наприклад: п'ять, state-of-the-art).
WORD_RE = re.compile(
    r"[A-Za-z0-9А-Яа-яЁёЇїІіЄєҐґ]+(?:[-'][A-Za-z0-9А-Яа-яЁёЇїІіЄєҐґ]+)*",
    flags=re.UNICODE
)

def count_words(text: str) -> int:
    """Повертає кількість слів у тексті."""
    return len(WORD_RE.findall(text))

def main():
    # Якщо текст передали через стандартний ввід (pipe або файл), читаємо все:
    if not sys.stdin.isatty():
        text = sys.stdin.read()
        n = count_words(text)
        print(f"Кількість слів: {n}")
        return

    # Інтерактивний режим: читаємо кілька рядків від користувача.
    print("Введіть текст (щоб завершити, введіть порожній рядок або натисніть Ctrl+D / Ctrl+Z):")
    lines = []
    try:
        while True:
            line = input()
            if line == "":
                # порожній рядок — закінчити введення
                break
            lines.append(line)
    except EOFError:
        # користувач натиснув Ctrl+D (Unix) або Ctrl+Z (Windows)
        pass

    text = "\n".join(lines)
    n = count_words(text)
    print(f"\nКількість слів: {n}")

if __name__ == "__main__":
    main()
