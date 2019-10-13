import re
import datetime
import csv

class File_operation:
    def __init__(self):
        self.menus = {"1":"ファイル読み込み","2":"ファイル名の指定(初期値はrs_list.csv)","3":"現在の指定されたファイル名の表示","4":"終了"}
        self.categories = dict()
        self.input_filename = "rs_list.csv"

        self.menu()

    def menu(self):
        while True:
            print("-----------ファイル操作-----------")
            for i,j in self.menus.items():
                print("{:<3}{}{:^26}".format(i,"|",j))
            print("----------------------------------")

            select = input("選択したいオプション番号を入力してください\n")
            if select == "1":
                self.road_file()
            elif select == "2":
                name = input("ファイル名を入力してください(csv形式)")
                if re.search(r".+\.csv",name):
                    self.input_filename = name
                else:
                    print("ファイル名に誤りがあります")
            elif select == "3":
                print("現在指定されているファイル名：",self.input_filename)
            elif select == "4":
                break
            else:
                print("入力されたオプション番号に誤りがあります")

    def road_file(self):
        time = datetime.datetime.today()
        add_list = list()
        sub_list = list()

        with open(self.input_filename,"r") as f:
            reader = csv.reader(f)
            for i in reader:
                if int(i[3]) > 0:
                    add_list.append(i)
                elif int(i[3]) < 0:
                    sub_list.append(i)

        with open("books_info/time_log/add.csv","a") as f:
            writer = csv.writer(f)
            for i in add_list:
                writer.writerow([time]+i)

        with open("books_info/time_log/sub.csv","a") as f:
            writer = csv.writer(f)
            for i in sub_list:
                writer.writerow([time]+i)
