from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel
)

from dictionary.api_dict import ApiDictionary
from .word import WordInputField, WordOutputField
from .fonts import CustomFonts
from .buttons import SendButton
from .scroll_box import ScrollDefinitions


class MainWindow(QMainWindow):
    """Main window of the app."""

    def __init__(self):
        super().__init__()

        self.wrd_input = WordInputField(slot=self.slot_output)
        self.wrd_out = WordOutputField()
        self.scroll_box = ScrollDefinitions()
        self.set_ui()

    def set_ui(self):
        """Set user interface."""

        self.setWindowIcon(QIcon('assets/icon.ico'))
        self.setWindowTitle('Word Definition')
        self.setStyleSheet('background-color: #f5efe6;')
        self.setGeometry(0, 0, 380, 450)
        self.center_window()

        central_widget = QWidget(parent=self)
        central_widget.setLayout(self.set_main_layout())
        central_widget.setContentsMargins(20, 0, 20, 20)
        self.setCentralWidget(central_widget)

    def set_main_layout(self):
        """Layout contains all the elements of the main window."""

        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)

        header = QLabel('Word Definition')
        header.setFont(QFont(CustomFonts().bello, 28, 900))
        header.setStyleSheet('color: #7895b2;')
        main_layout.addWidget(header, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Word input field and send button
        self.set_nested_layout()
        main_layout.addLayout(self.set_nested_layout())

        # Word output area
        main_layout.addWidget(self.wrd_out)

        # Definitions output area
        main_layout.addWidget(self.scroll_box)

        return main_layout

    def set_nested_layout(self):
        """Layout contains word input field and send button."""

        nest_layout = QHBoxLayout()
        nest_layout.addWidget(self.wrd_input, stretch=5)

        btn = SendButton(self.slot_output)
        nest_layout.addWidget(btn, stretch=1)

        return nest_layout

    def slot_output(self):
        """Output definitions to the scroll area."""

        dct = ApiDictionary()
        word = self.wrd_input.text()
        if word:
            self.wrd_out.setText(f'{word}')
            self.scroll_box.definitions.setText(
                f'\n{"-" * 55}\n'.join(dct.get_definition(word))
            )
            self.wrd_input.clear()
        else:
            self.scroll_box.definitions.setText('')
            self.wrd_out.clear()

    def center_window(self):
        """Open main window always in the center."""

        qt_rectangle = self.frameGeometry()
        center_point = self.screen().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())
