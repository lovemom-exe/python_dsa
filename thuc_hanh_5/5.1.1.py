# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 5 - Phần 1 - Bài 1: các thuật toán sắp xếp cơ bản."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def insertion_sort(mang: list[int]) -> list[int]:
    ket_qua = mang.copy()
    for i in range(1, len(ket_qua)):
        gia_tri = ket_qua[i]
        j = i - 1
        while j >= 0 and ket_qua[j] > gia_tri:
            ket_qua[j + 1] = ket_qua[j]
            j -= 1
        ket_qua[j + 1] = gia_tri
    return ket_qua


def selection_sort(mang: list[int]) -> list[int]:
    ket_qua = mang.copy()
    for i in range(len(ket_qua) - 1):
        vi_tri_nho_nhat = i
        for j in range(i + 1, len(ket_qua)):
            if ket_qua[j] < ket_qua[vi_tri_nho_nhat]:
                vi_tri_nho_nhat = j
        ket_qua[i], ket_qua[vi_tri_nho_nhat] = ket_qua[vi_tri_nho_nhat], ket_qua[i]
    return ket_qua


def bubble_sort(mang: list[int]) -> list[int]:
    ket_qua = mang.copy()
    for luot in range(len(ket_qua) - 1):
        da_doi_cho = False
        for j in range(len(ket_qua) - 1 - luot):
            if ket_qua[j] > ket_qua[j + 1]:
                ket_qua[j], ket_qua[j + 1] = ket_qua[j + 1], ket_qua[j]
                da_doi_cho = True
        if not da_doi_cho:
            break
    return ket_qua


def main() -> None:
    try:
        mang = [int(so) for so in input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()]
    except ValueError:
        print("Dữ liệu nhập vào phải là các số nguyên.")
        return

    print(f"Insertion sort: {insertion_sort(mang)}")
    print(f"Selection sort: {selection_sort(mang)}")
    print(f"Bubble sort:    {bubble_sort(mang)}")


if __name__ == "__main__":
    main()
