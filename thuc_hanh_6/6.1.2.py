# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 6 - Phần 1 - Bài 2: bài toán N hậu bằng quay lui đệ quy."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def giai_n_hau(kich_thuoc: int) -> list[list[int]]:
    loi_giai: list[list[int]] = []
    vi_tri_hau: list[int] = []
    cot_da_dung: set[int] = set()
    cheo_chinh: set[int] = set()
    cheo_phu: set[int] = set()

    def dat_hau(dong: int) -> None:
        if dong == kich_thuoc:
            loi_giai.append(vi_tri_hau.copy())
            return

        for cot in range(kich_thuoc):
            if cot in cot_da_dung or dong - cot in cheo_chinh or dong + cot in cheo_phu:
                continue
            vi_tri_hau.append(cot)
            cot_da_dung.add(cot)
            cheo_chinh.add(dong - cot)
            cheo_phu.add(dong + cot)

            dat_hau(dong + 1)

            vi_tri_hau.pop()
            cot_da_dung.remove(cot)
            cheo_chinh.remove(dong - cot)
            cheo_phu.remove(dong + cot)

    dat_hau(0)
    return loi_giai


def in_ban_co(vi_tri_hau: list[int]) -> None:
    for cot_dat_hau in vi_tri_hau:
        print(" ".join("Q" if cot == cot_dat_hau else "." for cot in range(len(vi_tri_hau))))


def main() -> None:
    try:
        kich_thuoc = int(input("Nhập số quân hậu N (1 <= N <= 10): "))
    except ValueError:
        print("N phải là số nguyên.")
        return

    if not 1 <= kich_thuoc <= 10:
        print("N phải thuộc đoạn từ 1 đến 10.")
        return

    loi_giai = giai_n_hau(kich_thuoc)
    print(f"Số cách đặt {kich_thuoc} quân hậu = {len(loi_giai)}")
    if not loi_giai:
        print("Không tồn tại cách đặt hợp lệ.")
        return

    gioi_han_hien_thi = min(len(loi_giai), 3)
    for stt, cach_dat in enumerate(loi_giai[:gioi_han_hien_thi], start=1):
        print(f"\nCách đặt {stt}:")
        in_ban_co(cach_dat)
    if len(loi_giai) > gioi_han_hien_thi:
        print(f"\nChỉ hiển thị {gioi_han_hien_thi} cách đặt đầu tiên.")


if __name__ == "__main__":
    main()
