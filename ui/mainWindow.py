# PyQt5 imports for UI elements
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, \
                            QPushButton, QSizePolicy, qApp

# local UI imports
from ui.controlGroupBox import ControlGroupBox
from ui.plot import PlotCanvas

# local core imports

# For handling debug output
import logging

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

        # signal connections
        # input and output modes use buttons, plot, audio streams

        
        # set debug mode?
        self.debug = debug

        self.initUI()
        logging.info("UI loaded.")

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

    def closeEvent(self, event):
        """
        description to be created at a later time
        """
        logging.info("Application closed.")
        qApp.quit()

    def beginInputMode(self):
        pass

    def beginOutputMode(self):
        pass

    def endInputMode(self):
        pass

    def endOutputMode(self):
        pass

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

class ControlLayout(QVBoxLayout):
    """
    description to be created at a later time
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.controlGroupBox = ControlGroupBox()    # defined in ui/controlGroupBox.py
        self.muteButton = QPushButton("Mute/Unmute")
        self.muteButton.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred))

        self.addWidget(self.controlGroupBox, 5)
        self.addWidget(self.muteButton, 1)

# if __name__ == "__main__":
#     logging.info("Starting application.")
#     app = QApplication(sys.argv)
#     mainWindow = MainWindow()
#     sys.exit(app.exec_())