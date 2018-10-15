class Room(object):#创建Room类

    def __init__(self,name,description):#初始化成员
        self.name = name#名字
        self.description = description#描述
        self.paths = {}#路径

    def go(self,direction):#从paths中找到对应的房间
        return self.paths.get(direction,None)

    def add_paths(self,paths):#添加房间
        self.paths.update(paths)
        #update() 方法用于更新字典中的键/值对，
        #可以修改存在的键对应的值，
        # 也可以添加新的键/值对到字典中。
    