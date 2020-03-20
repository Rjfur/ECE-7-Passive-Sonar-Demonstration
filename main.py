import sys
import argparse # for handling command line arguments
import logging  # for handling debug output

from PyQt5.QtWidgets import QApplication    # for starting UI

from ui.mainWindow import MainWindow    # local import

def main():
    logging.info("Starting application.")
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    # command line arguments
    parser = argparse.ArgumentParser(description="Passive Sonar Demonstration System")
    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    debug = False

    if args.debug:
        debug = True
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
        logging.debug("In DEBUG mode.")
    elif args.verbose:
        # if using verbose output set logging to display level and message
        # print anything level debug or higher
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
        logging.info("Using verbose output.")
    else:
        # if not using verbose output only print errors and warnings
        logging.basicConfig(format="%(levelname)s: %(message)s")

    main()
