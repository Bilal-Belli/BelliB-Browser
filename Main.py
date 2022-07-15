#this is my personal browser
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        ##############
        # Bookmark_bar
        Bookmark_bar = QToolBar()
        self.addToolBar(Bookmark_bar)

        Youtube_btn = QAction('Youtube', self)
        Youtube_btn.triggered.connect(self.goYoutube)
        Bookmark_bar.addAction(Youtube_btn)

        Facebook_btn = QAction('Facebook', self)
        Facebook_btn.triggered.connect(self.goFacebook)
        Bookmark_bar.addAction(Facebook_btn)

        Google_btn = QAction('Google', self)
        Google_btn.triggered.connect(self.goGoogle)
        Bookmark_bar.addAction(Google_btn)
        ##############
        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)
        
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def goYoutube(self):
        self.browser.setUrl(QUrl('https://www.youtube.com'))

    def goFacebook(self):
        self.browser.setUrl(QUrl('https://www.facebook.com'))

    def goGoogle(self):
        self.browser.setUrl(QUrl('https://www.google.fr'))


app = QApplication(sys.argv)
QApplication.setApplicationName('BelliB Browser')

window = MainWindow()

icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
window.setWindowIcon(icon)

app.exec_()
#command to convert from py code to executable: auto-py-to-exe
#i use nsis to make the installer of this application
#steps to make installer
#1-make the directory of executable
#2-install 'inno setup'
#3-use inno setup to create the executable of the installer, dont miss to add icons,folders, and any file
#4-dont forget to save the files with defferent nams