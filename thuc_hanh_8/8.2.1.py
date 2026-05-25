# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 8 - Phần 2: mô phỏng hàng đợi yêu cầu đến máy chủ."""

from collections import deque
from dataclasses import dataclass
import sys


sys.stdout.reconfigure(encoding="utf-8")


@dataclass
class YeuCau:
    ten: str
    dia_chi_ip: str
    noi_dung: str
    thoi_gian_xu_ly: int


class MayChu:
    def __init__(self) -> None:
        self.hang_doi: deque[YeuCau] = deque()

    def them_yeu_cau(self, yeu_cau: YeuCau) -> None:
        self.hang_doi.append(yeu_cau)

    def xu_ly_tiep_theo(self) -> YeuCau | None:
        return self.hang_doi.popleft() if self.hang_doi else None

    def hien_thi_hang_doi(self) -> None:
        if not self.hang_doi:
            print("Hàng đợi đang rỗng.")
            return
        for stt, yeu_cau in enumerate(self.hang_doi, start=1):
            print(f"{stt}. {yeu_cau.ten} từ {yeu_cau.dia_chi_ip} ({yeu_cau.thoi_gian_xu_ly}s)")


def nhap_yeu_cau() -> YeuCau:
    ten = input("Tên yêu cầu: ").strip()
    dia_chi_ip = input("Địa chỉ IP: ").strip()
    noi_dung = input("Nội dung: ").strip()
    thoi_gian = int(input("Thời gian thực hiện (giây): "))
    if thoi_gian < 0:
        raise ValueError("Thời gian không được âm.")
    return YeuCau(ten, dia_chi_ip, noi_dung, thoi_gian)


def main() -> None:
    may_chu = MayChu()
    while True:
        print("\n1. Gửi yêu cầu   2. Xử lý yêu cầu tiếp theo   3. Xem hàng đợi   0. Thoát")
        lua_chon = input("Chọn chức năng: ").strip()
        try:
            if lua_chon == "1":
                may_chu.them_yeu_cau(nhap_yeu_cau())
                print("Yêu cầu đã vào hàng đợi.")
            elif lua_chon == "2":
                yeu_cau = may_chu.xu_ly_tiep_theo()
                if yeu_cau:
                    print(f"Đang xử lý '{yeu_cau.ten}': {yeu_cau.noi_dung} ({yeu_cau.thoi_gian_xu_ly}s).")
                else:
                    print("Không có yêu cầu để xử lý.")
            elif lua_chon == "3":
                may_chu.hien_thi_hang_doi()
            elif lua_chon == "0":
                break
            else:
                print("Lựa chọn không hợp lệ.")
        except ValueError as loi:
            print(f"Lỗi: {loi}")


if __name__ == "__main__":
    main()
