import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Initialise window
        """
        
        super().__init__()

        # ---- setup GUI elements ---- 
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        
        # ---- initialise variables ---- 
        
        
        # ---- initialise GUI with starting values ----
        self.signals()

    def show(self):
        """
        Displays main window
        """
        self.main_win.show()

    def signals(self):
        """
        Connects the UI buttons to the corresponding functions (see slots)
        """
        
        ...
        
    # ---- slots ----


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())