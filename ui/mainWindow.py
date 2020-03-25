# PyQt5 imports for UI elements
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, \
                            QPushButton, QSizePolicy, qApp
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtMultimedia import QSound

# local UI imports
from ui.controlGroupBox import ControlGroupBox
from ui.plot import PlotCanvas

# local core imports
from core.input import UserInputStream
from core.output import UserOutputStream

# For handling debug output
import logging

# used for measuring time for debugging
import time

class MainWindow(QMainWindow):
    # debug mode?
    def __init__(self, debug):
        """
        description to be created at a later time
        """
        super().__init__()

        # set debug mode
        self.debug = debug

        # setup main window parameters
        self.title = "Passive Sonar Demonstration System"
        self.left = 100
        self.top = 100
        self.width = 1080
        self.height = 720
        self.minWidth = 800
        self.minHeight = 600
        self._main = MainWidget(debug)
        self.setCentralWidget(self._main)

        # initialize other classes
        self.inputStream = UserInputStream(debug)
        self.outputStream = UserOutputStream()

        # signal connections
        # input and output modes use buttons, plot, audio streams
        self._main.controlLayout.controlGroupBox.beginInputModeSignal.connect(self.beginInputMode)
        self._main.controlLayout.controlGroupBox.endInputModeSignal.connect(self.endInputMode)
        self._main.controlLayout.controlGroupBox.beginOutputModeSignal.connect(self.beginOutputMode)
        self._main.controlLayout.controlGroupBox.endOutputModeSignal.connect(self.endOutputMode)
        self._main.controlLayout.muteSignal.connect(self.mute)
        self._main.controlLayout.unmuteSignal.connect(self.unmute)

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
        logging.info("BEGINNING INPUT MODE...")
        self.inputStream.start()
        self._main.plot.beginAnimation(self.inputStream)
        if self.debug["time_buttons"]:
            logging.info("Time to begin input mode: {0} seconds".format(time.time() - self._main.controlLayout.controlGroupBox.clickedTime))

    def endInputMode(self):
        logging.info("END INPUT MODE.")
        self.inputStream.stop()
        # starting output mode runs the endInputMode method
        # if input mode has not been run, the animation was not created yet
        try:
            self._main.plot.anim.event_source.stop()    # make sure animation stops
        except AttributeError:
            pass
        if self.debug["time_buttons"]:
            logging.info("Time to stop input mode: {0} seconds".format(time.time() - self._main.controlLayout.controlGroupBox.clickedTime))

    def beginOutputMode(self, btnID):
        logging.info("BEGINNING OUTPUT MODE FOR BUTTON {0}...".format(btnID))
        self.outputStream.buttonToFile(btnID)
        if self.debug["time_buttons"]:
            logging.info("Time to begin output mode: {0} seconds".format(time.time() - self._main.controlLayout.controlGroupBox.clickedTime))

    def endOutputMode(self):
        logging.info("END OUTPUT MODE.")
        self.outputStream.stopPlayback()
        if self.debug["time_buttons"]:
            logging.info("Time to stop output mode: {0} seconds".format(time.time() - self._main.controlLayout.controlGroupBox.clickedTime))

    def mute(self):
        logging.info("SOUND MUTED.")
        if self.debug["time_buttons"]:
            logging.info("Time to mute: {0} seconds".format(time.time() - self._main.controlLayout.muteClickedTime))

    def unmute(self):
        logging.info("SOUND ON.")
        if self.debug["time_buttons"]:
            logging.info("Time to unmute: {0} seconds".format(time.time() - self._main.controlLayout.muteClickedTime))

class MainWidget(QWidget):
    """
    description to be created at a later time
    """
    def __init__(self, debug):
        super().__init__()
        self.initUI(debug)

    def initUI(self, debug):
        self.layout = QHBoxLayout()
        self.plot = PlotCanvas(debug)
        self.controlLayout = ControlLayout(debug)
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

    def __init__(self, debug):
        super().__init__()
        self.initUI(debug)

    def initUI(self, debug):
        self.controlGroupBox = ControlGroupBox(debug)    # defined in ui/controlGroupBox.py
        self.muteButton = QPushButton("Mute/Unmute")
        self.muteButton.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred))
        self.muteButton.setCheckable(True)

        self.muteButton.clicked.connect(self.onMuteButtonClicked)

        self.addWidget(self.controlGroupBox, 5)
        self.addWidget(self.muteButton, 1)

    def onMuteButtonClicked(self, btnChecked):
        self.muteClickedTime = time.time()
        if btnChecked:
            self.muteSignal.emit()
        else:
            self.unmuteSignal.emit()

# if __name__ == "__main__":
#     logging.info("Starting application.")
#     app = QApplication(sys.argv)
#     mainWindow = MainWindow()
#     sys.exit(app.exec_())