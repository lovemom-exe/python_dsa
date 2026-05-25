# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 6 - Phần 2: quản lý mượn trả sách theo các chương trình con."""

from dataclasses import dataclass
from datetime import date
import sys


sys.stdout.reconfigure(encoding="utf-8")
MUC_PHAT_MOI_NGAY = 5000


@dataclass
class BanDoc:
    ma_the: str
    ho_ten: str


@dataclass
class Sach:
    ma_sach: str
    ten_sach: str
    so_luong: int


@dataclass
class PhieuMuon:
    ma_the: str
    ma_sach: str
    ngay_hen_tra: date


class ThuVien:
    def __init__(self) -> None:
        self.ban_doc: dict[str, BanDoc] = {}
        self.sach: dict[str, Sach] = {}
        self.phieu_muon: dict[tuple[str, str], PhieuMuon] = {}

    def them_ban_doc(self, ma_the: str, ho_ten: str) -> None:
        if ma_the in self.ban_doc:
            raise ValueError("Mã thẻ đã tồn tại.")
        self.ban_doc[ma_the] = BanDoc(ma_the, ho_ten)

    def them_sach(self, ma_sach: str, ten_sach: str, so_luong: int) -> None:
        if so_luong < 0:
            raise ValueError("Số lượng sách không được âm.")
        if ma_sach in self.sach:
            self.sach[ma_sach].so_luong += so_luong
        else:
            self.sach[ma_sach] = Sach(ma_sach, ten_sach, so_luong)

    def muon_sach(self, ma_the: str, ma_sach: str, ngay_hen_tra: date) -> None:
        if ma_the not in self.ban_doc:
            raise ValueError("Không tìm thấy bạn đọc.")
        if ma_sach not in self.sach:
            raise ValueError("Không tìm thấy sách.")
        if self.sach[ma_sach].so_luong == 0:
            raise ValueError("Sách đã hết.")
        khoa = (ma_the, ma_sach)
        if khoa in self.phieu_muon:
            raise ValueError("Bạn đọc đang mượn sách này.")
        self.sach[ma_sach].so_luong -= 1
        self.phieu_muon[khoa] = PhieuMuon(ma_the, ma_sach, ngay_hen_tra)

    def tra_sach(self, ma_the: str, ma_sach: str, ngay_tra: date) -> int:
        khoa = (ma_the, ma_sach)
        if khoa not in self.phieu_muon:
            raise ValueError("Không tìm thấy phiếu mượn.")
        phieu = self.phieu_muon.pop(khoa)
        self.sach[ma_sach].so_luong += 1
        so_ngay_qua_han = max((ngay_tra - phieu.ngay_hen_tra).days, 0)
        return so_ngay_qua_han * MUC_PHAT_MOI_NGAY

    def hien_thi(self) -> None:
        print("\nDanh sách bạn đọc:")
        for ban_doc in self.ban_doc.values():
            print(f"- {ban_doc.ma_the}: {ban_doc.ho_ten}")
        print("Danh sách sách:")
        for sach in self.sach.values():
            print(f"- {sach.ma_sach}: {sach.ten_sach}, còn {sach.so_luong} quyển")
        print("Danh sách đang mượn:")
        for phieu in self.phieu_muon.values():
            print(f"- Thẻ {phieu.ma_the} mượn {phieu.ma_sach}, hẹn trả {phieu.ngay_hen_tra}")


def nhap_ngay(ghi_chu: str) -> date:
    return date.fromisoformat(input(f"{ghi_chu} (yyyy-mm-dd): ").strip())


def xu_ly_menu(thu_vien: ThuVien, lua_chon: str) -> None:
    if lua_chon == "1":
        thu_vien.them_ban_doc(input("Mã thẻ: ").strip(), input("Họ tên: ").strip())
        print("Đã cấp thẻ bạn đọc.")
    elif lua_chon == "2":
        ma_sach = input("Mã sách: ").strip()
        ten_sach = input("Tên sách: ").strip()
        so_luong = int(input("Số lượng: "))
        thu_vien.them_sach(ma_sach, ten_sach, so_luong)
        print("Đã cập nhật sách.")
    elif lua_chon == "3":
        thu_vien.muon_sach(
            input("Mã thẻ: ").strip(),
            input("Mã sách: ").strip(),
            nhap_ngay("Ngày hẹn trả"),
        )
        print("Mượn sách thành công.")
    elif lua_chon == "4":
        phi_phat = thu_vien.tra_sach(
            input("Mã thẻ: ").strip(),
            input("Mã sách: ").strip(),
            nhap_ngay("Ngày trả"),
        )
        print(f"Trả sách thành công. Phí phạt: {phi_phat:,} đồng.")
    elif lua_chon == "5":
        thu_vien.hien_thi()
    else:
        print("Lựa chọn không hợp lệ.")


def main() -> None:
    thu_vien = ThuVien()
    while True:
        print("\n1. Cấp thẻ bạn đọc   2. Nhập sách   3. Mượn sách")
        print("4. Trả sách          5. Hiển thị   0. Thoát")
        lua_chon = input("Chọn chức năng: ").strip()
        if lua_chon == "0":
            break
        try:
            xu_ly_menu(thu_vien, lua_chon)
        except (ValueError, KeyError) as loi:
            print(f"Lỗi: {loi}")


if __name__ == "__main__":
    main()
