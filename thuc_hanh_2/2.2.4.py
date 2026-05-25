"""Bài thực hành 2 - Phần 2 - Bài 4: tìm UCLN và BCNN."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def tim_ucln(so_thu_nhat: int, so_thu_hai: int) -> int:
    so_thu_nhat = abs(so_thu_nhat)
    so_thu_hai = abs(so_thu_hai)
    while so_thu_hai != 0:
        so_thu_nhat, so_thu_hai = so_thu_hai, so_thu_nhat % so_thu_hai
    return so_thu_nhat


def tim_bcnn(so_thu_nhat: int, so_thu_hai: int) -> int:
    if so_thu_nhat == 0 or so_thu_hai == 0:
        return 0
    return abs(so_thu_nhat // tim_ucln(so_thu_nhat, so_thu_hai) * so_thu_hai)


def main() -> None:
    try:
        so_thu_nhat = int(input("Nhập số nguyên thứ nhất: "))
        so_thu_hai = int(input("Nhập số nguyên thứ hai: "))
    except ValueError:
        print("Dữ liệu nhập vào phải là số nguyên.")
        return

    if so_thu_nhat == 0 and so_thu_hai == 0:
        print("UCLN và BCNN của 0 và 0 không xác định.")
        return

    print(f"UCLN = {tim_ucln(so_thu_nhat, so_thu_hai)}")
    print(f"BCNN = {tim_bcnn(so_thu_nhat, so_thu_hai)}")


if __name__ == "__main__":
    main()
