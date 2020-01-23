# PyQt5 imports for UI elements
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QPushButton, QSizePolicy, \
                            QButtonGroup, QGridLayout
from PyQt5.QtCore import pyqtSignal

# local core inputs
from core.input import UserInputStream
from core.output import UserOutputStream

class ControlGroupBox(QGroupBox):
    """
    description to be created at a later time
    """

    # signals
    beginInputModeSignal = pyqtSignal()
    endInputModeSignal = pyqtSignal()
    beginOutputModeSignal = pyqtSignal(int)
    endOutputModeSignal = pyqtSignal()

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

    def initStreams(self):
        self.inStream = UserInputStream()
        self.outStream = UserOutputStream()

    def initButtons(self):
        self.soundButtonLayout = QVBoxLayout()
        self.commentaryButtonLayout = QVBoxLayout()

        self.button1 = QPushButton("Whale")
        self.button2 = QPushButton("Shrimp")
        self.button3 = QPushButton("Shipping Trawler")
        self.button4 = QPushButton("Quiet Target")
        # self.hiddenButton = QPushButton()
        self.button1.setCheckable(True)
        self.button2.setCheckable(True)
        self.button3.setCheckable(True)
        self.button4.setCheckable(True)
        # self.hiddenButton.setCheckable(True)
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

        self.userInputButton = QPushButton("User Input")
        self.userInputButton.setCheckable(True)
        self.userInputButton.clicked.connect(self.onUserInputButtonClicked)

        self.buttonLayout.addLayout(self.soundButtonLayout, 0, 0, 4, 1)
        self.buttonLayout.addLayout(self.commentaryButtonLayout, 0, 1, 4, 1)
        self.buttonLayout.addWidget(self.userInputButton, 4, 0, 1, 2)

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
        # self.soundButtonGroup.addButton(self.hiddenButton, 5)

        self.soundButtonGroup.buttonClicked.connect(self.onSoundButtonClicked)

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
        self.userInputButton.setSizePolicy(QSizePolicy(hSizePolicy, vSizePolicy))

    def onSoundButtonClicked(self, btn):
        # stop playing of other sounds
        # stop playing of commentary sounds
        # stop input mode
        print("\t{0}".format(btn.text()))
        btnID = self.soundButtonGroup.checkedId()

        btnChecked = btn.isChecked()

        # uncheck all other buttons
        self.userInputButton.setChecked(False)
        for button in self.commentaryButtonGroup.buttons():
            button.setChecked(False)
        for button in self.soundButtonGroup.buttons():
            if button != btn:
                button.setChecked(False)

        # if turning button on
        #   emit endInputModeSignal
        #   emit beginOutputModeSignal(btn)
        # else
        #   emit endOutputModeSignal(btn)

        if btnChecked:
            self.endInputModeSignal.emit()
            print("end input mode signal emitted")
            self.beginOutputModeSignal.emit(btnID)
            print("begin output mode signal emitted (button {0})".format(btnID))
        else:
            self.endOutputModeSignal.emit()
            print("end output mode signal emitted")

    def onUserInputButtonClicked(self, btnChecked):
        # uncheck all other buttons
        for button in self.commentaryButtonGroup.buttons():
            button.setChecked(False)
        for button in self.soundButtonGroup.buttons():
            button.setChecked(False)

        # if turning button on
        #   emit endOutputModeSignal
        #   emit beginInputModeSignal
        # else
        #   emit endInputModeSignal

        if btnChecked:
            self.endOutputModeSignal.emit()
            print("end output mode signal emitted")
            self.beginInputModeSignal.emit()
            print("begin input mode signal emitted")
        else:
            self.endInputModeSignal.emit()
            print("end input mode signal emitted")