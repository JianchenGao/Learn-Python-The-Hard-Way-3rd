def peek(word_list):#将单词liet中的第一个单词取出，返回第一个单词的首字母
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):#
    if word_list:
        word = word_list.pop(0)#pop(0)表示移出list中的第一个元素
        if word[0] == expecting:#将第一个单词的第一个字母和expecting来对比
            return word#匹配则返回此单词
        else:
            return None
    else:
        return None

def skip(word_list, word_type):#遍历单词list中的所有单词，一一和word_type比较
    while peek(word_list) == word_type:#？？？？
        match(word_list, word_type)

        