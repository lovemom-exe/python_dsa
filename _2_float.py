# -*- coding: utf-8 -*-
import sys
import math
ham_chucnang =[
            "float(x) — ép kiểu sang float — float('3.14') → 3.14.",
            "round(x, n) — làm tròn x đến n chữ số sau dấu chấm — round(3.14159, 2) → 3.14.",
            "abs(x) — trị tuyệt đối — abs(-2.5) → 2.5.",
            "math.floor(x) — làm tròn xuống — math.floor(3.9) → 3.",
            "math.ceil(x) — làm tròn lên — math.ceil(3.1) → 4.",
            "math.trunc(x) — cắt phần thập phân — math.trunc(3.9) → 3.",
            "math.isclose(a, b) — so sánh 2 số float có gần bằng nhau không.",
            "math.isnan(x) — kiểm tra NaN (Not a Number).",
            "math.isinf(x) — kiểm tra vô cực (inf, -inf).",
            ]

baitap = """- Nhấm phím 1 để làm bài tập 1: Tính diện tích tam giác biết 3 cạnh a,b,c(m).
- Nhấm phím 2 để làm bài tập 2: Bài toán giải phương bậc 2 (làm tròn đến số thập phân thứ 6).
- Nhấm phím Enter để quay lại menu chính
- Nhấn phím khác để thoát."""

def show():
    print(f"\n=== Chào mừng bạn đến với float (số thực) ===")
    print("• Cú pháp: x = 3.14; y = float('1e-3'); round(x, 2); math.isclose(a,b)")
    print("• Cấu trúc: Dạng dấu phẩy động đôi (64-bit); toán tử + - * / // % **.")
    print("• Áp dụng: Tính toán xấp xỉ, đo lường, hình học, xác suất.")
    print("• Note: Tránh so sánh bằng ==; dùng math.isclose().")
    print("• Hàm/phương thức thường gặp:")
    for f in ham_chucnang:
        print("   -", f)
    print(f"""\nChúc mừng bạn vừa tìm hiểu xong về cấu trúc float!
\n---Nhấn phím 36 để đến với bài tập ví dụ---
---Nhấn phím Enter để quay lại menu chính.---
---Nhấn phím khác để thoát.---""")

def baitap1():
    a,b,c= map(float,input("nhập 3 cạnh a,b,c (cách nhau bởi dấu cách): ").strip().split())
    p=sum([a,b,c])/2
    if a<=0 or b<=0 or c<=0 or a+b<=c or a+c<=b or b+c<=a:
        print("không phải số đo 3 cạnh của tam giác)")
        return p
    s=(p*(p-a)*(p-b)*(p-c))**0.5
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

codemau1="""\n - a,b,c= map(float,input("nhập 3 cạnh a,b,c (cách nhau bởi dấu cách): ").strip().split())
    p=sum([a,b,c])/2
    if a<=0 or b<=0 or c<=0 or a+b<=c or a+c<=b or b+c<=a:
        print("không phải số đo 3 cạnh của tam giác)")
        return p
    s=(p*(p-a)*(p-b)*(p-c))**0.5
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