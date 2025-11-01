# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」


ans = 57

while True:
    user_input = input("請輸入1~100的數字:")
    user_input = int(user_input)
    if user_input < 1 or user_input > 100:
        print("超出範圍請重新輸入")
    elif user_input > ans:
        print("請輸入更小的數字")
    elif user_input < ans:
        print("請輸入更大的數字")
    else:
        print("恭喜中獎")
        break



ans = 57
user_input = "aaa"

while user_input != ans :
    user_input = input("請輸入1~100的數字:")
    user_input = int(user_input)
    if user_input < 1 or user_input > 100:
        print("超出範圍請重新輸入")
    elif user_input > ans:
        print("請輸入更小的數字")
    elif user_input < ans:
        print("請輸入更大的數字")
    
print("恭喜中獎")
    






