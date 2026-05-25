# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Thực hành 4 - Phần 1 - Bài 1: tìm giá trị, giá trị nhỏ nhất và lớn nhất."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def tim_vi_tri(mang: list[int], gia_tri: int) -> list[int]:
    return [vi_tri for vi_tri, phan_tu in enumerate(mang, start=1) if phan_tu == gia_tri]


def tim_min_max(mang: list[int]) -> tuple[int, int]:
    if not mang:
        raise ValueError("Mảng không được rỗng.")
    nho_nhat = lon_nhat = mang[0]
    for phan_tu in mang[1:]:
        if phan_tu < nho_nhat:
            nho_nhat = phan_tu
        if phan_tu > lon_nhat:
            lon_nhat = phan_tu
    return nho_nhat, lon_nhat


def main() -> None:
    try:
        mang = [int(so) for so in input("Nhập mảng số nguyên: ").split()]
        gia_tri = int(input("Nhập giá trị cần tìm: "))
        nho_nhat, lon_nhat = tim_min_max(mang)
    except ValueError as loi:
        print(f"Lỗi: {loi}")
        return

    vi_tri = tim_vi_tri(mang, gia_tri)
    if vi_tri:
        print(f"Tìm thấy {gia_tri} tại vị trí: {vi_tri}")
    else:
        print(f"Không tìm thấy {gia_tri} trong mảng.")
    print(f"Giá trị nhỏ nhất = {nho_nhat}")
    print(f"Giá trị lớn nhất = {lon_nhat}")


if __name__ == "__main__":
    main()
