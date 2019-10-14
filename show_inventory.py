import csv
import copy

#ソートオプション
#カテゴリー
#在庫数
#商品番号
class Show_inventory:
    def __init__(self):
        self.menus = {"1":"在庫の表示","2":"条件の指定","3":"ソート方法の指定","4":"終了"}
        self.all_products = list()
        self.conditioned_products = list()
        self.condition = [["1","カテゴリー",0]]
        self.sorts = list()

        self.menu()

    def menu(self):
        self.road_current()
        if len(self.all_products) <= 50:
            self.show()

        while True:
            print("-"*21+"在庫表示"+"-"*21)
            print("-"*50)
            for i,j in self.menus.items():
                print(i.ljust(3),"|",j.center(28))
            print("-"*50)

            select = input()
            if select == "1":
                self.update_products()
            elif select == "2":
                self.set_condition()
            elif select == "3":
                self.sorts()
                self.show()
            elif select == "4":
                break
            else:
                print("入力されたオプション番号に誤りがあります")
                continue

    def set_condition(self):
        while True:
            print("-"*20+"現在の条件指定"+"-"*20)
            for i in self.condition:
                print(i[0].ljust(3),"|",i[1].center(24),"|",end="")
                if i[2] == 0:
                    print("設定されていません")
                else:
                    print("設定されています")
            print("-"*48)

            select = input("変更したい場合は条件のオプション番号と(1(設定)または0(設定解除))を半角スペース区切りで入力してください(終了する場合はe)")
            try:
                if select == "e":
                    break
                else:
                    select = select.split()
                    self.condition[int(select[0])-1][2] = int(select[1])
            except:
                print("入力方法に誤りがあります")


    def set_sorts(self):
        #ソート方法の指定を行います
        pass

    def update_products(self):
        #指定された条件とソート方法で表示対象のリストを更新します
        pass

    def road_current(self):
        with open("books_info/current.csv","r") as f:
            reader = csv.reader(f)
            for i in reader:
                self.all_products.append([i[0],i[1],int(i[2])])
        self.conditioned_products = copy.deepcopy(self.all_products)

    def show(self):
        print("-"*50)
        print("{:-^14}{:-^20}{:-^7}".format("商品番号","商品名","個数"))
        for i in self.conditioned_products:
            print("{0[0]:^18}|{0[1]:^20}|{0[2]:>10}|".format(i))
