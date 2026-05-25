# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 8 - Phần 3: cây nhị phân tìm kiếm."""

from dataclasses import dataclass
import sys


sys.stdout.reconfigure(encoding="utf-8")


@dataclass
class Nut:
    gia_tri: int
    trai: "Nut | None" = None
    phai: "Nut | None" = None


class CayNhiPhanTimKiem:
    def __init__(self) -> None:
        self.goc: Nut | None = None

    def them(self, gia_tri: int) -> None:
        def them_vao(nut: Nut | None) -> Nut:
            if nut is None:
                return Nut(gia_tri)
            if gia_tri < nut.gia_tri:
                nut.trai = them_vao(nut.trai)
            elif gia_tri > nut.gia_tri:
                nut.phai = them_vao(nut.phai)
            return nut

        self.goc = them_vao(self.goc)

    def ton_tai(self, gia_tri: int) -> bool:
        nut = self.goc
        while nut:
            if gia_tri == nut.gia_tri:
                return True
            nut = nut.trai if gia_tri < nut.gia_tri else nut.phai
        return False

    def xoa(self, gia_tri: int) -> None:
        def xoa_khoi(nut: Nut | None) -> Nut | None:
            if nut is None:
                return None
            if gia_tri < nut.gia_tri:
                nut.trai = xoa_khoi(nut.trai)
            elif gia_tri > nut.gia_tri:
                nut.phai = xoa_khoi(nut.phai)
            elif nut.trai is None:
                return nut.phai
            elif nut.phai is None:
                return nut.trai
            else:
                ke_tiep = nut.phai
                while ke_tiep.trai:
                    ke_tiep = ke_tiep.trai
                nut.gia_tri = ke_tiep.gia_tri
                gia_tri_thay_the = ke_tiep.gia_tri

                def xoa_gia_tri_thay_the(nut_con: Nut | None) -> Nut | None:
                    if nut_con is None:
                        return None
                    if gia_tri_thay_the < nut_con.gia_tri:
                        nut_con.trai = xoa_gia_tri_thay_the(nut_con.trai)
                        return nut_con
                    return nut_con.phai

                nut.phai = xoa_gia_tri_thay_the(nut.phai)
            return nut

        self.goc = xoa_khoi(self.goc)

    def dem(self) -> int:
        def dem_tu(nut: Nut | None) -> int:
            return 0 if nut is None else 1 + dem_tu(nut.trai) + dem_tu(nut.phai)

        return dem_tu(self.goc)

    def duyet_tang_dan(self) -> list[int]:
        ket_qua: list[int] = []

        def duyet(nut: Nut | None) -> None:
            if nut:
                duyet(nut.trai)
                ket_qua.append(nut.gia_tri)
                duyet(nut.phai)

        duyet(self.goc)
        return ket_qua


def main() -> None:
    cay = CayNhiPhanTimKiem()
    while True:
        print(f"\nCây theo thứ tự tăng dần: {cay.duyet_tang_dan()}")
        print("1. Thêm   2. Xóa   3. Kiểm tra   4. Đếm phần tử   0. Thoát")
        lua_chon = input("Chọn chức năng: ").strip()
        try:
            if lua_chon == "1":
                cay.them(int(input("Giá trị cần thêm: ")))
            elif lua_chon == "2":
                cay.xoa(int(input("Giá trị cần xóa: ")))
            elif lua_chon == "3":
                gia_tri = int(input("Giá trị cần kiểm tra: "))
                print("Có trong cây." if cay.ton_tai(gia_tri) else "Không có trong cây.")
            elif lua_chon == "4":
                print(f"Số phần tử của cây = {cay.dem()}")
            elif lua_chon == "0":
                break
            else:
                print("Lựa chọn không hợp lệ.")
        except ValueError:
            print("Giá trị nhập vào phải là số nguyên.")


if __name__ == "__main__":
    main()
