# -*- coding: utf-8 -*-
import sys
import math
ham_chucnang =[
            "Fraction(n, d) — tạo phân số n/d và tự động rút gọn — Fraction(6, 9) → 2/3.",
            "Fraction(x) — tạo từ int/float/str — Fraction('0.75') → 3/4.",
            "f.numerator — lấy tử số — Fraction(3, 4).numerator → 3.",
            "f.denominator — lấy mẫu số — Fraction(3, 4).denominator → 4.",
            "float(f) — đổi phân số thành float — float(Fraction(3, 4)) → 0.75.",
            "f.limit_denominator(max_den) — xấp xỉ với mẫu nhỏ nhất ≤ max_den — Fraction(22, 7).limit_denominator(5) → 3/1.",
            "Fraction.from_float(x) — tạo từ float (tránh sai số khi ép trực tiếp).",
            "Fraction.from_decimal(x) — tạo từ Decimal chính xác."
            ]

baitap = """- Nhấm phím 1 để làm bài tập 1: Tính diện tích tam giác biết 3 cạnh a,b,c(m).
- Nhấm phím 2 để làm bài tập 2: Bài toán giải phương bậc 2 (làm tròn đến số thập phân thứ 6).
- Nhấm phím Enter để quay lại menu chính
- Nhấn phím khác để thoát."""

def show():
    print(f"\n=== Chào mừng bạn đến với Fraction (phân số) ===")
    print("• Cú pháp: F = Fraction(a,b) với a,b là int.")
    print("• Cấu trúc: Tử/mẫu tối giản; số học chính xác hữu tỉ.")
    print("• Áp dụng: Xác suất, tỉ lệ pha trộn, tránh sai số float.")
    print("• Note: dùng với float có thể không chính xác do sai số float.")
    print("• Hàm/phương thức thường gặp:")
    for f in ham_chucnang:
        print("   -", f)
    print(f"""\nChúc mừng bạn vừa tìm hiểu xong về cấu trúc Fraction!
\n---Nhấn phím 36 để đến với bài tập ví dụ---
---Nhấn phím Enter để quay lại menu chính.---
---Nhấn phím khác để thoát.---""")

def baitap1():
    nhap = list(map(float,input("nhập 3 cạnh a,b,c (cách nhau bởi dấu cách): ").strip().split()))
    p=sum(nhap)/2
    if(p<=0) or (p-(min(nhap))<=0):
        print("không có tam giác nào)")
        return p
    s=(p*(p-nhap[0])*(p-nhap[1])*(p-nhap[2]))**0.5
    print(f"diện tích tam giác là: {round(s,6)}")

def baitap2():
    print("giải phương trình bậc 2: ax^2 + bx + c = 0")
    a,b,c=map(float,input("nhập các hệ số a,b,c (cách nhau bởi dấu cách): ").strip().split())
    if a==0:
        if b==0:
            if c==0:
                print("phương trình có vô số nghiệm")
            else:
                print("phương trình vô nghiệm")
        else:
            x=-c/b
            print(f"phương trình có một nghiệm x={round(x,6)}")
    else:
        d=b**2-4*a*c
        if d<0:
            print("phương trình vô nghiệm")
        elif d==0:
            x=-b/(2*a)
            print(f"phương trình có nghiệm kép x1=x2={round(x,6)}")
        else:
            x1=(-b+math.sqrt(d))/(2*a)
            x2=(-b-math.sqrt(d))/(2*a)
            print(f"phương trình có hai nghiệm phân biệt:\nx1={round(x1,6)}\nx2={round(x2,6)}")

def test():
    print("""\nNhấn phím 1 để kiểm tra thêm
Nhấn phím 2 để xem code mẫu
nhấn phím Enter để quay lại menu chính
Nhấn phím khác để thoát""")
    tep=input("bạn muốn làm gì?: ").strip()
    return tep

codemau1="""\n - nhap = map(float,input("nhập 3 cạnh a,b,c (cách nhau bởi dấu cách): ").strip().split())
    p=sum(nhap)/2
    if(p<=0) or (p-(min(nhap))<=0):
        print("không có tam giác nào)")
        return p
    s=(p*(p-nhap[0])*(p-nhap[1])*(p-nhap[2]))**0.5
    print(f"diện tích tam giác là: {round(s,6)}")
\n - vậy là chúng ta đã tinh được diện tích tam giác rồi thật tuyệt vời đúng không?"""

codemau2="""\n - print("giải phương trình bậc 2: ax^2 + bx + c = 0")
    a,b,c=map(float,input("nhập các hệ số a,b,c (cách nhau bởi dấu cách): ").strip().split())
    if a==0:
        if b==0:
            if c==0:
                print("phương trình có vô số nghiệm")
            else:
                print("phương trình vô nghiệm")
        else:
            x=-c/b
            print(f"phương trình có một nghiệm x={round(x,6)}")
    else:
        d=b**2-4*a*c
        if d<0:
            print("phương trình vô nghiệm")
        elif d==0:
            x=-b/(2*a)
            print(f"phương trình có nghiệm kép x1=x2={round(x,6)}")
        else:
            x1=(-b+math.sqrt(d))/(2*a)
            x2=(-b-math.sqrt(d))/(2*a)
            print(f"phương trình có hai nghiệm phân biệt:\nx1={round(x1,6)}\nx2={round(x2,6)}")
\n - vậy là chúng ta đã giải được phương trình bậc 2 rồi thật tuyệt vời đúng không?"""

def main():
    show()
    luachon = input("\nMời bạn nhập lựa chọn của mình: ").strip()
    if luachon == "36":
        while True:
            print("\nBài tập ví dụ về int:")
            print(baitap) 
            bt=input("bạn muốn làm bài tập nào?: ").strip()
            if(bt=="1"):
                print("\ntính diện tích tam giác có 3 cạnh a b c.")
                while True:
                    baitap1()
                    t=test()
                    if(t=="1"):
                        continue
                    elif(t=="2"):
                        print(codemau1)
                        break
                    else:
                        if t != "":
                            print("\ncảm ơn bạn đã sử dụng chương trình")
                            sys.exit()
                        else:
                            break
            elif(bt=="2"):
                print("\ngiải phương trình bậc 2 có dạng ax^2 + bx + c = 0.")
                while True:
                    baitap2()
                    t=test()
                    if(t=="1"):
                        continue
                    elif(t=="2"):
                        print(codemau2)
                        break
                    else:
                        if t != "":
                            print("\ncảm ơn bạn đã sử dụng chương trình")
                            sys.exit()
                        else:
                            break
            elif bt == "":
                break
            else:
                sys.exit()
    elif luachon != "":
        print("\ncảm ơn bạn đã sử dụng chương trình*")
        sys.exit()
if __name__ == "__main__":
    main()