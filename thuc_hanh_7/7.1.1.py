# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 7 - Phần 1 - Bài 1: khoảng cách trung bình trong mảng."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def khoang_cach_trung_binh(mang: list[float]) -> float:
    if len(mang) < 2:
        raise ValueError("Mảng phải có ít nhất hai phần tử.")
    tong = sum(abs(mang[i] - mang[i - 1]) for i in range(1, len(mang)))
    return tong / (len(mang) - 1)


def main() -> None:
    try:
        mang = [float(so) for so in input("Nhập các số, cách nhau bởi dấu cách: ").split()]
        print(f"Khoảng cách trung bình giữa các phần tử liên tiếp = {khoang_cach_trung_binh(mang):g}")
    except ValueError as loi:
        print(f"Lỗi: {loi}")


if __name__ == "__main__":
    main()
