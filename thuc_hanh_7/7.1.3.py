# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 7 - Phần 1 - Bài 3: tìm mảng con có tổng bằng M."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def tim_mang_con(mang: list[int], muc_tieu: int) -> tuple[int, int] | None:
    tong_truoc = 0
    vi_tri_theo_tong = {0: -1}
    for vi_tri, gia_tri in enumerate(mang):
        tong_truoc += gia_tri
        tong_can_tim = tong_truoc - muc_tieu
        if tong_can_tim in vi_tri_theo_tong:
            return vi_tri_theo_tong[tong_can_tim] + 1, vi_tri
        vi_tri_theo_tong.setdefault(tong_truoc, vi_tri)
    return None


def main() -> None:
    try:
        mang = [int(so) for so in input("Nhập mảng số nguyên: ").split()]
        muc_tieu = int(input("Nhập M: "))
    except ValueError:
        print("Dữ liệu nhập vào phải là số nguyên.")
        return

    vi_tri = tim_mang_con(mang, muc_tieu)
    if vi_tri is None:
        print("Không tìm thấy mảng con có tổng bằng M.")
        return
    dau, cuoi = vi_tri
    print(f"Mảng con tìm được: {mang[dau:cuoi + 1]} (vị trí {dau + 1} đến {cuoi + 1})")


if __name__ == "__main__":
    main()
