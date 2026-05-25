# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 2 - Phần 2 - Bài 3: in cây theo lựa chọn."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def ve_cay_thong(chieu_cao: int) -> None:
    for tang in range(1, chieu_cao + 1):
        print(" " * (chieu_cao - tang) + "*" * (2 * tang - 1))
    print(" " * (chieu_cao - 1) + "|")


def ve_cay_lech_trai(chieu_cao: int) -> None:
    for tang in range(1, chieu_cao + 1):
        print("*" * tang)


def ve_cay_lech_phai(chieu_cao: int) -> None:
    for tang in range(1, chieu_cao + 1):
        print(" " * (chieu_cao - tang) + "*" * tang)


CAC_LOAI_CAY = {
    "1": ("Cây thông", ve_cay_thong),
    "2": ("Cây lệch trái", ve_cay_lech_trai),
    "3": ("Cây lệch phải", ve_cay_lech_phai),
}


def main() -> None:
    print("1. Cây thông")
    print("2. Cây lệch trái")
    print("3. Cây lệch phải")
    lua_chon = input("Chọn loại cây: ").strip()

    if lua_chon not in CAC_LOAI_CAY:
        print("Lựa chọn không hợp lệ.")
        return

    try:
        chieu_cao = int(input("Nhập chiều cao cây: "))
    except ValueError:
        print("Chiều cao phải là số nguyên.")
        return

    if chieu_cao <= 0:
        print("Chiều cao phải lớn hơn 0.")
        return

    ten_cay, ham_ve = CAC_LOAI_CAY[lua_chon]
    print(f"\n{ten_cay}:")
    ham_ve(chieu_cao)


if __name__ == "__main__":
    main()
