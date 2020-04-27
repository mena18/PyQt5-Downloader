from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from MainWindow import MainWindow
from YoutubeDownloader import YoutubeDownloader,PlayListDownloader

import pafy
import os,sys



ui,_ = loadUiType(os.path.join(os.path.dirname(__file__),'main.ui'))



class MainApp(QMainWindow,ui):

    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('Download')
        self.setFixedSize(600,330)
        self.message=""

        self.mainWindow_init()
        self.youtubeDownloader_init()
        self.PlayListDownloader_init()

    def mainWindow_init(self):
        lis={}
        lis['main'] = self
        lis['url'] = self.url_label
        lis['file'] = self.file_label
        lis['browse'] = self.browse_button
        lis['download'] = self.download_button
        lis['progress'] = self.main_download_progressbar
        self.main_window = MainWindow(lis)

    def youtubeDownloader_init(self):
        lis={}
        lis['main'] = self
        lis['url'] = self.url_label_3
        lis['file'] = self.file_label_3
        lis['browse'] = self.browse_button_3
        lis['download'] = self.download_button_3
        lis['progress'] = self.youtube_download_progressbar
        lis['quality_checkbox'] = self.quality
        self.youtube = YoutubeDownloader(lis)



    def PlayListDownloader_init(self):
        lis={}
        lis['main'] = self
        lis['url'] = self.url_label_4
        lis['file'] = self.file_label_4
        lis['browse'] = self.browse_button_4
        lis['download'] = self.download_button_4
        lis['progress'] = self.playlist_download_progressbar
        lis['lcd'] = self.lcd
        self.playlist = PlayListDownloader(lis)



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


main()
