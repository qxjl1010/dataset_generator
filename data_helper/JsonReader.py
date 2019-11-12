import json

class JsonReader(object):
    """description of class"""
    def __init__(self,JsonPath):
        path=JsonPath
        self.__dict__=json.load(open(path,r'r+',encoding='utf-8'))

    '''
    获取json中实体列表
    '''
    def getEntityList(self):
        return [entity for entity in self.__dict__]
    
    '''
    获取当前实体属性列表及其长度
    '''
    def getCurrentEntityAttributeList(self,currentEntity):
        self.__attrList__=[attr for attr in self.__dict__[currentEntity]]
        return self.__attrList__,len(self.__attrList__)

    '''
    获取属性列表中的项
    '''
    def getAttributeItems(self,currentEntity,attributeListIndex):
        result=list()
        for value in self.__dict__[currentEntity][self.__attrList__[attributeListIndex]]:
            if len(value)!=0:
                result.append("\"{}\":\"{}\"".format(value,self.__attrList__[attributeListIndex]))
        #return self.__dict__[currentEntity][self.__attrList__[attributeListIndex]]
        return result       

    '''获取外挂字典项'''
    def getPlugeDictAttrItems(self,attrTitle):
        result=list()
        for value in self.__dict__[attrTitle]:
            result.append("\"{}\":\"{}\"".format(value,attrTitle))
        #return self.__dict__[currentEntity][self.__attrList__[attributeListIndex]]
        return result

if __name__ == "__main__":
    jr=JsonReader(r'C:/Users/sa/Desktop/1.json')
    print(jr.getEntityList())
    jr.getCurrentEntityAttributeListLength("发热")
    print(jr.getAttributeItems("发热",1))
