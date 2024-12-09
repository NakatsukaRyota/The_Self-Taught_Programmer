answer_list = ["2", "5"]

while(True):
    ans = input("数字を入力してください('q'で終了する)")
    
    if ans == "q":
        break

    if ans.isdigit():
        if ans in answer_list:
            print("正解！")
        else: 
            print("不正解")
    else:
        if (ans == "q"):
            break
        else:
            print("数字を入力するか、qで終了します")