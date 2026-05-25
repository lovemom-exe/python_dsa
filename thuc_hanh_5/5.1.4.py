# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 5 - Phần 1 - Bài 4: Counting sort."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def counting_sort(mang: list[int]) -> list[int]:
    if not mang:
        return []

    gia_tri_nho_nhat = min(mang)
    gia_tri_lon_nhat = max(mang)
    khoang_gia_tri = gia_tri_lon_nhat - gia_tri_nho_nhat + 1
    if khoang_gia_tri > 1_000_000:
        raise ValueError("Khoảng giá trị quá lớn để sử dụng counting sort.")

    so_lan_xuat_hien = [0] * khoang_gia_tri
    for gia_tri in mang:
        so_lan_xuat_hien[gia_tri - gia_tri_nho_nhat] += 1

    ket_qua: list[int] = []
    for vi_tri, so_lan in enumerate(so_lan_xuat_hien):
        ket_qua.extend([vi_tri + gia_tri_nho_nhat] * so_lan)
    return ket_qua


def main() -> None:
    try:
        mang = [int(so) for so in input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()]
        print(f"Counting sort: {counting_sort(mang)}")
    except ValueError as loi:
        print(f"Lỗi: {loi}")


if __name__ == "__main__":
    main()
