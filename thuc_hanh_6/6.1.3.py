# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 6 - Phần 1 - Bài 3: bài toán Tháp Hà Nội."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def thap_ha_noi(
    so_dia: int,
    cot_nguon: str,
    cot_trung_gian: str,
    cot_dich: str,
    cac_buoc: list[tuple[int, str, str]],
) -> None:
    """Đưa các đĩa từ cột nguồn sang cột đích bằng đệ quy."""
    if so_dia == 0:
        return
    thap_ha_noi(so_dia - 1, cot_nguon, cot_dich, cot_trung_gian, cac_buoc)
    cac_buoc.append((so_dia, cot_nguon, cot_dich))
    thap_ha_noi(so_dia - 1, cot_trung_gian, cot_nguon, cot_dich, cac_buoc)


def mo_phong_chuyen_dia(so_dia: int, cac_buoc: list[tuple[int, str, str]]) -> None:
    cac_cot = {"A": list(range(so_dia, 0, -1)), "B": [], "C": []}
    print(f"Ban đầu: A={cac_cot['A']}, B={cac_cot['B']}, C={cac_cot['C']}")

    for stt, (dia, cot_di, cot_den) in enumerate(cac_buoc, start=1):
        dia_dang_chuyen = cac_cot[cot_di].pop()
        if dia_dang_chuyen != dia:
            raise RuntimeError("Trình tự di chuyển đĩa không hợp lệ.")
        if cac_cot[cot_den] and cac_cot[cot_den][-1] < dia:
            raise RuntimeError("Không thể đặt đĩa lớn lên trên đĩa nhỏ.")
        cac_cot[cot_den].append(dia)
        print(
            f"Bước {stt}: chuyển đĩa {dia} từ {cot_di} sang {cot_den} "
            f"=> A={cac_cot['A']}, B={cac_cot['B']}, C={cac_cot['C']}"
        )


def main() -> None:
    try:
        so_dia = int(input("Nhập số đĩa cần chuyển (1 <= n <= 10): "))
    except ValueError:
        print("Số đĩa phải là số nguyên.")
        return

    if not 1 <= so_dia <= 10:
        print("Số đĩa phải thuộc đoạn từ 1 đến 10.")
        return

    cac_buoc: list[tuple[int, str, str]] = []
    thap_ha_noi(so_dia, "A", "B", "C", cac_buoc)
    print(f"Số bước ít nhất cần thực hiện: 2^{so_dia} - 1 = {2 ** so_dia - 1}")
    mo_phong_chuyen_dia(so_dia, cac_buoc)
    print(f"Đã chuyển xong {so_dia} đĩa từ cột A sang cột C trong {len(cac_buoc)} bước.")


if __name__ == "__main__":
    main()
