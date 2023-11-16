"""
Definitions labels.
"""

from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QFont


class Definition(QLabel):
    """Word definition label."""

    def __init__(self):
        super().__init__()
        self.set_ui()

    def set_ui(self):
        """Set user interface."""

        self.setMinimumHeight(100)
        self.setWordWrap(True)
        self.setFont(QFont('Helvetica', 10))
        self.setStyleSheet('background-color: #fefcf9;')
