from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QWidgetAction, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Log Analyzer")
        self.resize(1200,700)
        self.statusBar().showMessage("Ready")

        file_menu=self.menuBar().addMenu("File")

        open_act=QAction("Open Log...", self)
        open_act.triggered.connect(self.on_open)
        file_menu.addAction(open_act)

        exit_act=QAction("Exit", self)
        exit_act.triggered.connect(self.close)
        file_menu.addAction(exit_act)

    def on_open(self):
        path,_=QFileDialog.getOpenFileName(self,"Open Log", "", "Log files (*.log *.txt);;All files (*.*)")
        if path:
            self.current_path=path
            self.statusBar().showMessage(f"Selected: {path}")
