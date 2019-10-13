
menus = {1:"在庫表示",2:"在庫情報の編集",3:"終了"}

while True:
    print("-----------在庫管理システム-----------")
    print("-----------基本操作メニュー-----------")
    for i,j in menus.items():
        print(str(i).ljust(3),"|",j.center(22))
    input()
