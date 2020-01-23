import sys
import logging

from PyQt5.QtWidgets import QApplication    # for starting UI

from ui.mainWindow import MainWindow    # local import

def main():
    logging.info("Starting application.")
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()