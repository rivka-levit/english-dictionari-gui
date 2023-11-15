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
        self.setWindowTitle('Word Definition')
        self.setGeometry(0, 0, 500, 300)

        self.center()

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)

        nest_layout = QHBoxLayout()

        self.wrd_input = QLineEdit()
        nest_layout.addWidget(self.wrd_input, stretch=5)

        btn = QPushButton('Convert')
        nest_layout.addWidget(btn, stretch=1)

        self.definitions = QLabel('')
        self.definitions.setMinimumHeight(100)

        main_layout.addLayout(nest_layout)
        main_layout.addWidget(self.definitions)

        widget = QWidget()
        widget.setLayout(main_layout)
        # widget.setStyleSheet('background-color: #F2EDDC;')
        widget.setContentsMargins(20, 20, 20, 20)
        self.setCentralWidget(widget)

    def center(self):
        qt_rectangle = self.frameGeometry()
        center_point = self.screen().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
