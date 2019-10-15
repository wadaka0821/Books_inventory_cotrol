import re
import datetime
import csv
import shutil
import os

#追加予定機能：１０個ほどのcurrent更新履歴を保管し、以前の状態を復帰できるようにする
#履歴保存は終了
#あと復帰用メソッドの作成

class File_operation:
    def __init__(self):
        self.menus = {"1":"ファイル読み込み","2":"ファイル名の指定(初期値はrs_list.csv)","3":"現在の指定されたファイル名の表示","4":"終了"}
        self.categories = dict()
        self.input_filename = "rs_list.csv"
        self.current = dict()

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
        adding_list = list()

        self.road_current()

        with open(self.input_filename,"r") as f:
            reader = csv.reader(f)
            warning = list()
            #在庫数が負になっても警告なし
            for i in reader:
                if i[0] in self.current:
                    self.current[i[0]][1] += int(i[2])
                else:
                    self.current.update({i[0]:[i[1],int(i[2])]})
                if self.current[i[0]][1] < 0:
                    warning.append(i[0])

                if int(i[2]) > 0:
                    add_list.append([time]+i)
                elif int(i[2]) < 0:
                    sub_list.append([time]+i)
            for i,j in self.current.items():
                adding_list.append([i]+j)
            #warning に要素がある場合に警告を行います
            if len(warning) > 0:
                print("エラー商品番号")
                for i in warning:
                    print(i)
                select = input("ファイルの読み込み時に在庫数が負になったものがあります\n読み込みを続行しますか?(yes or no)")
                if select == "no":
                    print("読み込みを中止しました")
                    return None

            self.save_history()

            self.writerow_file(adding_list,"books_info/current/current1.csv","w")
            self.writerow_file(add_list,"books_info/time_log/add.csv","a")
            self.writerow_file(sub_list,"books_info/time_log/sub.csv","a")

    def road_current(self):
        with open("books_info/current/current1.csv","r") as f:
            reader = csv.reader(f)
            for i in reader:
                if i[0] not in self.current:
                    self.current.update({i[0]:[i[1],int(i[2])]})

    def save_history(self):
        os.remove("books_info/current/current10.csv")
        for i in range(9,0,-1):
            file_new = "books_info/current/current" + str(i+1) + ".csv"
            file = "books_info/current/current" + str(i) + ".csv"

            shutil.move(file,file_new)


    def writerow_file(self,write_list,original_file,mode):
        with open(original_file,mode) as f:
            writer = csv.writer(f)
            writer.writerows(write_list)
