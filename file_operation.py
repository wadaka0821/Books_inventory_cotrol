import re

class File_operation:
    def __init__(self):
        self.menus = {"1":"ファイル読み込み","2":"ファイル名の指定(初期値はrs_list.csv)"}
        self.categories = dict()
        self.input_file = "rs_list.csv"

        self.menu()

    def menu(self):
        print("-----------ファイル操作-----------")
        for i,j in self.menus.items():
            print("{:<3}{}{:^26}".format(i,"|",j))
        print("----------------------------------")

        input()

    def check_filename(self,name):
        pass
