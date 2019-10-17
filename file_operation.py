import re
import datetime
import csv
import shutil
import os
import show_inventory

#追加予定機能：１０個ほどのcurrent更新履歴を保管し、以前の状態を復帰できるようにする
#履歴保存は終了
#復帰用メソッドも完成

class File_operation:
    def __init__(self):
        self.menus = {"1":"ファイル読み込み","2":"ファイル名の指定(初期値はrs_list.csv)","3":"現在の指定されたファイル名の表示","4":"以前の状態の復帰","5":"終了"}
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
                self.restore_menu()
            elif select == "5":
                break
            else:
                print("入力されたオプション番号に誤りがあります")

    def road_file(self):
        time = datetime.datetime.today()
        add_list = list()
        sub_list = list()
        adding_list = list()

        self.current = self.road_current("1","dic")

        with open(self.input_filename,"r") as f:
            reader = csv.reader(f)
            warning = list()
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

            print("正常にファイルの読み込みが完了しました")
            while True:
                select = input("読み込みを行ったファイルの内容を破棄しますか？（yes or no）（推奨）")
                if select == "yes":
                    with open(self.input_filename,"w") as f:
                        writer = csv.writer(f)
                        writer.writerow(list())
                    break
                elif == "no":
                    print("ファイル内容を保持しました")
                    break
                else:
                    print("正しい入力をしてください")

    def road_current(self,num,mode):
        ans = list()
        om = ""
        if mode == "dic":
            ans = dict()
            om = ans.update
        elif mode == "lis":
            ans = list()
            om = ans.append

        with open("books_info/current/current"+num+".csv","r") as f:
            
    def road_current(self):
        with open("books_info/current.csv","r") as f:
            reader = csv.reader(f)
            for i in reader:
                if mode == "dic":
                    om({i[0]:[i[1],int(i[2])]})
                else:
                    om(i)
        return ans

    def save_history(self):
        for i in range(10,0,-1):
            file_new = "books_info/current/current" + str(i+1) + ".csv"
            file = "books_info/current/current" + str(i) + ".csv"

            shutil.move(file,file_new)

    def restore_menu(self):
        while True:
            print("-"*50)
            for i in range(1,11,1):
                print(str(i).ljust(3),"|"," "*10,"current"+str(i)+".csv")
            print("-"*50)

            select = input("以前の状態を復帰したい場合：restore (番号)\nファイルの内容を確認したい場合：show (番号)\n終了：e\n").split()
            if select[0] == "restore":
                try:
                    self.restore(select[1])
                    print("正常に復帰が行われました")
                except:
                    print("入力方法か番号に誤りがあります")
            elif select[0] == "show":
                lis = self.road_current(select[1],"lis")
                #特例的なshowメソッドの呼び出し
                show_inventory.Show_inventory.show(None,lis)
            elif select[0] == "e":
                break
            else:
                print("入力方法に誤りがあります")

    def restore(self,file_num):
        shutil.copy("books_info/current/current"+file_num+".csv","books_info/current/temp.csv")
        self.save_history()
        shutil.move("books_info/current/temp.csv","books_info/current/current1.csv")

    def writerow_file(self,write_list,original_file,mode):
        with open(original_file,mode) as f:
            writer = csv.writer(f)
            writer.writerows(write_list)
