import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from main_form import Ui_MainWindow  #导入生成的窗口类
from excel2json_qt5 import excel2json
from JsonReader import JsonReader
from CorpusReader import CorpusReader
from ConfigFile import ConfigFile
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import re

#新建一个类来继承生成的窗口，也可以在这里添加关于窗口处理的代码，比如自定义信号等。
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.btnLoadPlugeDict.hide()

        self.viewList = list()
        self.PluDictViewList = list()
        self.historyInputList = list()
        #词典列表
        self.PlugeDictionary=list()
        '''
        读取配置文件
        '''
        self.ReadConfig()

        self.checkBoxPlugeDict.stateChanged.connect(self.LoadPlugeDict)
        self.btnExcel2Json.clicked.connect(self.Excel2Json)
        self.btnLoadJson.clicked.connect(self.getAttrFilePath)
        self.btnLoadCorpus.clicked.connect(self.getReadCorpusFilePath)
        self.btnPreviousPage.clicked.connect(self.PreviousPage)
        self.btnNextPage.clicked.connect(self.NextPage)
        self.btnJumpPage.clicked.connect(self.JumpPage)
        self.btnSaveCorpus.clicked.connect(self.getSaveCorpusFilePath)
        self.btnCommit.clicked.connect(self.Commit)
        self.btnLoadPlugeDict.clicked.connect(self.getPlugeDictionaryFilePath)
        self.btnOpenInputHistory.clicked.connect(self.ShowInputHistoryDock)
        self.btnClearInputHistory.clicked.connect(self.ClearInputHistory)
        self.btnResearch.clicked.connect(self.Research)
        self.lineEditResearch.textChanged.connect(self.Research)
        self.listWidgetResearch.itemClicked.connect(self.CommitResearch)
        self.btnEntityResearch.clicked.connect(self.EntityResearch)
        self.SetHistoryInputDock()

    def CommitResearch(self,qModelIndex):
        self.UpdateAttr(1)
        text=self.sourceText
        text=text.split('}')[0]
        tlist=self.listWidgetResearch.selectedItems()
        tlist=[t.text() for t in list(tlist)]
        text=text+','+','.join(tlist)+'}'
        self.lineEditResult.setText(text)

    def Research(self):
        self.listWidgetResearch.clear()
        self.sourceText=self.lineEditResult.text()
        compileString=self.lineEditResearch.text()
        #print(compileString)
        cp=re.compile('%s'%compileString)
        for items in self.PlugeDictionary:
            for item in items:
               #print(item)
               if len(re.findall(cp,item))!=0:
                   self.listWidgetResearch.addItem(item)

    def ClearInputHistory(self):
        self.historyInputListWidget.clear()
        self.historyInputList=[]

    def ShowInputHistoryDock(self):
        self.dockWidgetHistoryInput.show()

    def SetHistoryInputDock(self):
        self.historyInputListWidget=QListWidget()
        self.dockWidgetHistoryInput.setWidget(self.historyInputListWidget)
        self.historyInputListWidget.addItems(self.historyInputList)
        self.historyInputListWidget.itemClicked.connect(self.HistoryInput2lineEditResult)

    def HistoryInput2lineEditResult(self,qModelIndex):
        #print(qModelIndex)
        tlist=self.historyInputListWidget.selectedItems()
        text=[t.text() for t in list(tlist)]
        self.lineEditResult.setText(','.join(text))

    def LoadPlugeDict(self):
        if self.checkBoxPlugeDict.isChecked():
            self.btnLoadPlugeDict.show()
            for listWidget in self.PluDictViewList:
                listWidget.show()
        else:
            self.btnLoadPlugeDict.hide()
            for listWidget in self.PluDictViewList:
                listWidget.hide()

        self.UpdateAttr('')

    def Excel2Json(self):
        ex = excel2json(self)
        ex.show()

    def getAttrFilePath(self):
        tmpPath, _ = QFileDialog.getOpenFileName(self,
                                                  r'打开JSON',
                                                  r'./',
                                                  r'JSON File(*.json)')
        if tmpPath !='':
            self.attrFilePath=tmpPath
            self.LoadJson()

    def getReadCorpusFilePath(self):
        tmpPath, _ = QFileDialog.getOpenFileName(self,
                                                  r'打开语料',
                                                  r'./',
                                                  r'Excel File(*.xls *.xlsx)')
        if tmpPath !='':
            self.readCorpusFilePath=tmpPath
            self.LoadCorpus()

    def getSaveCorpusFilePath(self):
        filepath,_ = QFileDialog.getSaveFileName(self,
                                                r'保存语料',
                                                r'./',
                                                r'Excel File (*.xls)')
        tmpPath=filepath
        if tmpPath !='':
            self.saveCorpusFilePath=tmpPath
            self.SaveCorpus()

    def getPlugeDictionaryFilePath(self):
        tmpPath, _ = QFileDialog.getOpenFileName(self,
                                                  r'打开JSON',
                                                  r'./',
                                                  r'JSON File(*.json)')
        if tmpPath !='':
            self.plugeDictionaryFilePath=tmpPath
            self.PlugeDict()

    def LoadJson(self):
        self.jr=JsonReader(self.attrFilePath)
        self.ShowEntity()

    def EntityResearch(self):
        try:
            self.comboBoxEntitys.currentIndexChanged.disconnect(self.ShowAttribute)
        except:
            print('the slot dont have sign')

        entityList = self.jr.getEntityList()
        string = self.lineEditEntityResearch.text()
        cp = re.compile(string)
        researchList = list()
        for entity in entityList:
            if re.findall(cp,entity) != []:
                researchList.append(entity)
        self.comboBoxEntitys.clear()
        self.comboBoxEntitys.addItems(researchList)
        self.comboBoxEntitys.currentIndexChanged.connect(self.ShowAttribute)

    def ShowEntity(self):
        try:
            self.comboBoxEntitys.currentIndexChanged.disconnect(self.ShowAttribute)
        except:
            print('the slot dont have sign')
        self.comboBoxEntitys.clear()
        self.comboBoxEntitys.addItems(self.jr.getEntityList())
        self.comboBoxEntitys.currentIndexChanged.connect(self.ShowAttribute)
    
    def ShowAttribute(self,i):
        entity=self.comboBoxEntitys.currentText()

        attrList,attrListLength = self.jr.getCurrentEntityAttributeList(entity)

        #print(attrListLength)
        if len(self.viewList) < attrListLength:
            listIndex = -1
            for view in self.viewList:
                slm = QStringListModel()
                listIndex+=1
                view.clear()
                view.addItems(self.jr.getAttributeItems(entity,listIndex))

            widgetColumnIndex=listIndex
            widgetRowIndex=0

            for i in range(attrListLength-len(self.viewList)):
                #print(slm)
                listIndex+=1
                widgetColumnIndex+=1
                
                if widgetColumnIndex > 4:
                    widgetRowIndex+=1
                    widgetColumnIndex=0
                print(r'widgetRowIndex:{},widgetColumnIndex:{}'.format(widgetRowIndex,widgetColumnIndex))
                tmpListView = QListWidget()
                tmpListView.addItems(self.jr.getAttributeItems(entity,listIndex))
                tmpListView.itemClicked.connect(self.UpdateAttr)
                # 按住CTRL可多选
                tmpListView.setSelectionMode(QAbstractItemView.ExtendedSelection)
                self.viewList.append(tmpListView)
                self.gridLayoutAttrListView.addWidget(tmpListView,widgetRowIndex,widgetColumnIndex)
        else:
            for index in range(attrListLength):
                self.viewList[index].clear()
                self.viewList[index].addItems(self.jr.getAttributeItems(entity,index))
                self.viewList[index].show()

            for index in range(attrListLength,len(self.viewList)):
                self.viewList[index].hide() 

    def UpdateAttr(self,qModelIndex):
        result=[]
        for view in self.viewList:
            tlist = view.selectedItems()
            text = [t.text() for t in list(tlist)]
            result+=text

        if self.checkBoxPlugeDict.isChecked():
            for pdview in self.PluDictViewList:
                tlist = pdview.selectedItems()
                text = [t.text() for t in list(tlist)]
                result+=text

        self.lineEditResult.setText('{'+','.join(result)+'}')

    def LoadCorpus(self):
        self.cr=CorpusReader(self.readCorpusFilePath)
        id,corpu=self.cr.getCorpu(1)
        self.UpdataCorpu(id,corpu)

    #上一页
    def PreviousPage(self):
        id=self.cr.getId()
        id,corpu=self.cr.getCorpu(id-1)
        self.UpdataCorpu(id,corpu)
        self.lineEditResult.setText(self.cr.getCorpuResult(id))

    #下一页
    def NextPage(self):
        id=self.cr.getId()
        id,corpu=self.cr.getCorpu(id+1)
        self.UpdataCorpu(id,corpu)
        self.lineEditResult.setText(self.cr.getCorpuResult(id))

    #页面跳转
    def JumpPage(self):
        id=int(self.lineEditPage.text())
        _,corpu=self.cr.getCorpu(id)
        self.UpdataCorpu(id,corpu)
        self.lineEditResult.setText(self.cr.getCorpuResult(id))

    def UpdataCorpu(self,id,corpu):
        self.lblNo.setText(str(id))
        self.lblSourceCorpu.setText(corpu)

    def SaveCorpus(self):
        self.cr.setSavePath(self.saveCorpusFilePath)

    #提交结果
    def Commit(self):
        id=self.cr.getId()
        corpu=self.lineEditResult.text()
        self.cr.Commit(id,corpu)
        self.cr.Save()
        '''将输入加载到历史输入框中'''
        if corpu not in self.historyInputList:
            self.historyInputList.append(corpu)
            self.historyInputListWidget.addItem(corpu)

    def PlugeDict(self):
        self.plugeDictjr=JsonReader(self.plugeDictionaryFilePath)
        self.plugeDictAttrList=self.plugeDictjr.getEntityList()
        widgetRowIndex=0
        widgetColumnIndex=-1
        for attrTitle in self.plugeDictAttrList:
            #print(self.plugeDictjr.getPlugeDictAttrItems(attrTitle))
            widgetColumnIndex+=1
                
            if widgetColumnIndex > 4:
                widgetRowIndex+=1
                widgetColumnIndex=0
            print(r'widgetRowIndex:{},widgetColumnIndex:{}'.format(widgetRowIndex,widgetColumnIndex))
            tmpListView = QListWidget()
            item=self.plugeDictjr.getPlugeDictAttrItems(attrTitle)
            self.PlugeDictionary.append(item)
            tmpListView.addItems(item)
            tmpListView.itemClicked.connect(self.UpdateAttr)
                # 按住CTRL可多选
            tmpListView.setSelectionMode(QAbstractItemView.ExtendedSelection)
            self.PluDictViewList.append(tmpListView)
            tmpListView.hide()
            self.gridLayoutPlugeDictListView.addWidget(tmpListView,widgetRowIndex,widgetColumnIndex)

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        configItems=list()
        
        try:
            configItems.append('historyInputList&&'+"||".join(self.historyInputList))
            configItems.append('readCorpusFilePath&&'+self.readCorpusFilePath)
            configItems.append('attrFilePath&&'+self.attrFilePath)
            configItems.append('plugeDictionaryFilePath&&'+self.plugeDictionaryFilePath)
            configItems.append('saveCorpusFilePath&&'+self.saveCorpusFilePath)           
        except:
            print('存在设置没有设定')
        self.configFile.WriteConfig(configItems)

    def ReadConfig(self):
        self.configFile = ConfigFile()
        configItems=self.configFile.ReadConfig()

        for item in configItems:
            part=item.strip('\n').split('&&')
            if len(part)!=1:
                if part[0]=='attrFilePath':
                    self.attrFilePath=part[1]
                    self.LoadJson()
                elif part[0]=='plugeDictionaryFilePath':
                    self.plugeDictionaryFilePath=part[1]
                    self.PlugeDict()
                elif part[0]=='saveCorpusFilePath':
                    self.saveCorpusFilePath=part[1]
                    self.SaveCorpus()
                elif part[0]=='readCorpusFilePath':
                    self.readCorpusFilePath=part[1]
                    self.LoadCorpus()
                elif part[0]=='historyInputList':
                    self.historyInputList=part[1].split('||')

        
#主程序，生成一个窗口实例并运行。
if __name__=="__main__":  
    app = QApplication(sys.argv)  
    myWin = MyMainWindow()  
    myWin.show()  
    sys.exit(app.exec_())  
