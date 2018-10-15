from nose.tools import *
from ex48 import lexicon

def test_parse_sentence():#测试句子解析
    result = lexicon.scan("go north")
    parse_result = lexicon.parse_sentence(result)
    assert_equal((parse_result.print()), ( 'player','go','north') )

    result = lexicon.scan("go the door")
    parse_result = lexicon.parse_sentence(result)
    assert_equal((parse_result.print()), ( 'player','go','door') )

    #result = lexicon.scan("111 go north")
    #parse_result = lexicon.parse_sentence(result)
    #assert_equal(parse_result,"Must start with subject, object, or verb not: 111")

