# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 2 - Phần 2 - Bài 1: in các ký tự từ A đến Z."""


def in_bang_chu_cai() -> None:
    for ma_ascii in range(ord("A"), ord("Z") + 1):
        print(chr(ma_ascii), end=" ")
    print()


if __name__ == "__main__":
    in_bang_chu_cai()
