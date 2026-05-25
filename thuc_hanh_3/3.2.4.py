# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Thực hành 3 - Tìm độ dài chuỗi bằng cách duyệt từng ký tự."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def tinh_do_dai(chuoi: str) -> int:
    do_dai = 0
    for _ in chuoi:
        do_dai += 1
    return do_dai


def main() -> None:
    chuoi = input("Nhập chuỗi cần tính độ dài: ")
    print(f"Độ dài chuỗi = {tinh_do_dai(chuoi)}")


if __name__ == "__main__":
    main()
