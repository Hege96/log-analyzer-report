from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QWidgetAction, QFileDialog
import re
from datetime import datetime
import ipaddress
from logreport.parser import parse_line
from logreport.aggregations import status_counts, top_ips, top_paths

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
            self.load_log(path)

    def load_log(self,path):
        with open(path, "r", encoding="utf-8", errors="ignore") as file:
            entries=[]
            for line in file:
                rec=parse_line(line)
                if rec:
                    entries.append(rec)
        self.entries = entries
        self.statusBar().showMessage(f"Loaded {len(entries)} records from {path}")
        self.refresh_views()

    def refresh_views(self):
        if not getattr(self, "entries", None):
            self.statusBar().showMessage("No data loaded")
            return
        print("Status:", status_counts(self.entries)[:5])
        print("Top IPs:", top_ips(self.entries, top=5))
        print("Top paths:", top_paths(self.entries, top=5))
        self.statusBar().showMessage(f"Loaded {len(self.entries)} records | stats ready")


