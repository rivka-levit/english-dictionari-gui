from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont, QFontDatabase
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QScrollArea
)

from dictionary.api_dict import ApiDictionary
from .word import WordInputField, WordOutputField
from .fonts import CustomFonts


class MainWindow(QMainWindow):
    """Main window of the app."""

    def __init__(self):
        super().__init__()

        self.wrd_input = WordInputField()
        self.wrd_out = WordOutputField()
        self.definitions = QLabel('')
        self.set_ui()

    def set_ui(self):
        self.setWindowIcon(QIcon('assets/icon.svg'))
        self.setWindowTitle('Word Definition')
        self.setGeometry(0, 0, 380, 450)
        self._center()
        self.setStyleSheet(
            """
                QWidget {
                    background-color: #f5efe6;
                }
            """
        )

        widget = QWidget()
        widget.setLayout(self.set_main_layout())
        widget.setContentsMargins(20, 0, 20, 20)
        self.setCentralWidget(widget)

    def set_main_layout(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)

        header = QLabel('Word Definition')
        header.setFont(QFont(CustomFonts().bello, 28, 900))
        header.setStyleSheet('color: #7895b2;')
        main_layout.addWidget(header, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.set_nested_layout()

        main_layout.addLayout(self.set_nested_layout())
        main_layout.addWidget(self.wrd_out)

        self.definitions.setMinimumHeight(100)
        self.definitions.setWordWrap(True)
        self.definitions.setFont(QFont('Helvetica', 10))
        self.definitions.setStyleSheet('background-color: #fefcf9;')

        scroll_box = QScrollArea()
        scroll_box.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        scroll_box.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        scroll_box.setWidgetResizable(True)
        scroll_box.setStyleSheet(
            """
                QScrollArea {
                    border-radius: 5px;
                    padding: 10px 0 10px 10px;
                    color: #31373e;
                    background-color: #fefcf9;
                }
            """
        )
        scroll_box.setWidget(self.definitions)

        main_layout.addWidget(scroll_box)

        return main_layout

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self._set_output()
        else:
            super().keyPressEvent(event)

    def set_nested_layout(self):
        nest_layout = QHBoxLayout()
        nest_layout.addWidget(self.wrd_input, stretch=5)

        btn = QPushButton('Send')
        btn.setFixedHeight(40)
        btn.setMinimumWidth(80)
        btn.setFont(QFont(CustomFonts().fr_goth, 18))
        btn.setStyleSheet(
            """
                QPushButton {
                    background-color: #7895b2;
                    color: #f5efe6;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #849fb9;
                    color: #f5efe6;
                }
                QPushButton:pressed {
                    background-color: #486683;
                    color: #f5efe6;
                }
            """
        )
        nest_layout.addWidget(btn, stretch=1)
        btn.clicked.connect(self._set_output)

        return nest_layout

    def _set_output(self):
        dct = ApiDictionary()
        word = self.wrd_input.text()
        if word:
            self.wrd_out.setText(f'{word}')
            self.definitions.setText(
                f'\n{"-" * 55}\n'.join(dct.get_definition(word))
            )
            self.wrd_input.clear()
        else:
            self.definitions.setText('')
            self.wrd_out.clear()

    def _center(self):
        qt_rectangle = self.frameGeometry()
        center_point = self.screen().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
