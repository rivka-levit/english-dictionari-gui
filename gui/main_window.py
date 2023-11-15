from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
)

import sys


class MainWindow(QMainWindow):
    """Main window of the app."""

    def __init__(self):
        super().__init__()
        self.wrd_input = QLineEdit()
        self.definitions = QLabel('')
        self._set_main_window()

    def _set_main_window(self):
        self.setWindowIcon(QIcon('assets/icon.svg'))
        self.setWindowTitle('Word Definition')
        self.setGeometry(0, 0, 500, 300)
        self._center()

        widget = QWidget()
        widget.setLayout(self._set_main_layout())
        # widget.setStyleSheet('background-color: #F2EDDC;')
        widget.setContentsMargins(20, 20, 20, 20)
        self.setCentralWidget(widget)

    def _set_main_layout(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)

        main_layout.addLayout(self._set_nested_layout())

        self.definitions.setMinimumHeight(100)
        main_layout.addWidget(self.definitions)

        return main_layout

    def _set_nested_layout(self):
        nest_layout = QHBoxLayout()

        nest_layout.addWidget(self.wrd_input, stretch=5)

        btn = QPushButton('Convert')
        nest_layout.addWidget(btn, stretch=1)

        return nest_layout

    def _center(self):
        qt_rectangle = self.frameGeometry()
        center_point = self.screen().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
