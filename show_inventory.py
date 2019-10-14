import csv

#ソートオプション
#カテゴリー
#在庫数
#商品名
class Show_inventory:
    def __init__(self):
        self.products = list()
        self.menu()

    def menu(self):
        self.road_current()
        self.show_all()
        while True:
            print("-----------在庫表示-----------")
            print("------------------------------")
            input()

    def road_current(self):
        with open("books_info/current.csv","r") as f:
            reader = csv.reader(f)
            for i in reader:
                self.products.append([i[0],i[1],int(i[2])])

    def show_all(self):
        pass
