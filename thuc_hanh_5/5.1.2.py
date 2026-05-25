# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 5 - Phần 1 - Bài 2: sắp xếp trộn (merge sort)."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def tron_mang(trai: list[int], phai: list[int]) -> list[int]:
    ket_qua: list[int] = []
    i = j = 0
    while i < len(trai) and j < len(phai):
        if trai[i] <= phai[j]:
            ket_qua.append(trai[i])
            i += 1
        else:
            ket_qua.append(phai[j])
            j += 1
    return ket_qua + trai[i:] + phai[j:]


def merge_sort(mang: list[int]) -> list[int]:
    if len(mang) <= 1:
        return mang.copy()

    giua = len(mang) // 2
    trai = merge_sort(mang[:giua])
    phai = merge_sort(mang[giua:])
    return tron_mang(trai, phai)


def main() -> None:
    try:
        mang = [int(so) for so in input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()]
    except ValueError:
        print("Dữ liệu nhập vào phải là các số nguyên.")
        return

    print(f"Mảng sau khi sắp xếp: {merge_sort(mang)}")


if __name__ == "__main__":
    main()
