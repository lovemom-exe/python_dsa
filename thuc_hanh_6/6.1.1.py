# Name: Nguyễn Minh Hoàng
# Student ID: 202418904
# Class: 763965

"""Bài thực hành 6 - Phần 1: tính Fibonacci bằng đệ quy."""

import sys


sys.stdout.reconfigure(encoding="utf-8")


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main() -> None:
    try:
        n = int(input("Nhập n (0 <= n <= 35): "))
    except ValueError:
        print("n phải là số nguyên.")
        return

    if not 0 <= n <= 35:
        print("n phải thuộc đoạn từ 0 đến 35.")
        return
    print(f"F({n}) = {fibonacci(n)}")


if __name__ == "__main__":
    main()
