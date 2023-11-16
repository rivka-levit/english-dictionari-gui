import sys
from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow


def main() -> None:
    """
    Run application.
    :rtype: object
    :return: None
    """

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


main()
