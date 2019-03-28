# -*- coding: utf-8 -*-
# @Time    : 18-9-18 上午9:23
# @Author  : Redtree
# @File    :  emotion_eng.py
# @Desc : 文本情感分析算法 （英文）

import load_dict
all_list = load_dict.getAllList()
import nltk
import random
#文本情感分析算法
def cutSentence(input):  #结巴分词
    res = nltk.word_tokenize(input)  # 默认是精确模式
    return res

def reduceFunc(reduceTimes):  #适用于累加条件下的衰减法 （pos and neg）
    addY=(10/reduceTimes)/10
    return addY #衰减后当此追加的情感值

def levelReduceFunc(levelReduceTimes,level,type): #适用于区间叠乘条件下的衰减法 （level）
    if level==6:
        levela=2  #区间下限
        levelb=2.5 #区间上限
        levelER=0.67 #衰减系数

    if level==5:
        levela=1.6  #区间下限
        levelb=1.9 #区间上限
        levelER=0.67 #衰减系数

    if level==4:
        levela=1.2  #区间下限
        levelb=1.6 #区间上限
        levelER=0.67 #衰减系数

    if level==3:
        levela=0.6  #区间下限
        levelb=0.9 #区间上限
        levelER=1.23 #衰减系数

    if level == 2:
        levela = 0.4  # 区间下限
        levelb = 0.7  # 区间上限
        levelER = 1.23  # 衰减系数

    if level == 1:
        levela = 0.2  # 区间下限
        levelb = 0.5  # 区间上限
        levelER = 1.23  # 衰减系数

    if level >= 4:

       if type == 'topLimit':   #上限衰减
            levelbCheck = levelb * (levelER ** (levelReduceTimes - 1))
            if levelbCheck<=1.001:
                levelbCheck = 1.001
            return levelbCheck
       if type == 'lowerLimit': #下限衰减
            levelaCheck = levela * (levelER ** (levelReduceTimes - 1))
            if levelaCheck<=1.000:
                levelaCheck = 1.000
            return  levelaCheck

    if level <=3 :

        if type == 'topLimit':  # 上限衰减
            levelbCheck = levelb * (levelER ** (levelReduceTimes - 1))
            if levelbCheck >= 1.000:
                levelbCheck = 1.000
            return levelbCheck
        if type == 'lowerLimit':  # 下限衰减
            levelaCheck = levela * (levelER ** (levelReduceTimes - 1))
            if levelaCheck >= 0.998:
                levelaCheck = 0.998
            return levelaCheck

