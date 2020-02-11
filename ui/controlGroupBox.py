# PyQt5 imports for UI elements
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QPushButton, QSizePolicy, \
                            QButtonGroup, QGridLayout
from PyQt5.QtCore import pyqtSignal

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
        self.setLayout(self.buttonLayout)

    def initStreams(self):
        self.inStream = UserInputStream()
        self.outStream = UserOutputStream()

    #region BUTTON SETUP
    def initButtons(self):
        self.soundButtonLayout = QVBoxLayout()
        self.commentaryButtonLayout = QVBoxLayout()

        self.button1 = self.createButton("Whale", self.soundButtonLayout)
        self.button2 = self.createButton("Shrimp", self.soundButtonLayout)
        self.button3 = self.createButton("Shipping Trawler", self.soundButtonLayout)
        self.button4 = self.createButton("Quiet Target", self.soundButtonLayout)
        # self.hiddenButton = QPushButton()
        # self.hiddenButton.setCheckable(True)

        self.button1Commentary = self.createButton("? 1", self.commentaryButtonLayout)
        self.button2Commentary = self.createButton("? 2", self.commentaryButtonLayout)
        self.button3Commentary = self.createButton("? 3", self.commentaryButtonLayout)
        self.button4Commentary = self.createButton("? 4", self.commentaryButtonLayout)

        self.userInputButton = QPushButton("User Input")
        self.userInputButton.setCheckable(True)
        self.userInputButton.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred))

        self.userInputButton.clicked.connect(self.onUserInputButtonClicked)

        self.buttonLayout.addLayout(self.soundButtonLayout, 0, 0, 4, 1)
        self.buttonLayout.addLayout(self.commentaryButtonLayout, 0, 1, 4, 1)
        self.buttonLayout.addWidget(self.userInputButton, 4, 0, 1, 2)

    def createButton(self, name, layout):
        """
        creates a QPushButton with passed name, adds it to passed layout
        returns button object
        """
        btn = QPushButton(name)
        btn.setCheckable(True)
        layout.addWidget(btn)
        btn.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred))
        return btn

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
        self.commentaryButtonGroup.setExclusive(False)
        self.commentaryButtonGroup.addButton(self.button1Commentary, 1)
        self.commentaryButtonGroup.addButton(self.button2Commentary, 2)
        self.commentaryButtonGroup.addButton(self.button3Commentary, 3)
        self.commentaryButtonGroup.addButton(self.button4Commentary, 4)

        self.commentaryButtonGroup.buttonClicked.connect(self.onCommentaryButtonClicked)

    #endregion

    #region ON BUTTON CLICKED
    # methods called when buttons clicked, 
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
            # print("end input mode signal emitted")
            self.beginOutputModeSignal.emit(btnID)
            # print("begin output mode signal emitted (button {0})".format(btnID))
        else:
            self.endOutputModeSignal.emit()
            # print("end output mode signal emitted")

    def onCommentaryButtonClicked(self, btn):
        # stop playing of other sounds
        # stop playing of commentary sounds
        # stop input mode
        print("\t{0}".format(btn.text()))
        btnID = self.commentaryButtonGroup.checkedId()

        btnChecked = btn.isChecked()

        # uncheck all other buttons
        self.userInputButton.setChecked(False)
        for button in self.soundButtonGroup.buttons():
            button.setChecked(False)
        for button in self.commentaryButtonGroup.buttons():
            if button != btn:
                button.setChecked(False)
        if btnChecked:
            self.endInputModeSignal.emit()
            # print("end input mode signal emitted")
            # print(btnID)
            # print(len(self.soundButtonGroup.buttons()))
            self.beginOutputModeSignal.emit(btnID + len(self.soundButtonGroup.buttons()))
                                                    # first comm btn ID is after last sound btn ID
                                                    # allows number of sound buttons to change if needed
            # print("begin output mode signal emitted (button {0})".format(btnID))
        else:
            self.endOutputModeSignal.emit()
            # print("end output mode signal emitted")

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
            # print("end output mode signal emitted")
            self.beginInputModeSignal.emit()
            # print("begin input mode signal emitted")
        else:
            self.endInputModeSignal.emit()
            # print("end input mode signal emitted")

    #endregion