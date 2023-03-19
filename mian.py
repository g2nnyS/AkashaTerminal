import os
import sys
import ctypes
import threading
import asyncio
from webssh.main import main
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

try:
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    def window():    #窗口实现
        #如debug=false则隐藏控制台窗口
        if whnd != 0:
            debug = True #True显示控制台窗口，False隐藏控制台窗口
            if debug == False:
                ctypes.windll.user32.ShowWindow(whnd, 0)
                ctypes.windll.kernel32.CloseHandle(whnd)

        class MainWindow(QMainWindow):
            def __init__(self):
                super(MainWindow, self).__init__()
                self.setWindowTitle('虚空终端 | AkashaTerminal')  #窗口标题
                self.setWindowIcon(QIcon("./webssh/static/img/favicon.png"))
                self.setAttribute(Qt.WA_TranslucentBackground)
                self.desktop = QApplication.desktop()
                self.resize(1300,700)
                self.browser=QWebEngineView()
                self.browser.load(QUrl('http://127.0.0.1:34223'))
                self.setCentralWidget(self.browser)
        app=QApplication(sys.argv)
        win=MainWindow()
        win.show()
        app.exit(app.exec_())
        sys.exit()

    #创建多线程
    def run_main():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())
    thread_1 = threading.Thread(target=run_main)
    thread_2 = threading.Thread(target=window)

    if __name__ == '__main__':
        thread_1.start()
        thread_2.start()
        thread_1.join()
        thread_2.join()
        #当主线程退出时，子线程也退出
        thread_1.setDaemon(True)
        thread_2.setDaemon(True)

except Exception:
    sys.exit()