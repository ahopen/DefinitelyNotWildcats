# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 22:45:19 2017

@author: andre
"""

import io
import json
import os


def convert_tip_json_file_to_csv(old_file_path, new_file_path):
    write_dir = os.path.dirname(new_file_path)
    if not os.path.isdir(write_dir):
        os.mkdir(write_dir)
    with io.open(new_file_path, 'w', encoding='utf8') as new_f:
        new_f.write(u'biz_id,user_id,date,text,likes\n')
        with open(old_file_path, 'r', encoding='utf8') as old_f:
            for line in old_f:
                tip_json = json.loads(line)
                tip_cvs = u'{biz_id},{user_id},{date},{text},{likes}\n'.format(
                        biz_id=tip_json['business_id'].replace(',', ' '),
                        user_id=tip_json['user_id'].replace(',', ' '),
                        date=tip_json['date'].replace(',', ' '),
                        text=tip_json['text'].replace(',', ' ').replace('\n',' ').replace('\"',''),
                        likes=tip_json['likes'])
                new_f.write(tip_cvs)


def main():
    print("starting main process")
    convert_tip_json_file_to_csv('C:/Users/Andrew/Documents/DSGA-1001/Final Project/tip.json', 
                                      'C:/Users/Andrew/Documents/DSGA-1001/Final Project/tip.csv')
    print("\n finished the process")


if __name__ == "__main__":
    main()
