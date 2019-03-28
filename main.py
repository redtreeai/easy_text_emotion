# -*- coding: utf-8 -*-
# @Time    : 19-3-28 上午10:56
# @Author  : Redtree
# @File    : main.py
# @Desc :

import emotion_eng
import emotion_cn

if __name__ == '__main__':
    while 1>0 :
        lg = input("switch language,type 'CN' or 'ENG' ,if you want to exit ,type '0' "+'\n')
        if lg == 'CN':
            print("type chinese text to get result,if you want to exit ,type '0' ")
            while 1 > 0:
                input_text = input('\n')
                out_put = emotion_cn.getMoodValue(input_text)
                print(out_put)
                if input_text == '0':
                    break
        elif lg == 'ENG':
            print("type english text to get result,if you want to exit ,type '0' ")
            while 1 > 0:
                input_text = input('\n')
                out_put = emotion_eng.getMoodValue(input_text)
                print(out_put)
                if input_text == '0':
                    break
        elif lg =='0':
            break

