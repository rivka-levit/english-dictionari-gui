"""
Scroll area for definitions.
"""

from PyQt6.QtWidgets import QScrollArea
from PyQt6.QtCore import Qt

from .definitions import Definition


class ScrollDefinitions(QScrollArea):
    """Scroll box for definitions."""

    def __init__(self):
        super().__init__()
        self.definitions = Definition()
        self.set_ui()

    def set_ui(self):
        """Set user interface."""

        self.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        self.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.setWidgetResizable(True)
        self.setStyleSheet(
            """
                QScrollArea {
                    border-radius: 5px;
                    padding: 10px 0 10px 10px;
                    color: #31373e;
                    background-color: #fefcf9;
                }
            """
        )
        self.setWidget(self.definitions)
