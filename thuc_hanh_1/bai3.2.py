import cmath
def giai_bac_2_he_so_phuc():
    print("--- Giải phương trình bậc 2 với hệ số phức ---")
    print("Nhập số phức theo định dạng 'a+bj' (Ví dụ: 1+2j hoặc 3j hoặc 5)")

    try:
        a = complex(input("Nhập hệ số a: "))
        if a == 0:
            print("Hệ số a phải khác 0!")
            return

        b = complex(input("Nhập hệ số b: "))
        c = complex(input("Nhập hệ số c: "))
        delta = b ** 2 - 4 * a * c
        sqrt_delta = cmath.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2 * a)
        x2 = (-b - sqrt_delta) / (2 * a)

        print("-" * 30)
        print(f"Delta = {delta}")
        print(f"Nghiệm x1 = {x1}")
        print(f"Nghiệm x2 = {x2}")

    except ValueError:
        print("❌ Định dạng không hợp lệ! Hãy nhập đúng kiểu '1+2j'.")

giai_bac_2_he_so_phuc()