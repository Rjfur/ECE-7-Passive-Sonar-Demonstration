# PyQt5 imports for UI elements
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, \
                            QPushButton, QSizePolicy, qApp
from PyQt5.QtCore import pyqtSignal

# local UI imports
from ui.controlGroupBox import ControlGroupBox
from ui.plot import PlotCanvas

# local core imports
from core.input import UserInputStream
from core.output import UserOutputStream

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

        # initialize other classes
        self.inputStream = UserInputStream()
        self.outputStream = UserOutputStream()

        # signal connections
        # input and output modes use buttons, plot, audio streams
        self._main.controlLayout.controlGroupBox.beginInputModeSignal.connect(self.beginInputMode)
        self._main.controlLayout.controlGroupBox.endInputModeSignal.connect(self.endInputMode)
        self._main.controlLayout.controlGroupBox.beginOutputModeSignal.connect(self.beginOutputMode)
        self._main.controlLayout.controlGroupBox.endOutputModeSignal.connect(self.endOutputMode)
        self._main.controlLayout.muteSignal.connect(self.mute)
        self._main.controlLayout.unmuteSignal.connect(self.unmute)

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
        print("BEGINNING INPUT MODE...")
        self.inputStream.start()
        self._main.plot.beginAnimation(self.inputStream)

    def endInputMode(self):
        print("END INPUT MODE.")
        self.inputStream.stop()

    def beginOutputMode(self, btnID):
        print("BEGINNING OUTPUT MODE FOR BUTTON {0}...".format(btnID))
        self.outputStream.buttonToFile(btnID)

    def endOutputMode(self):
        print("END OUTPUT MODE.")
        self.outputStream.stopPlayback()

    def mute(self):
        print("SOUND MUTED.")

    def unmute(self):
        print("SOUND ON.")

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

    # signals
    muteSignal = pyqtSignal()
    unmuteSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.controlGroupBox = ControlGroupBox()    # defined in ui/controlGroupBox.py
        self.muteButton = QPushButton("Mute/Unmute")
        self.muteButton.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred))
        self.muteButton.setCheckable(True)

        self.muteButton.clicked.connect(self.onMuteButtonClicked)

        self.addWidget(self.controlGroupBox, 5)
        self.addWidget(self.muteButton, 1)

    def onMuteButtonClicked(self, btnChecked):
        if btnChecked:
            self.muteSignal.emit()
        else:
            self.unmuteSignal.emit()

# if __name__ == "__main__":
#     logging.info("Starting application.")
#     app = QApplication(sys.argv)
#     mainWindow = MainWindow()
#     sys.exit(app.exec_())