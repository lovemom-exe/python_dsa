# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 2 - Phần 1: thao tác dữ liệu trên tệp văn bản."""

import sys
from pathlib import Path


sys.stdout.reconfigure(encoding="utf-8")


def doc_cac_dong(duong_dan: Path) -> list[str]:
    """Đọc nội dung tệp thành danh sách dòng."""
    return duong_dan.read_text(encoding="utf-8").splitlines()


def in_cac_dong(cac_dong: list[str]) -> None:
    if not cac_dong:
        print("(Tệp đang rỗng.)")
        return

    for so_dong, noi_dung in enumerate(cac_dong, start=1):
        print(f"{so_dong}. {noi_dung}")


def hien_thi_du_lieu(duong_dan: Path) -> None:
    if not duong_dan.exists():
        print("Tệp chưa tồn tại.")
        return

    print(f"\nNội dung tệp {duong_dan}:")
    in_cac_dong(doc_cac_dong(duong_dan))


def them_du_lieu(duong_dan: Path) -> None:
    noi_dung = input("Nhập nội dung cần thêm: ")
    with duong_dan.open("a", encoding="utf-8") as tep:
        tep.write(noi_dung + "\n")
    print("Đã thêm dữ liệu.")


def chon_dong(cac_dong: list[str], hanh_dong: str) -> int | None:
    in_cac_dong(cac_dong)
    try:
        so_dong = int(input(f"Nhập số dòng cần {hanh_dong}: "))
    except ValueError:
        print("Số dòng không hợp lệ.")
        return None

    if not 1 <= so_dong <= len(cac_dong):
        print("Số dòng nằm ngoài phạm vi dữ liệu.")
        return None
    return so_dong - 1


def ghi_cac_dong(duong_dan: Path, cac_dong: list[str]) -> None:
    noi_dung = "\n".join(cac_dong)
    if cac_dong:
        noi_dung += "\n"
    duong_dan.write_text(noi_dung, encoding="utf-8")


def xoa_du_lieu(duong_dan: Path) -> None:
    if not duong_dan.exists():
        print("Tệp chưa tồn tại.")
        return

    cac_dong = doc_cac_dong(duong_dan)
    if not cac_dong:
        print("Tệp đang rỗng, không có dữ liệu để xóa.")
        return

    vi_tri = chon_dong(cac_dong, "xóa")
    if vi_tri is None:
        return

    cac_dong.pop(vi_tri)
    ghi_cac_dong(duong_dan, cac_dong)
    print("Đã xóa dữ liệu.")


def cap_nhat_du_lieu(duong_dan: Path) -> None:
    if not duong_dan.exists():
        print("Tệp chưa tồn tại.")
        return

    cac_dong = doc_cac_dong(duong_dan)
    if not cac_dong:
        print("Tệp đang rỗng, không có dữ liệu để cập nhật.")
        return

    vi_tri = chon_dong(cac_dong, "cập nhật")
    if vi_tri is None:
        return

    cac_dong[vi_tri] = input("Nhập nội dung mới: ")
    ghi_cac_dong(duong_dan, cac_dong)
    print("Đã cập nhật dữ liệu.")


def main() -> None:
    ten_tep = input("Nhập đường dẫn tệp (Enter để dùng du_lieu.txt): ").strip()
    duong_dan = Path(ten_tep) if ten_tep else Path(__file__).with_name("du_lieu.txt")

    while True:
        print("\n1. Hiển thị dữ liệu")
        print("2. Thêm dữ liệu")
        print("3. Xóa dữ liệu")
        print("4. Cập nhật dữ liệu")
        print("0. Thoát")
        lua_chon = input("Chọn chức năng: ").strip()

        if lua_chon == "1":
            hien_thi_du_lieu(duong_dan)
        elif lua_chon == "2":
            them_du_lieu(duong_dan)
        elif lua_chon == "3":
            xoa_du_lieu(duong_dan)
        elif lua_chon == "4":
            cap_nhat_du_lieu(duong_dan)
        elif lua_chon == "0":
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()
