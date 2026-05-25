# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 6 - Phần 1 - Bài 4: bài toán mã đi tuần."""

import sys


sys.stdout.reconfigure(encoding="utf-8")
CAC_NUOC_DI = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]


def tim_hanh_trinh(kich_thuoc: int, dong_dau: int, cot_dau: int) -> list[list[int]] | None:
    ban_co = [[0] * kich_thuoc for _ in range(kich_thuoc)]
    ban_co[dong_dau][cot_dau] = 1

    def cac_o_co_the_den(dong: int, cot: int) -> list[tuple[int, int]]:
        ket_qua: list[tuple[int, int]] = []
        for lech_dong, lech_cot in CAC_NUOC_DI:
            dong_moi, cot_moi = dong + lech_dong, cot + lech_cot
            if 0 <= dong_moi < kich_thuoc and 0 <= cot_moi < kich_thuoc and ban_co[dong_moi][cot_moi] == 0:
                ket_qua.append((dong_moi, cot_moi))
        return ket_qua

    def di_chuyen(dong: int, cot: int, buoc: int) -> bool:
        if buoc == kich_thuoc * kich_thuoc:
            return True

        # Ưu tiên ô có ít đường đi tiếp để giảm số nhánh phải thử.
        ung_vien = cac_o_co_the_den(dong, cot)
        ung_vien.sort(key=lambda o: len(cac_o_co_the_den(*o)))
        for dong_moi, cot_moi in ung_vien:
            ban_co[dong_moi][cot_moi] = buoc + 1
            if di_chuyen(dong_moi, cot_moi, buoc + 1):
                return True
            ban_co[dong_moi][cot_moi] = 0
        return False

    return ban_co if di_chuyen(dong_dau, cot_dau, 1) else None


def main() -> None:
    try:
        kich_thuoc = int(input("Nhập kích thước bàn cờ N (1 <= N <= 8): "))
        dong_dau = int(input("Nhập dòng xuất phát (bắt đầu từ 1): ")) - 1
        cot_dau = int(input("Nhập cột xuất phát (bắt đầu từ 1): ")) - 1
    except ValueError:
        print("Dữ liệu nhập vào phải là số nguyên.")
        return

    if not 1 <= kich_thuoc <= 8 or not (0 <= dong_dau < kich_thuoc and 0 <= cot_dau < kich_thuoc):
        print("Kích thước hoặc vị trí xuất phát không hợp lệ.")
        return

    hanh_trinh = tim_hanh_trinh(kich_thuoc, dong_dau, cot_dau)
    if hanh_trinh is None:
        print("Không tìm thấy hành trình đi qua toàn bộ bàn cờ.")
        return
    print("Thứ tự các bước đi của quân mã:")
    do_rong = len(str(kich_thuoc * kich_thuoc))
    for dong in hanh_trinh:
        print(" ".join(f"{buoc:>{do_rong}}" for buoc in dong))


if __name__ == "__main__":
    main()
