# -*- coding: utf-8 -*-
import sys
import math
ham_chucnang =[
            "len(s) — độ dài chuỗi — len('hello') → 5.",
            "s[i] — ký tự tại index i — 'abc'[1] → 'b'.",
            "s[a:b] — cắt chuỗi — 'abcdef'[1:4] → 'bcd'.",
            "s + t — nối chuỗi — 'hi'+'!' → 'hi!'.",
            "s * n — lặp chuỗi — 'ha'*3 → 'hahaha'.",
            "s.lower() — chuyển thường — 'HeLLo'.lower() → 'hello'.",
            "s.upper() — chuyển hoa — 'HeLLo'.upper() → 'HELLO'.",
            "s.capitalize() — viết hoa chữ cái đầu — 'python'.capitalize() → 'Python'.",
            "s.title() — viết hoa đầu mỗi từ — 'hello world'.title() → 'Hello World'.",
            "s.strip() — bỏ khoảng trắng 2 đầu — ' hi '.strip() → 'hi'.",
            "s.lstrip(), s.rstrip() — bỏ khoảng trắng trái/phải.",
            "s.split(sep) — tách thành list — 'a,b,c'.split(',') → ['a','b','c'].",
            "'sep'.join(lst) — nối list thành chuỗi — '-'.join(['a','b']) → 'a-b'.",
            "s.find(x) — tìm x (hoặc -1 nếu không có) — 'banana'.find('na') → 2.",
            "s.index(x) — tìm x (lỗi nếu không có) — 'banana'.index('na') → 2.",
            "s.replace(a,b) — thay thế — 'a-b-c'.replace('-','_') → 'a_b_c'.",
            "s.startswith(x) — kiểm tra tiền tố — 'hello'.startswith('he') → True.",
            "s.endswith(x) — kiểm tra hậu tố — 'hello'.endswith('lo') → True.",
            "s.isdigit() — toàn số — '123'.isdigit() → True.",
            "s.isalpha() — toàn chữ — 'abc'.isalpha() → True.",
            "s.isalnum() — chữ + số — 'abc123'.isalnum() → True.",
            "s.isspace() — toàn khoảng trắng — '   '.isspace() → True.",
            "min(s), max(s) — ký tự nhỏ nhất/lớn nhất theo bảng Unicode.",
            "sorted(s) — list ký tự đã sắp xếp — sorted('cba') → ['a','b','c'].",
            "f-string / format — chèn biến — name='Bob'; f'Hi {name}' → 'Hi Bob'."
            ]

baitap = """- Nhấm phím 1 để làm bài tập 1: Tính diện tích tam giác biết 3 cạnh a,b,c(m).
- Nhấm phím 2 để làm bài tập 2: Bài toán giải phương bậc 2 (làm tròn đến số thập phân thứ 6).
- Nhấm phím Enter để quay lại menu chính
- Nhấn phím khác để thoát."""

def show():
    print(f"\n=== Chào mừng bạn đến với string (chuỗi) ===")
    print("• Cú pháp: s='Xin chào',dùng ''' hoặc \"\"\" cho chuỗi nhiều dòng.")
    print("• Cấu trúc: Bất biến; Unicode.")
    print("• Áp dụng: Tiền xử lý, parsing, regex, NLP đơn giản.")
    print("• Note: Nối nhiều lần → dùng join; để ý encode/decode.")
    print("• Hàm/phương thức thường gặp:")
    for f in ham_chucnang:
        print("   -", f)
    print(f"""\nChúc mừng bạn vừa tìm hiểu xong về cấu trúc string!
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