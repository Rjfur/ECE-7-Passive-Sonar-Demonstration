# PyQt5 imports for UI elements
from PyQt5.QtWidgets import QMainWindow, qApp, QMessageBox, QWidget, QTabWidget, \
                            QHBoxLayout, QVBoxLayout, QTableView, QLabel, \
                            QLineEdit, QGroupBox, QComboBox, QListWidget, \
                            QPushButton, QAction, QActionGroup, QAbstractItemView, \
                            QFileDialog, QApplication, QSizePolicy
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
        self.axes = fig.add_subplot(111)

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
        self.muteButton = QPushButton()
        self.muteButton.setText("Mute/Unmute")
        self.muteButton.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding))

        self.addWidget(self.controlGroupBox, 7)
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
        self.buttonLayout = QVBoxLayout()
        self.initButtons()
        self.setLayout(self.buttonLayout)

    def initButtons(self):
        self.button1Layout = QHBoxLayout()
        self.button1 = QPushButton()
        self.button1.setText("Whale")
        self.button1.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding))
        self.button1Commentary = QPushButton()
        self.button1Commentary.setText("?")
        self.button1Commentary.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding))
        self.button1Layout.addWidget(self.button1, 3)
        self.button1Layout.addWidget(self.button1Commentary, 1)
        self.buttonLayout.addLayout(self.button1Layout)

        self.button2Layout = QHBoxLayout()
        self.button2 = QPushButton()
        self.button2.setText("Shrimp")
        self.button2.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding))
        self.button2Commentary = QPushButton()
        self.button2Commentary.setText("?")
        self.button2Commentary.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding))
        self.button2Layout.addWidget(self.button2, 3)
        self.button2Layout.addWidget(self.button2Commentary, 1)
        self.buttonLayout.addLayout(self.button2Layout)

        self.button3Layout = QHBoxLayout()
        self.button3 = QPushButton()
        self.button3.setText("Shipping Trawler")
        self.button3.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding))
        self.button3.clicked.connect()
        self.button3Commentary = QPushButton()
        self.button3Commentary.setText("?")
        self.button3Commentary.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding))
        self.button3Layout.addWidget(self.button3, 3)
        self.button3Layout.addWidget(self.button3Commentary, 1)
        self.buttonLayout.addLayout(self.button3Layout)

        self.button4Layout = QHBoxLayout()
        self.button4 = QPushButton()
        self.button4.setText("Quiet Target")
        self.button4.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding))
        self.button4Commentary = QPushButton()
        self.button4Commentary.setText("?")
        self.button4Commentary.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding))
        self.button4Layout.addWidget(self.button4, 3)
        self.button4Layout.addWidget(self.button4Commentary, 1)
        self.buttonLayout.addLayout(self.button4Layout)
        
        self.button5 = QPushButton()
        self.button5.setText("User")
        self.button5.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding))
        self.buttonLayout.addWidget(self.button5)

    def button1Pressed(self):
        pass

    def button1Pressed(self):
        pass

    def button1Pressed(self):
        pass

    def button1Pressed(self):
        pass

    def button1Pressed(self):
        pass

    def button1Pressed(self):
        pass

    def button1Pressed(self):
        pass


if __name__ == "__main__":
    logging.info("Starting application.")
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())