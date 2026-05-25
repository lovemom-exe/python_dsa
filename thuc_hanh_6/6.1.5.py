# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 6 - Phần 1 - Bài 5: liệt kê hoán vị bằng đệ quy."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def liet_ke_hoan_vi(phan_tu: list[str]) -> list[list[str]]:
    ket_qua: list[list[str]] = []

    def sinh_hoan_vi(vi_tri: int) -> None:
        if vi_tri == len(phan_tu):
            ket_qua.append(phan_tu.copy())
            return

        da_chon: set[str] = set()
        for i in range(vi_tri, len(phan_tu)):
            if phan_tu[i] in da_chon:
                continue
            da_chon.add(phan_tu[i])
            phan_tu[vi_tri], phan_tu[i] = phan_tu[i], phan_tu[vi_tri]
            sinh_hoan_vi(vi_tri + 1)
            phan_tu[vi_tri], phan_tu[i] = phan_tu[i], phan_tu[vi_tri]

    sinh_hoan_vi(0)
    return ket_qua


def main() -> None:
    phan_tu = input("Nhập các phần tử, cách nhau bởi dấu cách: ").split()
    if not phan_tu:
        print("Danh sách phần tử không được rỗng.")
        return
    if len(phan_tu) > 8:
        print("Chỉ hỗ trợ tối đa 8 phần tử để tránh in quá nhiều hoán vị.")
        return

    cac_hoan_vi = liet_ke_hoan_vi(phan_tu)
    print(f"Có {len(cac_hoan_vi)} hoán vị:")
    for hoan_vi in cac_hoan_vi:
        print(" ".join(hoan_vi))


if __name__ == "__main__":
    main()
