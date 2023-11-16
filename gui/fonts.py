"""
Custom fonts for the application.
"""

from PyQt6.QtGui import QFontDatabase


class CustomFonts:
    """Set custom font to use in the app."""

    def __init__(self):
        self.bello = self.add_font('assets/Bello-SmCp.ttf')
        self.fr_goth = self.add_font('assets/FrGoth-MdReg.ttf')

    @staticmethod
    def add_font(filename):
        """Add font to font database and return font family name."""

        font_id = QFontDatabase.addApplicationFont(filename)
        families = QFontDatabase.applicationFontFamilies(font_id)
        return families[0]
