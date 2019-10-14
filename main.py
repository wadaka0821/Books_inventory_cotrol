import show_inventory
import file_operation

menus = {"1":"在庫表示","2":"在庫情報の編集","3":"終了"}
#在庫入出荷履歴の表示に対応する必要あり

while True:
    print("-----------在庫管理システム-----------")
    print("-----------基本操作メニュー-----------")
    for i,j in menus.items():
        print("{:<3}{}{:^24}".format(i,"|",j,))
    print("--------------------------------------")

    select = input("操作したいオプション番号を入力してください\n")

    if select == "1":
        #current.csvの表示のみ addとsubはなし
        show_inventory.Show_inventory()
    elif select == "2":
        file_operation.File_operation()
    elif select == "3":
        break
    else:
        print("入力された番号に誤りがあります")
