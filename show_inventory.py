import csv
import copy

#ソートオプション
#カテゴリー
#在庫数
#商品名
class Show_inventory:
    def __init__(self):
        self.all_products = list()
        self.conditioned_products = list()
        self.menu()

    def menu(self):
        self.road_current()
        self.show()
        while True:
            print("-----------在庫表示-----------")
            print("------------------------------")
            input()

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
            print("{0[0]:^18}|{0[1]:^20}|{0[2]:>7}|".format(i))
