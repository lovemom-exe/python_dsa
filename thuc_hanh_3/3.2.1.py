# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Thực hành 3 - Cộng hai số qua tham chiếu khả biến trong Python."""

from dataclasses import dataclass
import sys


sys.stdout.reconfigure(encoding="utf-8")


@dataclass
class ThamChieuSo:
    gia_tri: float = 0


def cong_hai_so(so_thu_nhat: ThamChieuSo, so_thu_hai: ThamChieuSo, ket_qua: ThamChieuSo) -> None:
    ket_qua.gia_tri = so_thu_nhat.gia_tri + so_thu_hai.gia_tri


def main() -> None:
    try:
        so_thu_nhat = ThamChieuSo(float(input("Nhập số thứ nhất: ")))
        so_thu_hai = ThamChieuSo(float(input("Nhập số thứ hai: ")))
    except ValueError:
        print("Dữ liệu nhập vào phải là số.")
        return

    ket_qua = ThamChieuSo()
    cong_hai_so(so_thu_nhat, so_thu_hai, ket_qua)
    print(f"Tổng hai số = {ket_qua.gia_tri:g}")


if __name__ == "__main__":
    main()
