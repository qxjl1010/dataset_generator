import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import excel2json as xls2json

#class excel2json(QWidget):
class excel2json(QDialog):
    def __init__(self,parent = None):
        super(excel2json,self).__init__(parent)
        layout = QVBoxLayout()
        self.btnLoadExcel = QPushButton(r'读取Excel')
        self.btnLoadExcel.clicked.connect(self.getExcel)
        layout.addWidget(self.btnLoadExcel)
        self.btnSaveJson = QPushButton(r'保存JSON')
        self.btnSaveJson.clicked.connect(self.saveJson)
        layout.addWidget(self.btnSaveJson)
        self.leResult = QLabel(r'')
        layout.addWidget(self.leResult)
        self.setLayout(layout)
        self.x2j = xls2json.Excel2json()

    def getExcel(self):
        fname, _ = QFileDialog.getOpenFileName(self,
                                               r'打开Excel',
                                               r'./',
                                               r'Excel File (*.xls);;Excel File(*.xlsx)')
        #print(fname)
        self.dic = self.x2j.GetExcel(fname)
        self.leResult.setText(r'打开' + fname.split('/')[-1] + r'成功')

    def saveJson(self):
        file_path = QFileDialog.getSaveFileName(self,
                                                r'保存JSON',
                                                r'./',
                                                r'JSON File (*.json)')
        #print(file_path)
        try:
            self.x2j.SaveJson(file_path[0],self.dic)
        except:
            print(r'error')
            print(file_path)
            print(type(file_path))
        self.leResult.setText(r'保存' + file_path[0].split('/')[-1] + r'成功')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = excel2json()
    ex.show()
    sys.exit(app.exec_())