def checkMoodValue(segWord): #获取句子的情感能量值 mv =(posV*(functionE)+negV*(functionE))*isFouDing*chekLevel
    MoodValue = 0                  #functionE 为待加算法，用于处理重复数据的量级衰减
    isFouDing = 1
    checkLevel=1
    posreduceTimes=1
    negreduceTimes=1
    level6ReduceTimes=1
    level5ReduceTimes=1
    level4ReduceTimes=1
    level3ReduceTimes = 1
    level2ReduceTimes = 1
    level1ReduceTimes = 1
    # 正能量词Check
    for onePos in all_list.positive_words_eng:
        if str(onePos).__contains__(' '):
            if str(onePos) in str(segWord):
                MoodValue = MoodValue + reduceFunc(posreduceTimes);
                posreduceTimes = posreduceTimes + 1;
                break
        else:
            if str(onePos) in cutSentence(str(segWord)):
                MoodValue = MoodValue + reduceFunc(posreduceTimes);
                posreduceTimes = posreduceTimes + 1;
                break

    # 负能量词Check
    for oneNeg in all_list.negative_words_eng:
        if str(oneNeg).__contains__(' '):
            if str(oneNeg) in str(segWord):
                MoodValue = MoodValue - reduceFunc(negreduceTimes);
                negreduceTimes = negreduceTimes + 1;
                break
        else:
            if str(oneNeg) in cutSentence(str(segWord)):
                MoodValue = MoodValue - reduceFunc(negreduceTimes);
                negreduceTimes = negreduceTimes + 1;
                break
    # 否定词Check
    for fdword in all_list.fouding_words_eng:
        if str(fdword).__contains__(' '):
            if str(fdword) in str(segWord):
                isFouDing = isFouDing * (-1)
                break
        else:
            if str(fdword) in cutSentence(str(segWord)):
                isFouDing = isFouDing * (-1)
                break
    # 程度级Check 矫正系数 er
    # level1 矫正系数(0.2~0.5)
    # level2 矫正系数(0.4~0.7)
    # level3 矫正系数(0.6~0.9)
    # level4 矫正系数(1.2~1.6)
    # level5 矫正系数(1.6~1.9)
    # level6 矫正系数(2.0~2.5)

    for oneLevel in all_list.level1_words_eng:
        if str(oneLevel).__contains__(' '):
            if str(oneLevel) in str(segWord):
                er = random.uniform(levelReduceFunc(level1ReduceTimes, 1, 'lowerLimit'),
                                    levelReduceFunc(level1ReduceTimes, 1, 'topLimit'))
                checkLevel = checkLevel * er
                break
        else:
            if str(oneLevel) in cutSentence(str(segWord)):
                er = random.uniform(levelReduceFunc(level1ReduceTimes, 1, 'lowerLimit'),
                                    levelReduceFunc(level1ReduceTimes, 1, 'topLimit'))
                checkLevel = checkLevel * er
                break
    for oneLevel in all_list.level2_words_eng:
        if str(oneLevel).__contains__(' '):
            if str(oneLevel) in str(segWord):
                er = random.uniform(levelReduceFunc(level2ReduceTimes, 2, 'lowerLimit'),
                                    levelReduceFunc(level2ReduceTimes, 2, 'topLimit'))
                checkLevel = checkLevel * er
                break
        else:
            if str(oneLevel) in cutSentence(str(segWord)):
                er = random.uniform(levelReduceFunc(level2ReduceTimes, 2, 'lowerLimit'),
                                    levelReduceFunc(level2ReduceTimes, 2, 'topLimit'))
                checkLevel = checkLevel * er
                break
    for oneLevel in all_list.level3_words_eng:
        if str(oneLevel).__contains__(' '):
            if str(oneLevel) in str(segWord):
                er = random.uniform(levelReduceFunc(level3ReduceTimes, 3, 'lowerLimit'),
                                    levelReduceFunc(level3ReduceTimes, 3, 'topLimit'))
                checkLevel = checkLevel * er
                break
        else:
            if str(oneLevel) in cutSentence(str(segWord)):
                er = random.uniform(levelReduceFunc(level3ReduceTimes, 3, 'lowerLimit'),
                                    levelReduceFunc(level3ReduceTimes, 3, 'topLimit'))
                checkLevel = checkLevel * er
                break
    for oneLevel in all_list.level4_words_eng:
        if str(oneLevel).__contains__(' '):
            if str(oneLevel) in str(segWord):
                er = random.uniform(levelReduceFunc(level4ReduceTimes, 4, 'lowerLimit'),
                                    levelReduceFunc(level4ReduceTimes, 4, 'topLimit'))
                checkLevel = checkLevel * er
                break
        else:
            if str(oneLevel) in cutSentence(str(segWord)):
                er = random.uniform(levelReduceFunc(level4ReduceTimes, 4, 'lowerLimit'),
                                    levelReduceFunc(level4ReduceTimes, 4, 'topLimit'))
                checkLevel = checkLevel * er
                break
    for oneLevel in all_list.level5_words_eng:
        if str(oneLevel).__contains__(' '):
            if str(oneLevel) in str(segWord):
                er = random.uniform(levelReduceFunc(level5ReduceTimes, 5, 'lowerLimit'),
                                    levelReduceFunc(level5ReduceTimes, 5, 'topLimit'))
                checkLevel = checkLevel * er
                break
        else:
            if str(oneLevel) in cutSentence(str(segWord)):
                er = random.uniform(levelReduceFunc(level5ReduceTimes, 5, 'lowerLimit'),
                                    levelReduceFunc(level5ReduceTimes, 5, 'topLimit'))
                checkLevel = checkLevel * er
                break
    for oneLevel in all_list.level6_words_eng:
        if str(oneLevel).__contains__(' '):
            if str(oneLevel) in str(segWord):
                er = random.uniform(levelReduceFunc(level6ReduceTimes, 6, 'lowerLimit'),
                                    levelReduceFunc(level6ReduceTimes, 6, 'topLimit'))
                checkLevel = checkLevel * er
                break
        else:
            if str(oneLevel) in cutSentence(str(segWord)):
                er = random.uniform(levelReduceFunc(level6ReduceTimes, 6, 'lowerLimit'),
                                    levelReduceFunc(level6ReduceTimes, 6, 'topLimit'))
                checkLevel = checkLevel * er
                break

    MoodValue = MoodValue * isFouDing * checkLevel
    return MoodValue

def getMoodValue(text):
    try:
        text = str(text).replace('，', '，|')
        text = str(text).replace('。', '。|')
        text = str(text).replace(',', '，|')
        text = str(text).replace('.', '。|')
        text = str(text).replace('!', '!|')
        text = str(text).replace('！', '！|')
        text = str(text).replace('？', '？|')
        text = str(text).replace('?', '?|')
        tsp_list = text.split('|')
        all_mv = 0
        re_obj = []

        for tl in tsp_list:
            if not (tl == '' or tl == ' ' ):
                tmp_MoodValue = checkMoodValue(tl)
                all_mv = all_mv + tmp_MoodValue
                cobj = {'text':tl,'value':round(tmp_MoodValue,6)}
                re_obj.append(cobj)

        res = {'all_value':round(all_mv,6),'split':re_obj}
        return res
    except Exception as err:
        print('文本情感分析失败'+str(err))
        return 'error'
