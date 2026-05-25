# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Thực hành 4 - Phần 1 - Bài 4: liệt kê số xuất hiện nhiều nhất trong mảng."""

from collections import Counter
import sys


sys.stdout.reconfigure(encoding="utf-8")


def cac_so_xuat_hien_nhieu_nhat(mang: list[int]) -> tuple[list[int], int]:
    if not mang:
        raise ValueError("Mảng không được rỗng.")
    dem = Counter(mang)
    so_lan_nhieu_nhat = max(dem.values())
    cac_so = [gia_tri for gia_tri in dict.fromkeys(mang) if dem[gia_tri] == so_lan_nhieu_nhat]
    return cac_so, so_lan_nhieu_nhat


def main() -> None:
    try:
        mang = [int(so) for so in input("Nhập mảng số nguyên: ").split()]
        cac_so, so_lan = cac_so_xuat_hien_nhieu_nhat(mang)
    except ValueError as loi:
        print(f"Lỗi: {loi}")
        return

    print(f"Các số xuất hiện nhiều nhất: {cac_so}")
    print(f"Số lần xuất hiện: {so_lan}")


if __name__ == "__main__":
    main()
