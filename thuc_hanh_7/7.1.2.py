# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 7 - Phần 1 - Bài 2: xóa phần tử trùng trong mảng."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def xoa_trung(mang: list[int]) -> list[int]:
    da_gap: set[int] = set()
    ket_qua: list[int] = []
    for phan_tu in mang:
        if phan_tu not in da_gap:
            ket_qua.append(phan_tu)
            da_gap.add(phan_tu)
    return ket_qua


def main() -> None:
    try:
        mang = [int(so) for so in input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()]
    except ValueError:
        print("Dữ liệu nhập vào phải là các số nguyên.")
        return
    print(f"Mảng sau khi xóa trùng: {xoa_trung(mang)}")


if __name__ == "__main__":
    main()
