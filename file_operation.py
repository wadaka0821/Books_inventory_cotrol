import re
import datetime
import csv

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
            #在庫数が負になっても警告なし
            for i in reader:
                if i[0]+i[1] in self.current:
                    self.current[i[0]+i[1]][1] += int(i[3])
                else:
                    self.current.update({i[0]+i[1]:[i[2],i[3]]})

                if int(i[3]) > 0:
                    add_list.append(i)
                elif int(i[3]) < 0:
                    sub_list.append(i)
            print(self.current)
            for i,j in self.current.items():
                adding_list.append([i]+j)
            self.writerow_file(adding_list,"books_info/current.csv","w")
            self.writerow_file(add_list,"books_info/time_log/add.csv","a")
            self.writerow_file(sub_list,"books_info/time_log/sub.csv","a")

    def road_current(self):
        with open("books_info/current.csv","r") as f:
            reader = csv.reader(f)
            for i in reader:
                if i[0]+i[1] not in self.current:
                    self.current.update({i[0]+i[1]:[i[2],int(i[3])]})
        print(self.current)

    def writerow_file(self,write_list,original_file,mode):
        with open(original_file,mode) as f:
            writer = csv.writer(f)
            writer.writerows(write_list)
