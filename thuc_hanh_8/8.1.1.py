# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 8 - Phần 1 - Bài 1: trình soạn thảo có undo và redo."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


class TrinhSoanThao:
    def __init__(self) -> None:
        self.lich_su = [""]
        self.vi_tri_hien_tai = 0

    @property
    def noi_dung(self) -> str:
        return self.lich_su[self.vi_tri_hien_tai]

    def _luu(self, noi_dung_moi: str) -> None:
        self.lich_su = self.lich_su[: self.vi_tri_hien_tai + 1]
        self.lich_su.append(noi_dung_moi)
        self.vi_tri_hien_tai += 1

    def them(self, van_ban: str) -> None:
        self._luu(self.noi_dung + van_ban)

    def thay_the(self, van_ban: str) -> None:
        self._luu(van_ban)

    def xoa_cuoi(self, so_ky_tu: int) -> None:
        if so_ky_tu < 0:
            raise ValueError("Số ký tự phải không âm.")
        self._luu(self.noi_dung[:-so_ky_tu] if so_ky_tu else self.noi_dung)

    def undo(self) -> bool:
        if self.vi_tri_hien_tai == 0:
            return False
        self.vi_tri_hien_tai -= 1
        return True

    def redo(self) -> bool:
        if self.vi_tri_hien_tai == len(self.lich_su) - 1:
            return False
        self.vi_tri_hien_tai += 1
        return True


def main() -> None:
    soan_thao = TrinhSoanThao()
    while True:
        print(f"\nNội dung: {soan_thao.noi_dung!r}")
        print("1. Thêm văn bản   2. Thay thế   3. Xóa cuối   4. Undo   5. Redo   0. Thoát")
        lua_chon = input("Chọn chức năng: ").strip()
        try:
            if lua_chon == "1":
                soan_thao.them(input("Văn bản cần thêm: "))
            elif lua_chon == "2":
                soan_thao.thay_the(input("Nội dung mới: "))
            elif lua_chon == "3":
                soan_thao.xoa_cuoi(int(input("Số ký tự cần xóa: ")))
            elif lua_chon == "4":
                print("Không thể undo thêm." if not soan_thao.undo() else "Đã undo.")
            elif lua_chon == "5":
                print("Không thể redo thêm." if not soan_thao.redo() else "Đã redo.")
            elif lua_chon == "0":
                break
            else:
                print("Lựa chọn không hợp lệ.")
        except ValueError as loi:
            print(f"Lỗi: {loi}")


if __name__ == "__main__":
    main()
