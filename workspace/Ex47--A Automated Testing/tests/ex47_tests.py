from nose.tools import *
from ex47.game import Room

def test_room():#针对room类的测试
    gold = Room("GoldRoom",
    """This room has gold in it you can grab.
    There's a door to the north""")#构造一个示例
    assert_equal(gold.name,"GoldRoom")#检测gold的名字是否为GoldRoom
    assert_equal(gold.paths,{})#检测gold的paths成员是否为空

def test_room_paths():#测试对room类的add_paths和go操作是否正确
    center = Room("Center","Test room in the center.")
    north = Room("North","Test room in the north.")
    south = Room("South","Test room in the south.")
    #创建三个房间

    center.add_paths({'north':north,'south':south})
    #将north和south房间加入到paths中，一个字符对应一种实例
    
    assert_equal(center.go('north'),north)
    #检测center实例执行go('north')后，会不会返回north实例
    
    assert_equal(center.go('south'),south)
    #同上一条

def test_map():#检测paths中房间和方向是否正确
    start = Room("Start","You can go west and down a hole.")
    west = Room("Trees","There are trees here,you can go east.")
    down = Room("Dungeon","It's dark down here,you can go up.")
    #创建三个Room实例，分别为start，west，down

    start.add_paths({'west':west,'down':down})
    #start中有west和down

    west.add_paths({'east':start})
    #west中有east

    down.add_paths({'up':start})
    #down中有up

    assert_equal(start.go('west'),west)
    assert_equal(start.go('west').go('east'),start)
    assert_equal(start.go('down').go('up'),start)
    #一一检测构建的房间及方向是否正确

