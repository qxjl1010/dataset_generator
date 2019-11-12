import xlrd
from xlutils.copy import copy

class CorpusReader(object):
    def __init__(self,filename):
        self.__book__=xlrd.open_workbook(filename)
        self.__sheet__=self.__book__.sheet_by_index(0)
        self.__id__=1
        self.__corpu__=self.__sheet__.cell(0,0).value
        self.setSavePath(filename)

    def getCorpu(self,id):
        self.__row__=id-1
        return self.__row__+1,self.__sheet__.cell(self.__row__,0).value

    def getCorpuResult(self,id):
        self.__row__=id-1
        if self.__savePath__=='':
            try:
                return self.__row__+1,self.__sheet__.cell(self.__row__,2).value
            except: 
                return ''
        else:
            try:
                return saveSheet.cell(self.__row__,2).value
            except:
                saveBook=xlrd.open_workbook(self.__savePath__)
                saveSheet=saveBook.sheet_by_index(0)
                try:
                    return saveSheet.cell(self.__row__,2).value
                except:
                    return ''

    def getId(self):
        return self.__row__+1

    def setSavePath(self,filename):
        self.__savePath__=filename   
        self.__saveBook__=copy(self.__book__)
        self.__saveSheet__=self.__saveBook__.get_sheet(0)

    def Commit(self,id,corpu):
        self.__saveSheet__.write(id-1,2,corpu)

    def Save(self):
        self.__saveBook__.save(self.__savePath__)
