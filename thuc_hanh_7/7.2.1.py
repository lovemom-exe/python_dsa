# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 7 - Phần 2 - Bài 1: thêm, sửa, xóa, tìm kiếm trong danh sách."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def hien_thi(danh_sach: list[int]) -> None:
    print(f"Danh sách hiện tại: {danh_sach}")


def main() -> None:
    danh_sach: list[int] = []
    while True:
        print("\n1. Thêm   2. Sửa   3. Xóa   4. Tìm kiếm   5. Hiển thị   0. Thoát")
        lua_chon = input("Chọn chức năng: ").strip()
        try:
            if lua_chon == "1":
                danh_sach.append(int(input("Giá trị cần thêm: ")))
            elif lua_chon == "2":
                vi_tri = int(input("Vị trí cần sửa (bắt đầu từ 1): ")) - 1
                if not 0 <= vi_tri < len(danh_sach):
                    raise IndexError
                danh_sach[vi_tri] = int(input("Giá trị mới: "))
            elif lua_chon == "3":
                vi_tri = int(input("Vị trí cần xóa (bắt đầu từ 1): ")) - 1
                if not 0 <= vi_tri < len(danh_sach):
                    raise IndexError
                danh_sach.pop(vi_tri)
            elif lua_chon == "4":
                gia_tri = int(input("Giá trị cần tìm: "))
                vi_tri = [i + 1 for i, so in enumerate(danh_sach) if so == gia_tri]
                print(f"Vị trí tìm thấy: {vi_tri}" if vi_tri else "Không tìm thấy giá trị.")
            elif lua_chon == "5":
                hien_thi(danh_sach)
            elif lua_chon == "0":
                break
            else:
                print("Lựa chọn không hợp lệ.")
        except ValueError:
            print("Vui lòng nhập số nguyên.")
        except IndexError:
            print("Vị trí nằm ngoài danh sách.")


if __name__ == "__main__":
    main()
