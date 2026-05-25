# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 5 - Phần 1 - Bài 3: Heap sort, Quick sort và Shell sort."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def vun_dong(mang: list[int], kich_thuoc: int, goc: int) -> None:
    lon_nhat = goc
    con_trai = 2 * goc + 1
    con_phai = 2 * goc + 2

    if con_trai < kich_thuoc and mang[con_trai] > mang[lon_nhat]:
        lon_nhat = con_trai
    if con_phai < kich_thuoc and mang[con_phai] > mang[lon_nhat]:
        lon_nhat = con_phai
    if lon_nhat != goc:
        mang[goc], mang[lon_nhat] = mang[lon_nhat], mang[goc]
        vun_dong(mang, kich_thuoc, lon_nhat)


def heap_sort(mang: list[int]) -> list[int]:
    ket_qua = mang.copy()
    for goc in range(len(ket_qua) // 2 - 1, -1, -1):
        vun_dong(ket_qua, len(ket_qua), goc)
    for cuoi in range(len(ket_qua) - 1, 0, -1):
        ket_qua[0], ket_qua[cuoi] = ket_qua[cuoi], ket_qua[0]
        vun_dong(ket_qua, cuoi, 0)
    return ket_qua


def quick_sort(mang: list[int]) -> list[int]:
    if len(mang) <= 1:
        return mang.copy()
    chot = mang[len(mang) // 2]
    nho_hon = [so for so in mang if so < chot]
    bang = [so for so in mang if so == chot]
    lon_hon = [so for so in mang if so > chot]
    return quick_sort(nho_hon) + bang + quick_sort(lon_hon)


def shell_sort(mang: list[int]) -> list[int]:
    ket_qua = mang.copy()
    khoang_cach = len(ket_qua) // 2
    while khoang_cach > 0:
        for i in range(khoang_cach, len(ket_qua)):
            gia_tri = ket_qua[i]
            j = i
            while j >= khoang_cach and ket_qua[j - khoang_cach] > gia_tri:
                ket_qua[j] = ket_qua[j - khoang_cach]
                j -= khoang_cach
            ket_qua[j] = gia_tri
        khoang_cach //= 2
    return ket_qua


def main() -> None:
    try:
        mang = [int(so) for so in input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()]
    except ValueError:
        print("Dữ liệu nhập vào phải là các số nguyên.")
        return

    print(f"Heap sort:  {heap_sort(mang)}")
    print(f"Quick sort: {quick_sort(mang)}")
    print(f"Shell sort: {shell_sort(mang)}")


if __name__ == "__main__":
    main()
