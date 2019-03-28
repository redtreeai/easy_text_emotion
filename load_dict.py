# -*- coding: utf-8 -*-
# @File  : get_cache_demo.py
# @Author: redtree
# @Date  : 18-6-27
# @Desc  : 这是一个将特定文本数据预加载到缓存列表的demo,AllList 将作为全局缓存对象供工程内部的任意模块调用

class AllList():  # 存储所有列表信息的对象
    #中文情感词库
    positive_words_eng = [] #正螚量词
    negative_words_eng = [] #负能量词
    level1_words_eng = [] #程度1
    level2_words_eng = [] #程度2
    level3_words_eng = [] #程度3
    level4_words_eng = [] #程度4
    level5_words_eng = [] #程度5
    level6_words_eng = [] #程度6
    fouding_words_eng = [] #否定词
    #英文
    positive_words_cn = []  # 正螚量词
    negative_words_cn = []  # 负能量词
    level1_words_cn = []  # 程度1
    level2_words_cn = []  # 程度2
    level3_words_cn = []  # 程度3
    level4_words_cn = []  # 程度4
    level5_words_cn = []  # 程度5
    level6_words_cn = []  # 程度6
    fouding_words_cn = []  # 否定词
    pass

def getAllList():  # 提取所有规则列表（后期要改为多线程提取）

    allList = AllList()

    # 情感分析(英文)
    file = open("emotion_dict/eng/pos.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.positive_words_eng.append(checkTr)

    file = open("emotion_dict/eng/neg.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.negative_words_eng.append(checkTr)

    file = open("emotion_dict/eng/level1.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level1_words_eng.append(checkTr)

    file = open("emotion_dict/eng/level2.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level2_words_eng.append(checkTr)

    file = open("emotion_dict/eng/level3.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level3_words_eng.append(checkTr)

    file = open("emotion_dict/eng/level4.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level4_words_eng.append(checkTr)

    file = open("emotion_dict/eng/level5.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level5_words_eng.append(checkTr)

    file = open("emotion_dict/eng/level6.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level6_words_eng.append(checkTr)

    file = open("emotion_dict/eng/fouding.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.fouding_words_eng.append(checkTr)

        # 情感分析(中文)
    file = open("emotion_dict/cn/pos.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.positive_words_cn.append(checkTr)

    file = open("emotion_dict/cn/neg.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.negative_words_cn.append(checkTr)

    file = open("emotion_dict/cn/level1.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level1_words_cn.append(checkTr)

    file = open("emotion_dict/cn/level2.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level2_words_cn.append(checkTr)

    file = open("emotion_dict/cn/level3.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level3_words_cn.append(checkTr)

    file = open("emotion_dict/cn/level4.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level4_words_cn.append(checkTr)

    file = open("emotion_dict/cn/level5.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level5_words_cn.append(checkTr)

    file = open("emotion_dict/cn/level6.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.level6_words_cn.append(checkTr)

    file = open("emotion_dict/cn/fouding.txt", encoding='UTF-8')
    while 1:
        line = file.readline()
        if not line:
            break
        pass
        checkTr = str(line).replace('\n', '')
        allList.fouding_words_cn.append(checkTr)

    return allList