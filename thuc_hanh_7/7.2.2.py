# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 7 - Phần 2 - Bài 2: danh sách liên kết đơn quản lý sinh viên."""

from dataclasses import dataclass
import sys


sys.stdout.reconfigure(encoding="utf-8")


@dataclass
class SinhVien:
    mssv: str
    ho_ten: str
    hoc_phan: str
    diem: float


@dataclass
class Nut:
    du_lieu: SinhVien
    tiep_theo: "Nut | None" = None


class DanhSachLienKet:
    def __init__(self) -> None:
        self.dau: Nut | None = None

    def tim(self, mssv: str) -> SinhVien | None:
        hien_tai = self.dau
        while hien_tai:
            if hien_tai.du_lieu.mssv == mssv:
                return hien_tai.du_lieu
            hien_tai = hien_tai.tiep_theo
        return None

    def them(self, sinh_vien: SinhVien) -> None:
        if self.tim(sinh_vien.mssv):
            raise ValueError("MSSV đã tồn tại.")
        nut_moi = Nut(sinh_vien)
        if self.dau is None:
            self.dau = nut_moi
            return
        hien_tai = self.dau
        while hien_tai.tiep_theo:
            hien_tai = hien_tai.tiep_theo
        hien_tai.tiep_theo = nut_moi

    def xoa(self, mssv: str) -> bool:
        truoc: Nut | None = None
        hien_tai = self.dau
        while hien_tai:
            if hien_tai.du_lieu.mssv == mssv:
                if truoc is None:
                    self.dau = hien_tai.tiep_theo
                else:
                    truoc.tiep_theo = hien_tai.tiep_theo
                return True
            truoc, hien_tai = hien_tai, hien_tai.tiep_theo
        return False

    def hien_thi(self) -> None:
        hien_tai = self.dau
        if hien_tai is None:
            print("Danh sách rỗng.")
        while hien_tai:
            sv = hien_tai.du_lieu
            print(f"{sv.mssv} | {sv.ho_ten} | {sv.hoc_phan} | {sv.diem:g}")
            hien_tai = hien_tai.tiep_theo


def nhap_sinh_vien() -> SinhVien:
    return SinhVien(
        input("MSSV: ").strip(),
        input("Họ và tên: ").strip(),
        input("Học phần: ").strip(),
        float(input("Điểm: ")),
    )


def main() -> None:
    danh_sach = DanhSachLienKet()
    while True:
        print("\n1. Thêm   2. Sửa điểm   3. Xóa   4. Tìm kiếm   5. Hiển thị   0. Thoát")
        lua_chon = input("Chọn chức năng: ").strip()
        try:
            if lua_chon == "1":
                danh_sach.them(nhap_sinh_vien())
            elif lua_chon == "2":
                sv = danh_sach.tim(input("MSSV cần sửa: ").strip())
                if sv:
                    sv.diem = float(input("Điểm mới: "))
                    print("Đã cập nhật điểm.")
                else:
                    print("Không tìm thấy sinh viên.")
            elif lua_chon == "3":
                print("Đã xóa." if danh_sach.xoa(input("MSSV cần xóa: ").strip()) else "Không tìm thấy.")
            elif lua_chon == "4":
                sv = danh_sach.tim(input("MSSV cần tìm: ").strip())
                print(sv if sv else "Không tìm thấy sinh viên.")
            elif lua_chon == "5":
                danh_sach.hien_thi()
            elif lua_chon == "0":
                break
            else:
                print("Lựa chọn không hợp lệ.")
        except ValueError as loi:
            print(f"Lỗi: {loi}")


if __name__ == "__main__":
    main()
