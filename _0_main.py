# -*- coding: utf-8 -*-

import _1_int
import _2_float
import _3_bool
import _4_complex
import _5_Fraction
import _6_list
import _7_ma_tran
import _8_set
import _9_tuple
import _10_range
import _11_string
import _12_dict
import _13_enumerate
import _14_deque

MENU = """
Bạn muốn tìm hiểu về kiểu dữ liệu / công cụ nào:
01. int         06. list        11. string
02. float       07. ma_tran     12. dict
03. bool        08. set         13. enumerate
04. complex     09. tuple       14. deque
05. Fraction    10. range
(Ấn 00 để thoát)
"""

# Lưu hàm, KHÔNG gọi ngay (bỏ dấu ())
data = {
    "01": _1_int.main,
    "02": _2_float.main,
    "03": _3_bool.main,
    "04": _4_complex.main,
    "05": _5_Fraction.main,
    "06": _6_list.main,
    "07": _7_ma_tran.main,
    "08": _8_set.main,
    "09": _9_tuple.main,
    "10": _10_range.main,
    "11": _11_string.main,
    "12": _12_dict.main,
    "13": _13_enumerate.main,
    "14": _14_deque.main,
}

def main():
    while True:
        print(MENU)
        luachon = input("Mời bạn nhập lựa chọn của mình: ").strip()
        if luachon == "00":
            print("Cảm ơn bạn đã sử dụng chương trình.")
            break
        elif luachon in data:
            data[luachon]()
        else:
            print("\nLỰA CHỌN KHÔNG HỢP LỆ, MỜI BẠN NHẬP LẠI!")

if __name__ == "__main__":
    main()