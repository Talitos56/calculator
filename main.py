import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from components_package import info, styles
from components_package.buttons import ButtonsGrid
from components_package.display import Display
from components_package.main_window import MainWindow
from components_package.variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    app = QApplication(sys.argv)
    styles.setupTheme()
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    inform = info.Info('Sua conta')
    window.addWidgetToVLayout(inform)

    # Display
    display = Display()
    # display.setPlaceholderText('Digite algo')
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, inform, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
