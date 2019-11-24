# PyQt5 imports for UI elements
from PyQt5.QtWidgets import QMainWindow, qApp, QMessageBox, QWidget, QTabWidget, \
                            QHBoxLayout, QVBoxLayout, QTableView, QLabel, \
                            QLineEdit, QGroupBox, QComboBox, QListWidget, \
                            QPushButton, QAction, QActionGroup, QAbstractItemView, \
                            QFileDialog, QApplication, QSizePolicy, QButtonGroup, QGridLayout
from PyQt5.QtCore import pyqtSignal

# Matplotlib imports for graphs/plots
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
# from matplotlib.backends.backend_qt5agg import FigureCanvas, \
#                                     NavigationToolbar2QT as NavigationToolbar
# from matplotlib.figure import Figure

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
        self.plot = PlotCanvas()
        self.controlLayout = ControlLayout()
        self.layout.addWidget(self.plot, 75)
        self.layout.addLayout(self.controlLayout, 25)
        self.setLayout(self.layout)

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        #self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()


    def plot(self):
        data = [6 for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()

class ControlLayout(QVBoxLayout):
    """
    description to be created at a later time
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.controlGroupBox = ControlGroupBox()
        self.muteButton = QPushButton("Mute/Unmute")
        self.muteButton.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred))

        self.addWidget(self.controlGroupBox, 5)
        self.addWidget(self.muteButton, 1)

class ControlGroupBox(QGroupBox):
    """
    description to be created at a later time
    """

    # signals
    soundButtonClicked = pyqtSignal(int)
    commentaryButtonClicked = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.buttonLayout = QGridLayout()
        self.initButtons()
        self.createSoundButtonGroup()
        self.createCommentaryButtonGroup()
        self.setButtonSizePolicies(QSizePolicy.Preferred, QSizePolicy.Preferred)    # set all button size policies
        self.setLayout(self.buttonLayout)

    def initButtons(self):
        self.soundButtonLayout = QVBoxLayout()
        self.commentaryButtonLayout = QVBoxLayout()

        self.button1 = QPushButton("Whale")
        self.button2 = QPushButton("Shrimp")
        self.button3 = QPushButton("Shipping Trawler")
        self.button4 = QPushButton("Quiet Target")
        self.button1.setCheckable(True)
        self.button2.setCheckable(True)
        self.button3.setCheckable(True)
        self.button4.setCheckable(True)
        #self.button1.toggle()

        self.soundButtonLayout.addWidget(self.button1)
        self.soundButtonLayout.addWidget(self.button2)
        self.soundButtonLayout.addWidget(self.button3)
        self.soundButtonLayout.addWidget(self.button4)

        self.button1Commentary = QPushButton("?")
        self.button2Commentary = QPushButton("?")
        self.button3Commentary = QPushButton("?")
        self.button4Commentary = QPushButton("?")

        self.commentaryButtonLayout.addWidget(self.button1Commentary)
        self.commentaryButtonLayout.addWidget(self.button2Commentary)
        self.commentaryButtonLayout.addWidget(self.button3Commentary)
        self.commentaryButtonLayout.addWidget(self.button4Commentary)

        self.button5 = QPushButton("User Input")

        self.buttonLayout.addLayout(self.soundButtonLayout, 0, 0, 4, 1)
        self.buttonLayout.addLayout(self.commentaryButtonLayout, 0, 1, 4, 1)
        self.buttonLayout.addWidget(self.button5, 4, 0, 1, 2)

    def createSoundButtonGroup(self):
        """
        Creates a QButtonGroup for the four output mode buttons. Makes it easier to determine which
        button within the group was pressed.
        """
        self.soundButtonGroup = QButtonGroup()
        self.soundButtonGroup.setExclusive(False)
        self.soundButtonGroup.addButton(self.button1, 1)
        self.soundButtonGroup.addButton(self.button2, 2)
        self.soundButtonGroup.addButton(self.button3, 3)
        self.soundButtonGroup.addButton(self.button4, 4)

        self.soundButtonGroup.buttonClicked.connect(self.onSoundButtonClicked)

    def onSoundButtonClicked(self, btn):
        print("{0}".format(btn.text()))
        print(self.soundButtonGroup.checkedId())
        #self.button1.toggle()

    def createCommentaryButtonGroup(self):
        """
        Creates a QButtonGroup for the four commentary buttons. Makes it easier to determine which
        button within the group was pressed.
        """
        self.commentaryButtonGroup = QButtonGroup()
        self.commentaryButtonGroup.addButton(self.button1Commentary, 1)
        self.commentaryButtonGroup.addButton(self.button2Commentary, 2)
        self.commentaryButtonGroup.addButton(self.button3Commentary, 3)
        self.commentaryButtonGroup.addButton(self.button4Commentary, 4)


    def setButtonSizePolicies(self, hSizePolicy, vSizePolicy):
        # left column, output mode sound buttons
        self.button1.setSizePolicy(QSizePolicy(hSizePolicy, vSizePolicy))
        self.button2.setSizePolicy(QSizePolicy(hSizePolicy, vSizePolicy))
        self.button3.setSizePolicy(QSizePolicy(hSizePolicy, vSizePolicy))
        self.button4.setSizePolicy(QSizePolicy(hSizePolicy, vSizePolicy))

        # right column, commentary buttons
        self.button1Commentary.setSizePolicy(QSizePolicy(hSizePolicy, vSizePolicy))
        self.button2Commentary.setSizePolicy(QSizePolicy(hSizePolicy, vSizePolicy))
        self.button3Commentary.setSizePolicy(QSizePolicy(hSizePolicy, vSizePolicy))
        self.button4Commentary.setSizePolicy(QSizePolicy(hSizePolicy, vSizePolicy))

        # button 5, user input button
        self.button5.setSizePolicy(QSizePolicy(hSizePolicy, vSizePolicy))

if __name__ == "__main__":
    logging.info("Starting application.")
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())