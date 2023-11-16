"""
Fields for word input and output in the window.
"""
from PyQt6.QtWidgets import QLineEdit, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class WordInputField(QLineEdit):
    """Text field to enter a word."""

    def __init__(self):
        super().__init__()
        self.set_ui()

    def set_ui(self):
        """Set user interface."""

        self.setFont(QFont('Helvetica', 14))
        self.setFixedHeight(40)
        self.setPlaceholderText('Enter a word here...')
        self.setStyleSheet(
            """
                QLineEdit {
                    background-color: #fefcf9;
                    padding: 6px;
                    border: 2px solid #aebdca;
                    border-radius: 5px;
                    font-size: 26;
                    color: #31373e;
                }
            """
        )


class WordOutputField(QLabel):
    """Label for output the word that has been inputted by user."""

    def __init__(self):
        super().__init__()
        self.set_ui()

    def set_ui(self):
        """Set user interface."""

        self.setFont(QFont('Helvetica', 18, weight=700))
        self.setFixedHeight(50)
        self.setStyleSheet(
            f'qproperty-alignment: {Qt.AlignmentFlag.AlignCenter}; '
            f'border-radius: 5px; '
            f'padding: 8px; '
            f'color: #3d4650;'
            f'background-color: #fefcf9;'
        )
