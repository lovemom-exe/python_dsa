# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Thực hành 3 - Phần 1: đọc ảnh ký tự X từ file và xuất ra màn hình/file."""

from pathlib import Path
import sys


sys.stdout.reconfigure(encoding="utf-8")


def doc_anh_ky_tu(duong_dan: Path) -> list[str]:
    if not duong_dan.exists():
        raise FileNotFoundError("Không tìm thấy file ảnh văn bản.")

    cac_dong = duong_dan.read_text(encoding="utf-8").splitlines()
    if not cac_dong:
        raise ValueError("File ảnh đang rỗng.")
    if not any("X" in dong.upper() for dong in cac_dong):
        raise ValueError("File ảnh không có điểm ảnh ký tự X.")
    return [dong.upper() for dong in cac_dong]


def chuyen_sang_anh_hien_thi(cac_dong: list[str]) -> list[str]:
    """Giữ điểm ảnh X và đổi các ký tự khác thành khoảng trắng."""
    return ["".join("X" if ky_tu == "X" else " " for ky_tu in dong) for dong in cac_dong]


def ghi_anh_text(duong_dan: Path, anh: list[str]) -> None:
    duong_dan.write_text("\n".join(anh) + "\n", encoding="utf-8")


def main() -> None:
    ten_file_vao = input("Nhập file ảnh text đầu vào: ").strip()
    ten_file_ra = input("Nhập file kết quả (Enter để dùng ket_qua_anh.txt): ").strip()
    file_vao = Path(ten_file_vao)
    file_ra = Path(ten_file_ra) if ten_file_ra else Path(__file__).with_name("ket_qua_anh.txt")

    try:
        anh = chuyen_sang_anh_hien_thi(doc_anh_ky_tu(file_vao))
        print("\nẢnh hiển thị bằng ký tự X:")
        print("\n".join(anh))
        ghi_anh_text(file_ra, anh)
        print(f"\nĐã ghi ảnh kết quả vào: {file_ra}")
    except (FileNotFoundError, ValueError) as loi:
        print(f"Lỗi: {loi}")


if __name__ == "__main__":
    main()
