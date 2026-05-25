import cmath
def giai_phuong_trinh_bac2_he_so_thuc():
    try:
        a=float(input('Nhập vào hệ số a:'))
        if a==0:
            print("Đây không phải phương trình bậc 2!")
            return

        b = float(input('Nhập vào hệ số b:'))
        c = float(input('Nhập vào hệ số c:'))
        delta=b**2-4*a*c
        x1 = (-b+cmath.sqrt(delta))/(2*a)
        x2 = (-b-cmath.sqrt(delta))/(2*a)
        if delta>0:
            print('Phương trình có 2 nghiệm thực phân biệt:')
            print(f"x1 = {x1.real:.2f}")
            print(f"x2 = {x2.real:.2f}")
        elif delta == 0:
            print(f"Phương trình có nghiệm kép: x = {x1.real:.2f}")
        else:
            print(f"Phương trình có 2 nghiệm phức liên hợp:")
            print(f"x1 = {x1.real:.2f} + {x1.imag:.2f}j")
            print(f"x2 = {x2.real:.2f} + {x2.imag:.2f}j")
    except ValueError:
        print('Hãy nhập vào 1 số thực')
giai_phuong_trinh_bac2_he_so_thuc()


