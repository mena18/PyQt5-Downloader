from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import urllib.request
import os

class MainWindow:
    def __init__(self,lis):
        self.main = lis['main']
        self.url_label = lis['url']
        self.file_label = lis['file']
        self.browse_button = lis['browse']
        self.download_button = lis['download']
        self.progress_bar = lis['progress']

        self.download_button.clicked.connect(self.download)
        self.browse_button.clicked.connect(self.browse)


    def browse(self):
        loc = QFileDialog.getExistingDirectory(None,'choose direcory')
        self.file_label.setText(loc);

    def progress(self,blocknum,blocksize,size):
        self.progress_bar.setValue((blocksize*blocknum*100)/size);
        QApplication.processEvents()


    def file_exists(self,new_path):
        try:
            f = open(new_path,"r")
            f.close()
            return 1
        except:
            return 0


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
            QMessageBox.warning(self.main,"Error",message);
        else:
            extention = url.split('.')[-1]
            new_path = ""
            index=1
            file_name="random"
            new_path=os.path.join(file,file_name+'.'+extention)
            while True:
                if(self.file_exists(new_path)):
                    new_path = os.path.join(file,"{}({}).{}".format(file_name,index,extention))
                    index+=1
                else:
                    break;

            urllib.request.urlretrieve(url,new_path,self.progress)
            self.url_label.setText("")
            self.file_label.setText("")
            self.progress_bar.setValue(0)
