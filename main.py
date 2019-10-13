
menus = {"1":"在庫表示","2":"在庫情報の編集","3":"終了"}

while True:
    print("-----------在庫管理システム-----------")
    print("-----------基本操作メニュー-----------")
    for i,j in menus.items():
        print(i.ljust(3),"|",j.center(22))

    select = input("操作したいオプション番号を入力してください")

    if i == "1":
        pass
    elif i == "2":
        pass
    elif i == "3":
        break
    else:
        print("入力された番号に誤りがあります")
