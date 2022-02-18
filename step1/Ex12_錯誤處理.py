try:
    n = float(input("輸入浮點數"))
except ValueError:
    print("請輸入浮點數")
except:
    print("test2")
else:
    print("沒問題")
finally:
    print("完成")