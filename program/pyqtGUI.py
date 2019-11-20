#!/usr/bin/env python

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

import os
import shutil
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        with open("./templates/this_test.html", 'r') as f:
            html = f.read()

        self.browser.setHtml(html)
        self.setFixedSize(1600,900)
        # self.browser.urlChanged.connect(self.update_urlbar)
        # self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        # Uncomment to disable native menubar on Mac
        # self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu("File")

        open_file_action = QAction(QIcon("./images/open.png"), "Open Graph File...", self)
        open_file_action.setStatusTip("Open Graph from File")
        open_file_action.triggered.connect(self.open_file)
        file_menu.addAction(open_file_action)

        open_csv_action = QAction(QIcon("./images/open.png"), "Open CSV File...", self)
        open_csv_action.setStatusTip("Open CSV and Generate Graph from File")
        open_csv_action.triggered.connect(self.open_csv)
        file_menu.addAction(open_csv_action)

        save_screenshot_action = QAction(QIcon("./images/save.png"), "Save Screenshot...", self)
        save_screenshot_action.setStatusTip("Save Screenshot")
        save_screenshot_action.triggered.connect(self.save_screenshot)
        file_menu.addAction(save_screenshot_action)

        save_file_action = QAction(QIcon("./images/save.png"), "Save Graph...", self)
        save_file_action.setStatusTip("Save current graph to HTML file")
        save_file_action.triggered.connect(self.save_file)
        file_menu.addAction(save_file_action)

        self.show()

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("%s" % title)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "Hypertext Markup Language (*.htm *.html);;")

        if filename:
            with open(filename, 'r') as f:
                html = f.read()

            self.browser.setHtml(html)

    def open_csv(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "CSV file (*.csv);;")
        print("Opened \"" + filename + "\" and HOPEFULLY created a graph from it.")
        # if filename:
        #     with open(filename, 'r') as f:
        #         html = f.read()
        #
        #     self.browser.setHtml(html)
        #
    def save_file(self):
        print("Saved the file")
        filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
                                                  "Hypertext Markup Language (*.htm *html);;"
                                                  "All files (*.*)")

        if filename:
            shutil.copy("./running/this_test.html",filename)

    def save_screenshot(self):
        p = self.browser.grab()
        p.save("test", 'jpg')

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def closeEvent(self, event):
        os.remove("./running/this_test.html")


app = QApplication(sys.argv)
app.setApplicationName("Network Visualization")
app.setOrganizationName("Team Banana")

window = MainWindow()

app.exec_()
