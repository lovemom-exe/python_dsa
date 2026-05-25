# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 5 - Phần 2: chồng toán tử cho số phức, vector, ma trận."""

from dataclasses import dataclass
import sys


sys.stdout.reconfigure(encoding="utf-8")


@dataclass
class SoPhuc:
    thuc: float
    ao: float

    def __add__(self, khac: "SoPhuc") -> "SoPhuc":
        return SoPhuc(self.thuc + khac.thuc, self.ao + khac.ao)

    def __sub__(self, khac: "SoPhuc") -> "SoPhuc":
        return SoPhuc(self.thuc - khac.thuc, self.ao - khac.ao)

    def __mul__(self, khac: "SoPhuc") -> "SoPhuc":
        return SoPhuc(
            self.thuc * khac.thuc - self.ao * khac.ao,
            self.thuc * khac.ao + self.ao * khac.thuc,
        )

    def __str__(self) -> str:
        dau = "+" if self.ao >= 0 else "-"
        return f"{self.thuc:g} {dau} {abs(self.ao):g}i"


@dataclass
class Vector:
    phan_tu: list[float]

    def __add__(self, khac: "Vector") -> "Vector":
        self._kiem_tra_kich_thuoc(khac)
        return Vector([a + b for a, b in zip(self.phan_tu, khac.phan_tu)])

    def __sub__(self, khac: "Vector") -> "Vector":
        self._kiem_tra_kich_thuoc(khac)
        return Vector([a - b for a, b in zip(self.phan_tu, khac.phan_tu)])

    def __mul__(self, khac: "Vector") -> float:
        self._kiem_tra_kich_thuoc(khac)
        return sum(a * b for a, b in zip(self.phan_tu, khac.phan_tu))

    def _kiem_tra_kich_thuoc(self, khac: "Vector") -> None:
        if len(self.phan_tu) != len(khac.phan_tu):
            raise ValueError("Hai vector phải có cùng số phần tử.")

    def __str__(self) -> str:
        return str(self.phan_tu)


@dataclass
class MaTran:
    dong: list[list[float]]

    def __post_init__(self) -> None:
        if not self.dong or not self.dong[0]:
            raise ValueError("Ma trận không được rỗng.")
        if any(len(dong) != len(self.dong[0]) for dong in self.dong):
            raise ValueError("Các dòng ma trận phải có cùng độ dài.")

    def __add__(self, khac: "MaTran") -> "MaTran":
        self._kiem_tra_cung_kich_thuoc(khac)
        return MaTran([[a + b for a, b in zip(x, y)] for x, y in zip(self.dong, khac.dong)])

    def __sub__(self, khac: "MaTran") -> "MaTran":
        self._kiem_tra_cung_kich_thuoc(khac)
        return MaTran([[a - b for a, b in zip(x, y)] for x, y in zip(self.dong, khac.dong)])

    def __mul__(self, khac: "MaTran") -> "MaTran":
        if len(self.dong[0]) != len(khac.dong):
            raise ValueError("Số cột ma trận thứ nhất phải bằng số dòng ma trận thứ hai.")
        cot_cua_khac = list(zip(*khac.dong))
        return MaTran(
            [[sum(a * b for a, b in zip(dong, cot)) for cot in cot_cua_khac] for dong in self.dong]
        )

    def _kiem_tra_cung_kich_thuoc(self, khac: "MaTran") -> None:
        if len(self.dong) != len(khac.dong) or len(self.dong[0]) != len(khac.dong[0]):
            raise ValueError("Hai ma trận phải có cùng kích thước.")

    def __str__(self) -> str:
        return "\n".join(str(dong) for dong in self.dong)


def main() -> None:
    z1, z2 = SoPhuc(2, 3), SoPhuc(1, -4)
    print(f"Số phức: ({z1}) + ({z2}) = {z1 + z2}")
    print(f"Số phức: ({z1}) * ({z2}) = {z1 * z2}")

    v1, v2 = Vector([1, 2, 3]), Vector([4, 5, 6])
    print(f"\nVector: {v1} + {v2} = {v1 + v2}")
    print(f"Tích vô hướng: {v1} * {v2} = {v1 * v2:g}")

    a = MaTran([[1, 2], [3, 4]])
    b = MaTran([[5, 6], [7, 8]])
    print(f"\nMa trận A + B:\n{a + b}")
    print(f"Ma trận A * B:\n{a * b}")


if __name__ == "__main__":
    main()
