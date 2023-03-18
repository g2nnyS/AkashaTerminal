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
        if whnd != 0:    
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

except Exception:
    sys.exit()