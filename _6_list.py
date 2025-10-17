# -*- coding: utf-8 -*-
import sys
import math
ham_chucnang =[
            "len(lst) — số phần tử — len([1,2,3]) → 3.",
            "lst.append(x) — thêm 1 phần tử vào cuối — a=[1,2]; a.append(3) → [1,2,3].",
            "lst.extend(iterable) — nối nhiều phần tử — a=[1]; a.extend([2,3]) → [1,2,3].",
            "lst.insert(i, x) — chèn x vào vị trí i — a=[1,3]; a.insert(1,2) → [1,2,3].",
            "lst.remove(x) — xóa phần tử đầu tiên có giá trị x — [1,2,2].remove(2) → [1,2].",
            "lst.pop([i]) — lấy & xóa phần tử tại i (mặc định cuối) — a=[1,2,3]; a.pop() → 3, a=[1,2].",
            "lst.clear() — xóa toàn bộ list — a=[1,2]; a.clear() → [].",
            "lst.index(x) — vị trí đầu tiên của x — [1,2,3,2].index(2) → 1.",
            "lst.count(x) — đếm số lần xuất hiện x — [1,2,2,3].count(2) → 2.",
            "lst.sort() — sắp xếp in-place tăng dần — a=[3,1,2]; a.sort() → [1,2,3].",
            "lst.reverse() — đảo ngược in-place — a=[1,2,3]; a.reverse() → [3,2,1].",
            "sorted(lst) — trả về list mới đã sắp xếp — sorted([3,1,2]) → [1,2,3].",
            "reversed(lst) — iterator đảo ngược — list(reversed([1,2,3])) → [3,2,1].",
            "sum(lst) — tính tổng — sum([1,2,3]) → 6.",
            "max(lst), min(lst) — lớn nhất/nhỏ nhất — max([1,5,2]) → 5.",
            "any(lst) — True nếu có ít nhất 1 phần tử truthy — any([0, '', 5]) → True.",
            "all(lst) — True nếu tất cả truthy — all([1,2,3]) → True; all([1,0,3]) → False.",
            "enumerate(lst) — lấy cả index & value — list(enumerate(['a','b'])) → [(0,'a'), (1,'b')].",
            "zip(lst1, lst2, …) — ghép nhiều list song song — list(zip([1,2],[3,4])) → [(1,3),(2,4)].",
            "listcomp — [f(x) for x in a if cond] để lọc/biến đổi nhanh.",
            "lst[::-1] — đảo ngược list — [1,2,3][::-1] → [3,2,1].",
            "map(hàm, dãy_dữ_liệu) — áp hàm cho từng phần tử trong dãy và trả về dãy.",
            "split() — tách chuỗi thành các phần tử trong list (mặc định tách theo dấu cách).",
            "join() — nối các phần tử trong list thành chuỗi (mặc định nối bằng dấu cách) → \"ký_tự_ngăn_cách\".join(map(str,danh_sách_list)).",
            "lambda x: x * 2 — hàm ẩn danh (không tên) nhận tham số x và trả về x*2.",
            "filter(hàm, dãy_dữ_liệu) — lọc các phần tử trong dãy dựa trên hàm trả về True/False → list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])) → [2, 4].",
            "[x for x in lst if điều_kiện] — list comprehension để tạo list mới từ lst với điều kiện lọc."
            ]

baitap = """- Nhấm phím 1 để làm bài tập 1: Tính diện tích tam giác biết 3 cạnh a,b,c(m).
- Nhấm phím 2 để làm bài tập 2: Bài toán giải phương bậc 2 (làm tròn đến số thập phân thứ 6).
- Nhấm phím Enter để quay lại menu chính
- Nhấn phím khác để thoát."""

def show():
    print(f"\n=== Chào mừng bạn đến với list(danh sách) ===")
    print("• Cú pháp: a=[1,2]; a[1:3]; [f(x) for x in a].")
    print("• Cấu trúc: Mảng động, có thứ tự, cho phép trùng.")
    print("• Áp dụng: Lưu chuỗi phần tử, DP, ngăn xếp nhỏ.")
    print("• Note: append/pop cuối O(1); chèn giữa O(n).")
    print("• Hàm/phương thức thường gặp:")
    for f in ham_chucnang:
        print("   -", f)
    print(f"""\nChúc mừng bạn vừa tìm hiểu xong về cấu trúc list!
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