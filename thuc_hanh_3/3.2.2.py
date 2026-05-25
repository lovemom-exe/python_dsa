# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Thực hành 3 - Tráo đổi hai giá trị qua tham chiếu khả biến."""

from dataclasses import dataclass
import sys


sys.stdout.reconfigure(encoding="utf-8")


@dataclass
class ThamChieuSo:
    gia_tri: float


def trao_doi(so_thu_nhat: ThamChieuSo, so_thu_hai: ThamChieuSo) -> None:
    so_thu_nhat.gia_tri, so_thu_hai.gia_tri = so_thu_hai.gia_tri, so_thu_nhat.gia_tri


def main() -> None:
    try:
        so_thu_nhat = ThamChieuSo(float(input("Nhập số thứ nhất: ")))
        so_thu_hai = ThamChieuSo(float(input("Nhập số thứ hai: ")))
    except ValueError:
        print("Dữ liệu nhập vào phải là số.")
        return

    print(f"Trước khi tráo đổi: a = {so_thu_nhat.gia_tri:g}, b = {so_thu_hai.gia_tri:g}")
    trao_doi(so_thu_nhat, so_thu_hai)
    print(f"Sau khi tráo đổi:   a = {so_thu_nhat.gia_tri:g}, b = {so_thu_hai.gia_tri:g}")


if __name__ == "__main__":
    main()
