from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pafy
import os


class YoutubeDownloader:
    def __init__(self,lis):
        self.main = lis['main']
        self.url_label = lis['url']
        self.file_label = lis['file']
        self.browse_button = lis['browse']
        self.download_button = lis['download']
        self.progress_bar = lis['progress']
        self.quality_checkbox = lis['quality_checkbox']

        self.pafy_object=""
        self.streams=""

        self.download_button.clicked.connect(self.download)
        self.browse_button.clicked.connect(self.browse)
        self.url_label.textChanged.connect(self.validate_url)




    def validate_url(self):
        self.quality_checkbox.clear()
        url = self.url_label.text()
        self.pafy_object = pafy.new(url)
        self.streams = self.pafy_object.streams
        for i in self.streams:
            self.quality_checkbox.addItem("{} {} {}".format(i.extension,i.quality,i.get_filesize()/1000000))


    def browse(self):
        loc = QFileDialog.getExistingDirectory(None,'choose direcory')
        self.file_label.setText(loc);

    def progress(self,total, recvd, ratio, rate, eta):
        self.progress_bar.setValue(ratio*100);
        QApplication.processEvents()

    def valid(self,url,file):
        if(url==""):
            return "url is empty"
        if(file==""):
            return "file is empty"

        return ""


    def download(self):
        url = self.url_label.text()
        file = self.file_label.text()
        message = self.valid(url,file)
        if(message!=""):
            QMessageBox.warning(self,"Error",message)
        else:
            a = self.pafy_object
            streams = self.streams
            video_quality = self.quality_checkbox.currentIndex()
            download = streams[video_quality].download(filepath=file,callback=self.progress)

        self.url_label.setText("")
        self.file_label.setText("")
        self.progress_bar.setValue(0)
        self.quality_checkbox.clear()






class PlayListDownloader:
    def __init__(self,lis):
        self.main = lis['main']
        self.url_label = lis['url']
        self.file_label = lis['file']
        self.browse_button = lis['browse']
        self.download_button = lis['download']
        self.progress_bar = lis['progress']
        self.lcd = lis['lcd']

        self.download_button.clicked.connect(self.download)
        self.browse_button.clicked.connect(self.browse)



    def browse(self):
        loc = QFileDialog.getExistingDirectory(None,'choose direcory')
        self.file_label.setText(loc);

    def progress(self,total, recvd, ratio, rate, eta):
        self.progress_bar.setValue(ratio*100);
        QApplication.processEvents()

    def valid(self,url,file):
        if(url==""):
            return "url is empty"
        if(file==""):
            return "file is empty"

        return ""


    def download(self):
        url = self.url_label.text()
        file = self.file_label.text()
        message = self.valid(url,file)
        if(message!=""):
            QMessageBox.warning(self,"Error",message)
        else:
            playlist = pafy.get_playlist(url)
            videos = playlist['items']
            video_n = 1
            for video in videos:
                self.lcd.display(video_n)
                video['pafy'].getbestaudio().download(filepath=file,callback=self.progress)
                video_n+=1

        self.url_label.setText("")
        self.file_label.setText("")
        self.progress_bar.setValue(0)
        self.lcd.display(0)
