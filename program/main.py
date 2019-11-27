#!/usr/bin/env python

##########################
# Network Visualizer Tool
# By Danny Ullrich,
#    Adam Cook,
#    Caden Koscinski
#
# Icons by Chanut on www.flaticon.com
##########################


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

import network
import qdarkstyle

import os
import shutil
import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.graphExists = False

        self.l1 = QLabel()

        self.l1.setText("Welcome to Network Visualizer! Please Open or Import a network!")
        self.l1.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.l1)
        self.setWindowTitle("Network Visualizer")

        self.setWindowIcon(QIcon('./images/internet.png'))
        self.setFixedSize(1600,900)
        #self.status = QStatusBar()
        #self.setStatusBar(self.status)
        toolbar = self.addToolBar("Actions")
        # toolbar.setIconSize(QSize(16, 16))
        # self.addToolBar(toolbar)
        # Uncomment to disable native menubar on Mac
        # self.menuBar().setNativeMenuBar(False)

        #file_menu = self.menuBar().addMenu("File")

        open_file_action = QAction(QIcon("./images/folder.png"), "Open Graph File...", self)
        open_file_action.setStatusTip("Open Graph from File")
        open_file_action.triggered.connect(self.open_file)
        #file_menu.addAction(open_file_action)
        toolbar.addAction(open_file_action)

        open_csv_action = QAction(QIcon("./images/document.png"), "Open CSV File...", self)
        open_csv_action.setStatusTip("Open CSV and Generate Graph from File")
        open_csv_action.triggered.connect(self.open_csv)
        #file_menu.addAction(open_csv_action)
        toolbar.addAction(open_csv_action)

        self.save_screenshot_action = QAction(QIcon("./images/picture.png"), "Save Screenshot...", self)
        self.save_screenshot_action.setStatusTip("Save Screenshot")
        self.save_screenshot_action.triggered.connect(self.save_screenshot)
        #file_menu.addAction(save_screenshot_action)
        toolbar.addAction(self.save_screenshot_action)

        self.save_file_action = QAction(QIcon("./images/download.png"), "Save Graph...", self)
        self.save_file_action.setStatusTip("Save current graph to HTML file")
        self.save_file_action.triggered.connect(self.save_file)
        #file_menu.addAction(save_file_action)
        toolbar.addAction(self.save_file_action)

        self.save_file_action.setEnabled(False)
        self.save_screenshot_action.setEnabled(False)
        self.show()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "Hypertext Markup Language (*.htm *.html);;")
        if filename:
            self.graphExists = True
            self.updatePage(filename)

    def open_csv(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                  "CSV file (*.csv);;")

        self.graphExists = True
        network.build_network("graph", filename)
        self.updatePage("./running/graph.html")
        #print("Opened \"" + filename + "\" and HOPEFULLY created a graph from it.")
        # if filename:
        #     with open(filename, 'r') as f:
        #         html = f.read()
        #
        #     self.browser.setHtml(html)
        #
    def save_file(self):
        print("Saved the file")
        filename, _ = QFileDialog.getSaveFileName(self, "Save Page", "",
                                                  "Hypertext Markup Language (*.htm *.html);;"
                                                  "All files (*.*)")

        if filename:
            shutil.copy("./running/graph.html",filename + ".html")

    def save_screenshot(self):
        p = self.browser.grab()
        filename, _ = QFileDialog.getSaveFileName(self, "Save Screenshot", "",
                                                  "JPG / JPEG (*.JPG *.JPEG);;"
                                                  "All files (*.*)")
        p.save(filename + ".jpg", "jpg")
        print("Saved: " + filename + ".jpg")

    def closeEvent(self, event):
        dir = os.listdir("./running/")

        for file in dir:
            if file.endswith(".html"):
                os.remove(os.path.join(dir, file))

    def updatePage(self, page):
        if self.graphExists == True:
            with open(page, 'r') as f:
                html = f.read()

            # print("Update Ran!")
            self.browser.setHtml(html)
            self.setCentralWidget(self.browser)
            self.save_file_action.setEnabled(True)
            self.save_screenshot_action.setEnabled(True)


app = QApplication([])
app.setApplicationName("Network Visualizer")
app.setOrganizationName("Team Banana")
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

window = MainWindow()

app.exec_()
