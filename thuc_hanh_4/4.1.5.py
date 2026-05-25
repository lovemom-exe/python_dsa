# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Thực hành 4 - Phần 1 - Bài 5: phép toán vector và ma trận qua hàm."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def cong_vector(vector_a: list[float], vector_b: list[float]) -> list[float]:
    kiem_tra_vector(vector_a, vector_b)
    return [a + b for a, b in zip(vector_a, vector_b)]


def tru_vector(vector_a: list[float], vector_b: list[float]) -> list[float]:
    kiem_tra_vector(vector_a, vector_b)
    return [a - b for a, b in zip(vector_a, vector_b)]


def tich_vo_huong(vector_a: list[float], vector_b: list[float]) -> float:
    kiem_tra_vector(vector_a, vector_b)
    return sum(a * b for a, b in zip(vector_a, vector_b))


def kiem_tra_vector(vector_a: list[float], vector_b: list[float]) -> None:
    if not vector_a or len(vector_a) != len(vector_b):
        raise ValueError("Hai vector phải khác rỗng và cùng kích thước.")


def kiem_tra_ma_tran(ma_tran: list[list[float]]) -> None:
    if not ma_tran or not ma_tran[0] or any(len(dong) != len(ma_tran[0]) for dong in ma_tran):
        raise ValueError("Ma trận không hợp lệ.")


def cong_ma_tran(ma_tran_a: list[list[float]], ma_tran_b: list[list[float]]) -> list[list[float]]:
    kiem_tra_cung_kich_thuoc(ma_tran_a, ma_tran_b)
    return [[a + b for a, b in zip(dong_a, dong_b)] for dong_a, dong_b in zip(ma_tran_a, ma_tran_b)]


def tru_ma_tran(ma_tran_a: list[list[float]], ma_tran_b: list[list[float]]) -> list[list[float]]:
    kiem_tra_cung_kich_thuoc(ma_tran_a, ma_tran_b)
    return [[a - b for a, b in zip(dong_a, dong_b)] for dong_a, dong_b in zip(ma_tran_a, ma_tran_b)]


def kiem_tra_cung_kich_thuoc(ma_tran_a: list[list[float]], ma_tran_b: list[list[float]]) -> None:
    kiem_tra_ma_tran(ma_tran_a)
    kiem_tra_ma_tran(ma_tran_b)
    if len(ma_tran_a) != len(ma_tran_b) or len(ma_tran_a[0]) != len(ma_tran_b[0]):
        raise ValueError("Hai ma trận phải cùng kích thước để cộng hoặc trừ.")


def nhan_ma_tran(ma_tran_a: list[list[float]], ma_tran_b: list[list[float]]) -> list[list[float]]:
    kiem_tra_ma_tran(ma_tran_a)
    kiem_tra_ma_tran(ma_tran_b)
    if len(ma_tran_a[0]) != len(ma_tran_b):
        raise ValueError("Số cột ma trận A phải bằng số dòng ma trận B.")
    cac_cot_b = list(zip(*ma_tran_b))
    return [[sum(a * b for a, b in zip(dong, cot)) for cot in cac_cot_b] for dong in ma_tran_a]


def doc_vector(ghi_chu: str) -> list[float]:
    return [float(so) for so in input(ghi_chu).split()]


def doc_ma_tran(ghi_chu: str) -> list[list[float]]:
    print(ghi_chu)
    so_dong = int(input("Số dòng: "))
    return [[float(so) for so in input(f"Dòng {i + 1}: ").split()] for i in range(so_dong)]


def dinh_dang_so(gia_tri: float) -> str:
    return f"{gia_tri:g}"


def dinh_dang_vector(vector: list[float]) -> str:
    return "[" + ", ".join(dinh_dang_so(gia_tri) for gia_tri in vector) + "]"


def in_ma_tran(ma_tran: list[list[float]]) -> None:
    for dong in ma_tran:
        print(" ".join(dinh_dang_so(gia_tri) for gia_tri in dong))


def main() -> None:
    try:
        vector_a = doc_vector("Nhập vector A: ")
        vector_b = doc_vector("Nhập vector B: ")
        print(f"A + B = {dinh_dang_vector(cong_vector(vector_a, vector_b))}")
        print(f"A - B = {dinh_dang_vector(tru_vector(vector_a, vector_b))}")
        print(f"A . B = {dinh_dang_so(tich_vo_huong(vector_a, vector_b))}")

        ma_tran_a = doc_ma_tran("\nNhập ma trận A")
        ma_tran_b = doc_ma_tran("Nhập ma trận B")
        print("A + B =")
        in_ma_tran(cong_ma_tran(ma_tran_a, ma_tran_b))
        print("A - B =")
        in_ma_tran(tru_ma_tran(ma_tran_a, ma_tran_b))
        print("A * B =")
        in_ma_tran(nhan_ma_tran(ma_tran_a, ma_tran_b))
    except ValueError as loi:
        print(f"Lỗi: {loi}")


if __name__ == "__main__":
    main()
