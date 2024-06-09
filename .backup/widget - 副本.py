# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.PL_Data = []
        self.Enemy_Data = []

        # Connect signals and slots
        self.ui.lineEdit_4.editingFinished.connect(self.create_pl_data)
        self.ui.lineEdit_5.editingFinished.connect(self.create_enemy_data)
        self.ui.comboBox_2.currentTextChanged.connect(self.update_spinbox_limit)
        self.ui.spinBox.valueChanged.connect(self.update_data)

        self.line_edits = [self.ui.lineEdit_6, self.ui.lineEdit_7, self.ui.lineEdit_8, self.ui.lineEdit_9, self.ui.lineEdit_10, self.ui.lineEdit_11]
        for line_edit in self.line_edits:
            line_edit.editingFinished.connect(self.update_data)

        self.update_ui()

    def create_pl_data(self):
        num = int(self.ui.lineEdit_4.text())
        self.PL_Data = [[] for _ in range(num)]
        self.update_spinbox_limit()

    def create_enemy_data(self):
        num = int(self.ui.lineEdit_5.text())
        self.Enemy_Data = [[] for _ in range(num)]
        self.update_spinbox_limit()

    def update_spinbox_limit(self):
        if self.ui.comboBox_2.currentText() == "PL":
            self.ui.spinBox.setMaximum(len(self.PL_Data))
            self.ui.label_8.show()
            self.ui.lineEdit_11.show()
        else:
            self.ui.spinBox.setMaximum(len(self.Enemy_Data))
            self.ui.label_8.hide()
            self.ui.lineEdit_11.hide()

    def update_data(self):
        index = self.ui.spinBox.value() - 1
        if self.ui.comboBox_2.currentText() == "PL":
            if index < len(self.PL_Data):
                self.PL_Data[index] = [le.text() for le in self.line_edits[:5]]
                self.PL_Data[index].append(self.ui.lineEdit_11.text())
                self.update_text_browser(self.ui.textBrowser, self.PL_Data, "PL_Data")
        else:
            if index < len(self.Enemy_Data):
                self.Enemy_Data[index] = [le.text() for le in self.line_edits[:5]]
                self.update_text_browser(self.ui.textBrowser_13, self.Enemy_Data, "Enemy_Data")

    def update_text_browser(self, text_browser, data_list, prefix):
        text_browser.clear()
        for i, data in enumerate(data_list):
            if data:
                text_browser.append(f"{prefix}_{i+1}: {', '.join(data)}")

    def update_ui(self):
        self.update_spinbox_limit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
