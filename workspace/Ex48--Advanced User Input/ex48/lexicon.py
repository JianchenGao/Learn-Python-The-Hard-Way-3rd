import re

class ParserError(Exception):
    pass

def convert_number(s):#将字符数字转换成int型
    try:
        return int(s)
    except ValueError:
        return None

#词典数据
lexicon_direction = ['north','south','east','west','down','up','left','right']
lexicon_verbs = ['go','stop','kill','eat']
lexicon_stop = ['the','in','of','from','at','it']
lexicon_nouns = ['door','bear','princess','cabinet']
lexicon_nums_pattern = re.compile(r'\d+')#匹配数字的正则表达式

def scan(stuff):
    sentence = []#处理好的句子

    #将句子按空格将其分成单词
    words = stuff.split()

    #将单词与词性匹配
    for word in words:
        if lexicon_nums_pattern.match(word):#匹配成功，即此单词为数字
            #匹配成功后，立即将 词性-单词 元组存储
            sentence.append(('number',convert_number(word)))
            continue
        elif lexicon_direction.count(word):#如果Word在direction_list中出现，即可归为此类
            #匹配成功后，立即将 词性-单词 元组存储
            sentence.append(('direction',word))
            continue
        elif lexicon_verbs.count(word):#如果Word在verbs_list中出现，即可归为此类
            #匹配成功后，立即将 词性-单词 元组存储
            sentence.append(('verb',word))
            continue
        elif lexicon_stop.count(word):#如果Word在stop_list中出现，即可归为此类
            #匹配成功后，立即将 词性-单词 元组存储
            sentence.append(('stop',word))
            continue
        elif lexicon_nouns.count(word):#如果Word在nouns_list中出现，即可归为此类
            #匹配成功后，立即将 词性-单词 元组存储
            sentence.append(('noun',word))
            continue
        else:
            #未匹配成功，则设置为error
            sentence.append(('error',word))
    #返回做好匹配的句子
    return sentence

class Sentence(object):

    def __init__(self, subject, verb, object):
        # remember we take ('noun','princess') tuples and convert them
        #将句子中的单词取出
        self.subject = subject[1]# 1 对应Word，单词
        self.verb = verb[1]
        self.object = object[1]
    def print(self):
        return(((self.subject),(self.verb),(self.object)))

def peek(word_list):#将单词liet中的第一个 词性-单词组 取出并返回其词性
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):#对word_list中的第一个和expecting进行匹配
    if word_list:
        word = word_list.pop(0)#pop(0)表示移出list中的第一个 词性-单词组
        if word[0] == expecting:#将词性-单词组中的词性和expecting来对比
            return word#匹配则返回此词性-单词组
        else:
            return None
    else:
        return None

def skip(word_list, word_type):#遍历单词list中的所有单词，一一和word_type比较
    while peek(word_list) == word_type:#找到符合word_type词性的词
        match(word_list, word_type)#将其移除


def parse_verb(word_list):#处理动词
    skip(word_list, 'stop')#跳过定词
    if peek(word_list) == 'verb':#识别并返回动词词组，同时从word_list中移除
        return match(word_list, 'verb')
    else:#若不是动词则返回错误并提示
        raise ParserError("Expected a verb next.")

def parse_object(word_list):#处理名词和方位词
    skip(word_list, 'stop')#删除stop词性的单词
    next = peek(word_list)#取出第一个词性
    if next == 'noun':#识别并返回名词词组，同时从word_list中移除
        return match(word_list, 'noun')
    if next == 'direction':#识别并返回方位词组，同时从word_list中移除
        return match(word_list, 'direction')
    else:#若不是名词或方位词，返回错误并提示
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list, subj):
    verb = parse_verb(word_list)#先处理动词
    obj = parse_object(word_list)#让后处理随后的名词或方位词

    return Sentence(subj, verb, obj)#按特定方式输出,主谓宾

def parse_sentence(word_list):
    skip(word_list, 'stop')#跳过stop类词

    start = peek(word_list)#取出第一个词的词性
    if start == 'noun':#如果第一个词为名词，则将其弹出，然后处理动词加名词的结构
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'verb':#如果第一个词为动词，则直接交由parse_subject来处理动名词结构
        # assume the subject is the player then
        return parse_subject(word_list, ('noun', 'player'))
    else:#返回错误并提示
        raise ParserError("Must start with subject, object, or verb not: %s" % start)