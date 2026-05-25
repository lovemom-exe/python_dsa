# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Thực hành 4 - Phần 1 - Bài 2: tìm kiếm nhị phân trên mảng đã sắp xếp."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def tim_kiem_nhi_phan(mang: list[int], gia_tri: int) -> int | None:
    trai = 0
    phai = len(mang) - 1
    while trai <= phai:
        giua = (trai + phai) // 2
        if mang[giua] == gia_tri:
            return giua
        if mang[giua] < gia_tri:
            trai = giua + 1
        else:
            phai = giua - 1
    return None


def main() -> None:
    try:
        mang = [int(so) for so in input("Nhập mảng đã sắp xếp tăng dần: ").split()]
        gia_tri = int(input("Nhập giá trị cần tìm: "))
    except ValueError:
        print("Dữ liệu nhập vào phải là số nguyên.")
        return

    if mang != sorted(mang):
        print("Mảng chưa được sắp xếp tăng dần, không thể tìm kiếm nhị phân.")
        return

    vi_tri = tim_kiem_nhi_phan(mang, gia_tri)
    if vi_tri is None:
        print(f"Không tìm thấy {gia_tri} trong mảng.")
    else:
        print(f"Tìm thấy {gia_tri} tại vị trí {vi_tri + 1}.")


if __name__ == "__main__":
    main()
