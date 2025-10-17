# -*- coding: utf-8 -*-
import sys
import math
ham_chucnang =[
            "int(x, base=10) — ép kiểu int từ str/float; hỗ trợ cơ số — int('101', 2) → 5.",
            "abs(x) — trị tuyệt đối — abs(-10) → 10.",
            "pow(x, y[, mod]) — lũy thừa (có thể kèm modulo) — pow(2, 5) → 32.",
            "round(x[, n]) — làm tròn số (n chữ số thập phân) — round(3.6) → 4.",
            "divmod(a, b) — trả về (thương, dư) — divmod(17, 5) → (3, 2).",
            "max(a, b, …) — giá trị lớn nhất — max(3, 7, 5) → 7.",
            "min(a, b, …) — giá trị nhỏ nhất — min(3, 7, 5) → 3.",
            "sum(iterable) — tổng các phần tử — sum([1, 2, 3]) → 6.",
            "bin(x) — đổi sang nhị phân (chuỗi, prefix 0b) — bin(5) → '0b101'.",
            "oct(x) — đổi sang bát phân (chuỗi, prefix 0o) — oct(8) → '0o10'.",
            "hex(x) — đổi sang thập lục phân (chuỗi, prefix 0x) — hex(26) → '0x1a'.",
            "x.bit_length() — số bit cần để biểu diễn x (không dấu) — (5).bit_length() → 3."
            ]

baitap = """- Nhấm phím 1 để làm bài tập 1: kiểm tra số hoàn hảo.
- Nhấm phím 2 để làm bài tập 2: Liệt kê tất cả các số nguyên tố trong khoảng từ 1 đến n.
- Nhấm phím Enter để quay lại menu chính
- Nhấn phím khác để thoát."""

def show():
    print(f"\n=== Chào mừng bạn đến với int (số nguyên) ===")
    print("• Cú pháp: x = 42; y = int('101', 2); bin(x); x.bit_length()")
    print("• Cấu trúc: Số nguyên không giới hạn; toán tử + - * // % ** & | ^ << >>.")
    print("• Áp dụng: Đếm, chỉ số, toán học tổ hợp, mã hoá.")
    print("• Note: / trả về float kể cả khi chia hết; dùng // để chia lấy phần nguyên.")
    print("• Hàm/phương thức thường gặp:")
    for f in ham_chucnang:
        print("   -", f)
    print(f"""\nChúc mừng bạn vừa tìm hiểu xong về cấu trúc int!
\n---Nhấn phím 36 để đến với bài tập ví dụ---
---Nhấn phím Enter để quay lại menu chính.---
---Nhấn phím khác để thoát.---""")
def baitap1():
    n=int(input("nhập số cần kiểm tra: "))
    if(n<0) or type(n)!=int:
        print(f"số {n} không phải số hoàn hảo vì số hoàn hảo là số tự nhiên > 0")
    else:
        denta=1+8*n
        x=math.log((denta**0.5+1)/2,2)
        if int(x)!=x:
            print(f"số {n} không là số hoàn hảoo")
            return x
        for i in range(2,int(math.sqrt(x)+1)):
            if(x%i==0):
                print(f"số {n} không là số hoàn hảo")
                return x
        for i in range(2,int(math.sqrt(2**x-1))+1):
            if(2**x-1)%2==0:
                print(f"số {n} không là số hoàn hảo")
                return x
        print(f"số {n} là số hoàn hảo")

def baitap2():
    """ - dùng phương pháp sàng số nguyên tố."""
    n=int(input("nhập số tự nhiên n: "))
    if(n<2) or type(n)!=int:
        print(f"không có số nguyên tố nào trong khoảng từ 1 đến {n}")
        return n
    dssont = [True] * (n + 1)  # mặc định: mọi số đều là nguyên tố
    dssont[0] = dssont[1] = False  # 0 và 1 không phải nguyên tố
    p = 2
    while p * p <= n:
        if dssont[p]:
            # Gạch các bội số của p
            for i in range(p * p, n + 1, p):
                dssont[i] = False
        p += 1
    # in ra danh sách các số nguyên tố
    print(f"danh sách các số nguyên tố từ 1 đến {n} là:",[i for i in range(n + 1) if dssont[i]])

def test():
    print("""\nNhấn phím 1 để kiểm tra thêm
Nhấn phím 2 để xem code mẫu
nhấn phím Enter để quay lại menu chính
Nhấn phím khác để thoát""")
    tep=input("bạn muốn làm gì?: ").strip()
    return tep
codemau1="""\n - ta có nếu p là số nguyên tố và 2^p - 1 cũng là số nguyên tố thì số hoàn hảo sẽ là 2^(p-1)*(2^p - 1) 
import math
    n=int(input("nhập số cần kiểm tra: "))
    if(n<0) or type(n)!=int:
        print(f"số {n} không phải số hoàn hảo vì số hoàn hảo là số tự nhiên > 0")
    else:   #đặt x=2^p ta có x*x-x-2*n=0
        denta=1+8*n
        p=math.log((denta**0.5+1)/2,2)  #giải phương trình ta được p
        if int(p)!=p:
            print(f"số {n} không là số hoàn hảo")   
            return p
        for i in range(2,int(math.sqrt(p)+1)):  #kiểm tra p có phải số nguyên tố không
            if(p%i==0):
                print(f"số {n} không là số hoàn hảo")
                return p
        for i in range(2,int(math.sqrt(2**p-1))+1):  #kiểm tra 2^p-1 có phải số nguyên tố không
            if(2**p-1)%2==0:
                print(f"số {n} không là số hoàn hảo")
                return p
        print(f"số {n} là số hoàn hảo")
\n - đây là code tham khảo ngoài ra bạn có thể tạo list để kiểm tra số hoàn hảo từ trước vì số hòan hảo rất hiếm
ví dụ list=[6,28,496,8128,33550336,...]"""
codemau2=""" \n - dùng phương pháp sàng số nguyên tố.
    n=int(input("nhập số tự nhiên n: "))
    if(n<2) or type(n)!=int:
        print(f"không có số nguyên tố nào trong khoảng từ 1 đến {n}")
        return n
    dssont = [True] * (n + 1)  # mặc định: mọi số đều là nguyên tố
    dssont[0] = dssont[1] = False  # 0 và 1 không phải nguyên tố
    p = 2
    while p * p <= n:
        if dssont[p]:
            # Gạch các bội số của p
            for i in range(p * p, n + 1, p):
                dssont[i] = False
        p += 1
    # in ra danh sách các số nguyên tố
    print(f"danh sách các số nguyên tố từ 1 đến {n} là:",[i for i in range(n + 1) if dssont[i]])
\n - bạn thấy chương trình này có hay không?"""
def main():
    show()
    luachon = input("\nMời bạn nhập lựa chọn của mình: ").strip()
    if luachon == "36":
        while True:
            print("\nBài tập ví dụ về int:")
            print(baitap) 
            bt=input("bạn muốn làm bài tập nào?: ").strip()
            if(bt=="1"):
                print("\nsố hoàn hảo là số mà tổng tất cả các ước số của nó (không bao gồm chính nó) bằng chính nó.")
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
                print("\nsố hoàn hảo là số mà tổng tất cả các ước số của nó (không bao gồm chính nó) bằng chính nó.")
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