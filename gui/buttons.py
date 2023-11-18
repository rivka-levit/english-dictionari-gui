"""
Buttons for the app.
"""

from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont


class SendButton(QPushButton):
    """Button to send a word to the dictionary."""

    def __init__(self, slot=None, fonts=None):
        super().__init__()
        self.fonts = fonts
        self.set_ui()
        self.clicked.connect(slot=slot)

    def set_ui(self):
        """Set user interface."""

        self.setText('Send')
        self.setFixedHeight(40)
        self.setMinimumWidth(80)
        self.setFont(QFont(self.fonts.fr_goth, 18))
        self.setStyleSheet(
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
