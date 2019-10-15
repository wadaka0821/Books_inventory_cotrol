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
        #[インデックス、条件設定名、yes or no(1 or 0)]
        self.conditions = [["1","カテゴリー",0]]
        #[インデックス、ソート設定名、yes or no (1 or 0)、reverse設定]
        self.sorts = [["1","The number of inventory",0,False],["2","product index",1,False]]

        self.menu()

    def menu(self):
        init = self.road_current()
        if len(self.all_products) <= 50:
            self.show(init)

        while True:
            print("-"*21+"在庫表示"+"-"*21)
            print("-"*50)
            for i,j in self.menus.items():
                print(i.ljust(3),"|",j.center(28))
            print("-"*50)

            select = input()
            if select == "1":
                lis = self.update_products()
                self.show(lis)
            elif select == "2":
                self.set_condition()
            elif select == "3":
                self.set_sorts()
            elif select == "4":
                break
            else:
                print("入力されたオプション番号に誤りがあります")
                continue

    def set_condition(self):
        while True:
            print("-"*20+"現在の条件設定"+"-"*20)
            for i in self.conditions:
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
                    self.conditions[int(select[0])-1][2] = int(select[1])
            except:
                print("入力方法に誤りがあります")


    def set_sorts(self):
        #ソート方法の指定を行います
        while True:
            print("-"*20+"現在のソート指定"+"-"*20)
            for i in self.sorts:
                if i[2] == 1 and i[3] == True:
                    print("{:^50}".format(i[1]+"(reverse)"))
                    break
                elif i[2] == 1 and i[3] == False:
                    print("{:^50}".format(i[1]))
                    break
            else:
                self.sorts[1][2] = 1
                print("{:^50}".format(self.sorts[1][1]))
            print("-"*54)
            for i in self.sorts:
                print("{:<3}|{:^34}|".format(i[0],i[1]),end="")
                if i[2] == 1 and i[3] == True:
                    print("設定中(reverse)".center(16))
                elif i[2] == 1 and i[3] == False:
                    print("設定中".center(16))
                else:
                    print("-"*18)

            select = input("指定したい設定のオプション番号を入力してください(reverseさせる場合は半角スペース区切りで1)(終了する場合はe)\n").split()
            if select == ["e"]:
                break
            for i in self.sorts:
                if select[0] == i[0] and len(select) == 1:
                    i[2] = 1
                    i[3] = False
                elif select[0] == i[0] and len(select) == 2:
                    i[2] = 1
                    i[3] = True
                else:
                    i[2] = 0
                    i[3] = False

    def update_products(self):
        #指定された条件とソート方法で表示対象のリストを更新します
        #まず条件設定から必要な要素だけを取り出します

        if self.conditions[0][2] == 1:
            conditioned_products = list()
            select_category = set(input("探したいカテゴリーを半角スペース区切りで入力してください\n").split())
            conditioned_products = list()
            for i in self.all_products:
                if i[0][:2:] in select_category:
                    conditioned_products.append(i)

        #次にソート方法の設定からソートを行います
        if self.sorts[0][2] == 1:
            conditioned_products.sort(key=lambda x:x[2],reverse=self.sorts[0][3])
        elif self.sorts[1][2] == 1:
            conditioned_products.sort(key=lambda x:x[0][2::],reverse=self.sorts[1][3])

        return conditioned_products

    def road_current(self):
        with open("books_info/current.csv","r") as f:
            reader = csv.reader(f)
            for i in reader:
                self.all_products.append([i[0],i[1],int(i[2])])
        return copy.deepcopy(self.all_products)

    def show(self,conditioned_products):
        print("-"*50)
        print("{:-^14}{:-^20}{:-^7}".format("商品番号","商品名","個数"))
        for i in conditioned_products:
            print("{0[0]:^18}|{0[1]:^20}|{0[2]:>10}|".format(i))
