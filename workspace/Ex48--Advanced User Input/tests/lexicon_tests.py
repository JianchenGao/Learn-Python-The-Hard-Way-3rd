from nose.tools import *
from ex48 import lexicon

def test_directions():#对表明方向的词进行测试
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                            ('direction', 'south'),
                            ('direction', 'east')])
def test_verbs():#测试动词
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                            ('verb', 'kill'),
                            ('verb', 'eat')])
def test_stops():#测试冠词
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                            ('stop', 'in'),
                            ('stop', 'of')])
def test_nouns():#测试名词
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess")
    assert_equal(result, [('noun', 'bear'),
                            ('noun', 'princess')])
def test_numbers():#测试数字
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                            ('number', 91234)])
def test_errors():#测试错误有没有被检测出来
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                            ('error', 'IAS'),
                            ('noun', 'princess')])