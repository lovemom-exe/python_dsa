# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Thực hành 4 - Duyệt mảng số nguyên và in theo thứ tự đảo ngược."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def dao_nguoc_bang_cach_duyet(mang: list[int]) -> list[int]:
    ket_qua: list[int] = []
    vi_tri = len(mang) - 1
    while vi_tri >= 0:
        ket_qua.append(mang[vi_tri])
        vi_tri -= 1
    return ket_qua


def main() -> None:
    try:
        mang = [int(so) for so in input("Nhập mảng số nguyên: ").split()]
    except ValueError:
        print("Dữ liệu nhập vào phải là số nguyên.")
        return

    print(f"Mảng theo thứ tự đảo ngược: {dao_nguoc_bang_cach_duyet(mang)}")


if __name__ == "__main__":
    main()
