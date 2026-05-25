# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Thực hành 4 - Phần 1 - Bài 3 (OPTION): tìm kiếm bằng bảng băm."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


class BangBam:
    def __init__(self, kich_thuoc: int = 11) -> None:
        self.cac_ngan: list[list[int]] = [[] for _ in range(kich_thuoc)]

    def _bam(self, gia_tri: int) -> int:
        return gia_tri % len(self.cac_ngan)

    def them(self, gia_tri: int) -> None:
        ngan = self.cac_ngan[self._bam(gia_tri)]
        if gia_tri not in ngan:
            ngan.append(gia_tri)

    def tim(self, gia_tri: int) -> bool:
        return gia_tri in self.cac_ngan[self._bam(gia_tri)]

    def hien_thi(self) -> None:
        for chi_so, ngan in enumerate(self.cac_ngan):
            if ngan:
                print(f"Ngăn {chi_so}: {ngan}")


def main() -> None:
    try:
        mang = [int(so) for so in input("Nhập mảng số nguyên: ").split()]
        gia_tri = int(input("Nhập giá trị cần tìm: "))
    except ValueError:
        print("Dữ liệu nhập vào phải là số nguyên.")
        return

    bang_bam = BangBam()
    for phan_tu in mang:
        bang_bam.them(phan_tu)
    print("Bảng băm đã tạo:")
    bang_bam.hien_thi()
    print(f"Tìm thấy {gia_tri} trong bảng băm." if bang_bam.tim(gia_tri) else f"Không tìm thấy {gia_tri}.")


if __name__ == "__main__":
    main()
