def ve_cay_thong():
    print("--- Chương trình vẽ cây thông Noel ---")
    while True:
        try:
            h = int(input("Nhập độ cao tổng của cây (h > 2): "))
            if h <= 2:
                print("Độ cao phải lớn hơn 2 để có phần thân và gốc!")
                continue
            break
        except ValueError:
            print("❌ Lỗi: Vui lòng nhập một số nguyên!")
    h_la = h - 2
    for i in range(1, h_la + 1):
        print(" " * (h_la - i), end="")
        print("x" * (2 * i - 1))
    for _ in range(2):
        print(" " * (h_la - 1) + "x")
ve_cay_thong()