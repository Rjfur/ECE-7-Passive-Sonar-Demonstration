# PyQt5 imports for UI elements
from PyQt5.QtWidgets import QMainWindow, qApp, QMessageBox, QWidget, QTabWidget, \
                            QHBoxLayout, QVBoxLayout, QTableView, QLabel, \
                            QLineEdit, QGroupBox, QComboBox, QListWidget, \
                            QPushButton, QAction, QActionGroup, QAbstractItemView, \
                            QFileDialog, QApplication
from PyQt5.QtCore import pyqtSignal

# Matplotlib imports for graphs/plots
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# For handling debug output
import logging

import sys


class MainWindow(QMainWindow):
    # debug mode?
    def __init__(self, debug=False):
        """
        description to be created at a later time
        """
        super().__init__()

        # setup main window parameters
        self.title = "Passive Sonar Demonstration System"
        self.left = 100
        self.top = 100
        self.width = 1080
        self.height = 720
        self.minWidth = 800
        self.minHeight = 600
        self._main = MainWidget()
        self.setCentralWidget(self._main)
        
        # set debug mode?
        self.debug = debug

        self.initUI()
        logging.info("UI loaded.")

    def closeEvent(self, event):
        """
        description to be created at a later time
        """
        logging.info("Application closed.")
        qApp.quit()

    def initUI(self):
        """
        description to be created at a later time
        """
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setMinimumSize(self.minWidth, self.minHeight)
        self.horizontalLayout = QHBoxLayout()
        self.setCentralWidget = self.horizontalLayout

        #self.statusBar().showMessage("")
        self.show()

class MainWidget(QWidget):
    """
    description to be created at a later time
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout()
        self.plot = Plot()
        self.controlLayout = ControlLayout()
        self.layout.addWidget(self.plot, 75)
        self.layout.addLayout(self.controlLayout, 25)
        self.setLayout(self.layout)

class Plot(QTableView):
    """
    description to be created at a later time
    """
    def __init__(self):
        super().__init__()

class ControlLayout(QVBoxLayout):
    """
    description to be created at a later time
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.controlGroupBox = ControlGroupBox()
        self.muteButton = QPushButton()

        self.addWidget(self.controlGroupBox)
        self.addWidget(self.muteButton)

class ControlGroupBox(QGroupBox):
    """
    description to be created at a later time
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.buttonLayout = QVBoxLayout()
        self.initButtons()
        self.setLayout(self.buttonLayout)

    def initButtons(self):
        self.button1Layout = QHBoxLayout()
        self.button1 = QPushButton()
        self.button1Commentary = QPushButton()
        self.button1Layout.addWidget(self.button1)
        self.button1Layout.addWidget(self.button1Commentary)
        self.buttonLayout.addLayout(self.button1Layout)

        self.button2Layout = QHBoxLayout()
        self.button2 = QPushButton()
        self.button2Commentary = QPushButton()
        self.button2Layout.addWidget(self.button2)
        self.button2Layout.addWidget(self.button2Commentary)
        self.buttonLayout.addLayout(self.button2Layout)

        self.button3Layout = QHBoxLayout()
        self.button3 = QPushButton()
        self.button3Commentary = QPushButton()
        self.button3Layout.addWidget(self.button3)
        self.button3Layout.addWidget(self.button3Commentary)
        self.buttonLayout.addLayout(self.button3Layout)

        self.button4Layout = QHBoxLayout()
        self.button4 = QPushButton()
        self.button4Commentary = QPushButton()
        self.button4Layout.addWidget(self.button4)
        self.button4Layout.addWidget(self.button4Commentary)
        self.buttonLayout.addLayout(self.button4Layout)
        
        self.button5 = QPushButton()
        self.buttonLayout.addWidget(self.button5)


if __name__ == "__main__":
    logging.info("Starting application.")
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())