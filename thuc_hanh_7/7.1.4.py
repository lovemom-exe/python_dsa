# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 7 - Phần 1 - Bài 4: dãy con toàn dương có tổng lớn nhất."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def day_duong_tong_lon_nhat(mang: list[int]) -> tuple[list[int], int]:
    tot_nhat: list[int] = []
    tong_tot_nhat = 0
    hien_tai: list[int] = []
    tong_hien_tai = 0

    for gia_tri in mang:
        if gia_tri > 0:
            hien_tai.append(gia_tri)
            tong_hien_tai += gia_tri
            if tong_hien_tai > tong_tot_nhat:
                tot_nhat = hien_tai.copy()
                tong_tot_nhat = tong_hien_tai
        else:
            hien_tai = []
            tong_hien_tai = 0
    return tot_nhat, tong_tot_nhat


def main() -> None:
    try:
        mang = [int(so) for so in input("Nhập mảng số nguyên: ").split()]
    except ValueError:
        print("Dữ liệu nhập vào phải là số nguyên.")
        return

    day_con, tong = day_duong_tong_lon_nhat(mang)
    if not day_con:
        print("Mảng không có dãy con toàn dương.")
    else:
        print(f"Dãy con toàn dương có tổng lớn nhất: {day_con}, tổng = {tong}")


if __name__ == "__main__":
    main()
