import json
import xlrd

#excelPath = r'C:/Users/sa/Desktop/诊断学症状整理.xlsx'
class Excel2json(object):
    def GetExcel(self,excelPath):
        excelBook = xlrd.open_workbook(excelPath)
        js = dict()
        try:
            for sheet in range(10):
                excelSheet = excelBook.sheet_by_index(sheet)

                cols = excelSheet.ncols
                rows = excelSheet.nrows

                
                for row in range(1,rows-1):
                    entity = excelSheet.cell(row,0).value
                    js[entity] = dict()
    #print(entity)
                    js[entity][r'体征']=[entity]
                    for col in range(1,cols-1):
                        value = excelSheet.cell(row,col).value
                        if value != '':
                            key = excelSheet.cell(0,col).value
                            js[entity][key]=value.split('、')
        except:
            print('out of range')

        return js
            #print(value.split('、'),key)

#print(js)
#print(json.dumps(js,ensure_ascii=False,indent=4))
    def SaveJson(self,jsonPath,jsonDict):
        with open(jsonPath,'w+',encoding = 'utf-8') as jsf:
            json.dump(jsonDict,jsf,ensure_ascii=False,indent=4)