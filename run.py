import os
import sys
import ctypes
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

whnd = ctypes.windll.kernel32.GetConsoleWindow()    
if whnd != 0:    
    ctypes.windll.user32.ShowWindow(whnd, 0)    
    ctypes.windll.kernel32.CloseHandle(whnd)  

os.popen('python main.py')
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('虚空终端 | AkashaTerminal')  #窗口标题
        self.setWindowIcon(QIcon("./webssh/static/img/favicon.png"))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.desktop = QApplication.desktop()
        self.setFixedSize(self.desktop.width() * 0.35, self.desktop.height() * 0.6) #窗口大小
        self.browser=QWebEngineView()
        self.browser.load(QUrl('http://127.0.0.1:34223'))
        self.setCentralWidget(self.browser)
def _close_max_min_icon(self):
    self.pushButton_3.setText('r')
    self.pushButton_2.setText('1')
    self.pushButton.setText('0')

@pyqtSlot()
def on_pushButton_clicked(self):
    # 最小化
    self.showMinimized()

@pyqtSlot()
def on_pushButton_2_clicked(self):
    # 最大化与复原
    if self.isMaximized():
        self.showNormal()
        self.pushButton_2.setText('1')  # 切换放大按钮图标字体
        self.pushButton_2.setToolTip("<html><head/><body><p>最大化</p></body></html>")
    else:
        self.showMaximized()
        self.pushButton_2.setText('2')
        self.pushButton_2.setToolTip("<html><head/><body><p>恢复</p></body></html>")

@pyqtSlot()
def on_pushButton_3_clicked(self):
    # 关闭程序
    self.close()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    app.exit(app.exec_())
    os.system('taskkill /im python.exe /f')
