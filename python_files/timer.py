import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QTimer
from ui_timer import Ui_MainWindow


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
        
        # ---- initialise variable ---- 
        self.timer = QTimer(self)
        self.time = 0
        
        # ---- initialise GUI with starting values ----
        self.signals()

    def show(self):
        """
        Displays main window
        """
        self.main_win.show()

    def convert_time(self, seconds):
        """
        Returns a m:ss represenation of the seconds
        """
        mins = str(seconds // 60)
        secs = f"0{str(seconds % 60)}" if seconds % 60 < 10 else str(seconds % 60)
        return f"{mins}:{secs}"

    def signals(self):
        """
        Connects the UI buttons to the corresponding functions (see slots)
        """
        self.timer.timeout.connect(self.update_time)
        self.ui.start_btn.clicked.connect(self.start_timer)
        self.ui.stop_btn.clicked.connect(self.stop_timer)
        self.ui.reset_btn.clicked.connect(self.reset_timer)
        
    # ---- slots ----
    def update_time(self):
        """
        Changes the value of the timer on display
        """
        self.time += 1
        self.ui.time_lb.setText(self.convert_time(self.time))
        
    def start_timer(self):
        """
        Starts the timer running
        """
        self.timer.start(1000)
        
    def stop_timer(self):
        """
        Stops the timer
        """
        self.timer.stop()
        
    def reset_timer(self):
        """
        Stops the timer and resets it to 0
        """
        self.timer.stop()
        self.time = 0
        self.ui.time_lb.setText(self.convert_time(self.time))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())