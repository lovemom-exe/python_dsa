# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Thực hành 3 - Tính tổng các phần tử khi duyệt lần lượt qua mảng."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def tinh_tong_qua_tham_chieu(mang: list[float]) -> float:
    tong = 0.0
    vi_tri = 0
    while vi_tri < len(mang):
        tong += mang[vi_tri]
        vi_tri += 1
    return tong


def main() -> None:
    try:
        mang = [float(so) for so in input("Nhập các phần tử của mảng: ").split()]
    except ValueError:
        print("Dữ liệu nhập vào phải là số.")
        return

    print(f"Tổng các phần tử = {tinh_tong_qua_tham_chieu(mang):g}")


if __name__ == "__main__":
    main()
