from fractions import Fraction
#dictionary: value account
accounts= {
    "admin":{
        "password":"241206",     #str
        "balance" : 2000.5,      #float
        "secure_key": 4+5j,      #complex
        "discount": Fraction(1,5)#Fraction
    }
}
#dict
#hàm kiểm tra thông tin đăng nhập(function)
def check_login(user_name:str,password:str) -> bool:
    return user_name in accounts and accounts[user_name]["password"]==password
#hàm in kết quả đăng nhập(procedure)
def print_result(success:bool) -> None:
    if success:
        print("Đăng nhập thành công!")
    else:
        print("Sai tài khoản hoặc mật khẩu! Vui lòng nhập lại.")
#hàm hiển thị thông tin tài khoản
def show_account_infor(user_name:str) -> None:
    acc=accounts[user_name]
    print(f"/n=== Thông tin tài khoản [{user_name}] ===")
    print(f" Số dư tài khoản: {acc['balance']}VND ")
    print(f" Khóa bảo mật: {acc['secure_key']}")
    print(f" Khuyến mại: {acc['discount']}={float(acc['discount'])*100:.1f}%")
#hàm main 
def login_system():
    #gán int
    attempts=0
    #while loop
    while attempts <3:
        user=input("Nhập username: ")
        pw=input("Nhập mật khẩu: ")
        success=check_login(user,pw)
        print_result(success)
        # điều kiện
        if success:
            show_account_infor(user)
            return
        attempts +=1
        print(f"Bạn còn {3-attempts} lần thử!")
    print("Tài khoản đã bị khóa do bạn đã nhập quá 3 lần!")
if __name__=="__main__":
    login_system()