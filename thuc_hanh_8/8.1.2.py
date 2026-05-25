# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 8 - Phần 1 - Bài 2: tính biểu thức toán học bằng ngăn xếp."""

import operator
import re
import sys


sys.stdout.reconfigure(encoding="utf-8")
MAU_TOKEN = re.compile(r"\s*(?:(\d+(?:\.\d*)?|\.\d+)|([()+\-*/]))")
DO_UU_TIEN = {"u+": 3, "u-": 3, "*": 2, "/": 2, "+": 1, "-": 1}


def tach_token(bieu_thuc: str) -> list[str]:
    tokens: list[str] = []
    vi_tri = 0
    while vi_tri < len(bieu_thuc):
        if not bieu_thuc[vi_tri:].strip():
            break
        ket_qua = MAU_TOKEN.match(bieu_thuc, vi_tri)
        if not ket_qua:
            raise ValueError(f"Ký tự không hợp lệ tại vị trí {vi_tri + 1}.")
        tokens.append(ket_qua.group(1) or ket_qua.group(2))
        vi_tri = ket_qua.end()
    if not tokens:
        raise ValueError("Biểu thức không được rỗng.")
    return tokens


def doi_sang_hau_to(tokens: list[str]) -> list[str]:
    dau_ra: list[str] = []
    ngan_xep: list[str] = []
    token_truoc: str | None = None

    for token in tokens:
        if token.replace(".", "", 1).isdigit():
            dau_ra.append(token)
        elif token == "(":
            ngan_xep.append(token)
        elif token == ")":
            while ngan_xep and ngan_xep[-1] != "(":
                dau_ra.append(ngan_xep.pop())
            if not ngan_xep:
                raise ValueError("Dấu ngoặc không cân bằng.")
            ngan_xep.pop()
        else:
            if token in "+-" and (token_truoc is None or token_truoc in DO_UU_TIEN or token_truoc == "("):
                token = "u" + token
            while (
                ngan_xep
                and ngan_xep[-1] != "("
                and (
                    DO_UU_TIEN[ngan_xep[-1]] > DO_UU_TIEN[token]
                    or (DO_UU_TIEN[ngan_xep[-1]] == DO_UU_TIEN[token] and token not in {"u+", "u-"})
                )
            ):
                dau_ra.append(ngan_xep.pop())
            ngan_xep.append(token)
        token_truoc = token

    while ngan_xep:
        token = ngan_xep.pop()
        if token == "(":
            raise ValueError("Dấu ngoặc không cân bằng.")
        dau_ra.append(token)
    return dau_ra


def tinh_hau_to(tokens: list[str]) -> float:
    ngan_xep: list[float] = []
    phep_tinh = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    for token in tokens:
        if token.replace(".", "", 1).isdigit():
            ngan_xep.append(float(token))
        elif token in {"u+", "u-"}:
            if not ngan_xep:
                raise ValueError("Biểu thức thiếu toán hạng.")
            gia_tri = ngan_xep.pop()
            ngan_xep.append(gia_tri if token == "u+" else -gia_tri)
        else:
            if len(ngan_xep) < 2:
                raise ValueError("Biểu thức thiếu toán hạng.")
            so_thu_hai = ngan_xep.pop()
            so_thu_nhat = ngan_xep.pop()
            ngan_xep.append(phep_tinh[token](so_thu_nhat, so_thu_hai))
    if len(ngan_xep) != 1:
        raise ValueError("Biểu thức không hợp lệ.")
    return ngan_xep[0]


def tinh_bieu_thuc(bieu_thuc: str) -> float:
    return tinh_hau_to(doi_sang_hau_to(tach_token(bieu_thuc)))


def main() -> None:
    try:
        bieu_thuc = input("Nhập biểu thức: ")
        print(f"Kết quả = {tinh_bieu_thuc(bieu_thuc):g}")
    except (ValueError, ZeroDivisionError) as loi:
        print(f"Lỗi: {loi}")


if __name__ == "__main__":
    main()
