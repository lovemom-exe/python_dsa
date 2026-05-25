"""Bài thực hành 2 - Phần 2 - Bài 2: kiểm tra số nguyên tố."""

import sys
from math import isqrt


sys.stdout.reconfigure(encoding="utf-8")


def la_so_nguyen_to(so: int) -> bool:
    if so < 2:
        return False

    for uoc in range(2, isqrt(so) + 1):
        if so % uoc == 0:
            return False
    return True


def main() -> None:
    try:
        so = int(input("Nhập một số nguyên: "))
    except ValueError:
        print("Dữ liệu nhập vào không phải số nguyên.")
        return

    if la_so_nguyen_to(so):
        print(f"{so} là số nguyên tố.")
    else:
        print(f"{so} không phải là số nguyên tố.")


if __name__ == "__main__":
    main()
