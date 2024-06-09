import sys
import json
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizePolicy, QFileDialog, QMessageBox
from PySide6.QtGui import QIntValidator
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.PL_Data = []
        self.Enemy_Data = []

        # Set SpinBox minimum value to 1
        self.ui.spinBox.setMinimum(1)

        # Connect signals and slots
        self.ui.lineEdit_4.editingFinished.connect(self.create_pl_data)
        self.ui.lineEdit_5.editingFinished.connect(self.create_enemy_data)
        self.ui.comboBox_2.currentTextChanged.connect(self.update_spinbox_limit)
        self.ui.spinBox.valueChanged.connect(self.update_line_edits)
        self.ui.pushButton_4.clicked.connect(self.sort_and_display_third_element)
        self.ui.pushButton_3.clicked.connect(self.export_to_json)
        self.ui.pushButton_2.clicked.connect(self.import_from_json)

        self.line_edits = [self.ui.lineEdit_6, self.ui.lineEdit_7, self.ui.lineEdit_8, self.ui.lineEdit_9, self.ui.lineEdit_10, self.ui.lineEdit_11]
        for line_edit in self.line_edits:
            line_edit.editingFinished.connect(self.update_data)

        self.ui.lineEdit_3.editingFinished.connect(self.validate_lineEdit_3)
        self.ui.lineEdit_2.editingFinished.connect(self.validate_lineEdit_2)
        self.ui.pushButton_13.clicked.connect(self.calculate_damage)

        # Set up layout to make the TabWidget resize with the window
        layout = QVBoxLayout(self)
        layout.addWidget(self.ui.tabWidget)
        self.setLayout(layout)

        # Ensure the TabWidget resizes proportionally
        self.ui.tabWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Initial UI update
        self.update_ui()

    def create_pl_data(self):
        try:
            num = int(self.ui.lineEdit_4.text())
            self.PL_Data = [[] for _ in range(num)]
            self.update_spinbox_limit()
        except ValueError:
            pass

    def create_enemy_data(self):
        try:
            num = int(self.ui.lineEdit_5.text())
            self.Enemy_Data = [[] for _ in range(num)]
            self.update_spinbox_limit()
        except ValueError:
            pass

    def update_spinbox_limit(self):
        current_text = self.ui.comboBox_2.currentText()
        if current_text == "PL":
            self.ui.spinBox.setMaximum(len(self.PL_Data))
            self.ui.label_8.show()
            self.ui.lineEdit_11.show()
        else:
            self.ui.spinBox.setMaximum(len(self.Enemy_Data))
            self.ui.label_8.hide()
            self.ui.lineEdit_11.hide()
        # Ensure SpinBox value is within the new range
        self.ui.spinBox.setValue(min(self.ui.spinBox.maximum(), self.ui.spinBox.value()))
        self.update_line_edits()

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

    def sort_and_display_third_element(self):
        combined_data = [(lst[0], lst[2]) for lst in self.PL_Data + self.Enemy_Data if len(lst) > 2]
        sorted_data = sorted(combined_data, key=lambda x: x[1], reverse=True)

        self.ui.textBrowser_3.clear()
        for first, third in sorted_data:
            self.ui.textBrowser_3.append(f"{first}: {third}")

    def export_to_json(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Data", "", "JSON Files (*.json);;All Files (*)", options=options)
        if file_name:
            data = {
                "PL_Data": self.PL_Data,
                "Enemy_Data": self.Enemy_Data
            }
            try:
                with open(file_name, 'w') as json_file:
                    json.dump(data, json_file)
                QMessageBox.information(self, "Success", "Data successfully exported.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to export data: {e}")

    def import_from_json(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Import Data", "", "JSON Files (*.json);;All Files (*)", options=options)
        if file_name:
            try:
                with open(file_name, 'r') as json_file:
                    data = json.load(json_file)
                self.PL_Data = data.get("PL_Data", [])
                self.Enemy_Data = data.get("Enemy_Data", [])
                self.ui.lineEdit_4.setText(str(len(self.PL_Data)))
                self.ui.lineEdit_5.setText(str(len(self.Enemy_Data)))
                self.update_ui()
                QMessageBox.information(self, "Success", "Data successfully imported.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to import data: {e}")

    def update_line_edits(self):
        index = self.ui.spinBox.value() - 1
        if self.ui.comboBox_2.currentText() == "PL":
            if 0 <= index < len(self.PL_Data):
                data = self.PL_Data[index]
                for i, le in enumerate(self.line_edits):
                    le.setText(data[i] if i < len(data) else "")
            else:
                for le in self.line_edits:
                    le.clear()
        else:
            if 0 <= index < len(self.Enemy_Data):
                data = self.Enemy_Data[index]
                for i, le in self.line_edits[:5]:
                    le.setText(data[i] if i < len(data) else "")
                self.ui.lineEdit_11.setText(data[5] if len(data) > 5 else "")
            else:
                for le in self.line_edits[:5]:
                    le.clear()
                self.ui.lineEdit_11.clear()

    def update_ui(self):
        self.update_spinbox_limit()
        self.update_text_browser(self.ui.textBrowser, self.PL_Data, "PL_Data")
        self.update_text_browser(self.ui.textBrowser_13, self.Enemy_Data, "Enemy_Data")

    def validate_lineEdit_3(self):
        input_text = self.ui.lineEdit_3.text()
        is_valid = any(input_text == data[0] for data in self.PL_Data + self.Enemy_Data)
        if not is_valid:
            QMessageBox.warning(self, "Invalid Input", "lineEdit_3 input is not in any list. Please re-enter.")
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_3.setFocus()

        # Check if input_text is in PL_Data and show/hide CheckBox accordingly
        in_pl_data = any(input_text == data[0] for data in self.PL_Data)
        self.ui.checkBox.setChecked(in_pl_data)
        self.ui.checkBox.setVisible(in_pl_data)

    def validate_lineEdit_2(self):
        input_text = self.ui.lineEdit_2.text()
        is_valid = any(input_text == data[0] for data in self.PL_Data + self.Enemy_Data)
        if not is_valid:
            QMessageBox.warning(self, "Invalid Input", "lineEdit_2 input is not in any list. Please re-enter.")
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_2.setFocus()

    def calculate_damage(self):
        attacker = self.ui.lineEdit_3.text()
        target = self.ui.lineEdit_2.text()
        sp_cost = 0

        try:
            sp_cost = float(self.ui.lineEdit.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid SP input.")
            return

        attacker_list = None
        target_list = None

        # Find attacker and target lists
        for lst in self.PL_Data + self.Enemy_Data:
            if lst and lst[0] == attacker:
                attacker_list = lst
            if lst and lst[0] == target:
                target_list = lst

        if not attacker_list or not target_list:
            QMessageBox.warning(self, "Error", "Attacker or Target not found in lists.")
            return

        if float(attacker_list[5]) < sp_cost:
            QMessageBox.warning(self, "Error", "SP不足")
            return

        attacker_list[5] = str(float(attacker_list[5]) - sp_cost)

        try:
            damage_factor = float(self.ui.lineEdit_12.text())
            damage_multiplier = float(self.ui.lineEdit_13.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid damage factor or multiplier.")
            return

        attack_type = self.ui.comboBox.currentText()
        temp_damage = 0.0

        if attack_type == "物理":
            temp_damage = max(0, damage_factor * damage_multiplier - float(target_list[3]))
        elif attack_type == "法术":
            temp_damage = max(0, damage_factor * damage_multiplier - float(target_list[4]))
        elif attack_type == "真伤":
            temp_damage = damage_factor * damage_multiplier

        initial_hp = float(target_list[1])
        target_list[1] = str(max(0, initial_hp - temp_damage))

        additional_damage = 0.0
        try:
            additional_damage = float(self.ui.lineEdit_14.text())
        except ValueError:
            pass

        final_hp = float(target_list[1])
        if final_hp > 0:
            final_hp = max(0, final_hp - additional_damage)
            if final_hp <= 0:
                self.ui.textBrowser_4.append(f"{target}被追加伤害击倒了。")

        target_list[1] = str(final_hp)

        if final_hp <= 0:
            QMessageBox.information(self, "Info", f"{target}遭受了来自{attacker}的伤害并倒地了。")

        combined_damage = temp_damage + (additional_damage if final_hp > 0 else 0)

        self.ui.textBrowser_4.append(f"{attacker}对{target}造成了{temp_damage}点{attack_type}伤害并消耗了{sp_cost}SP，{target}还剩{target_list[1]}点HP，{attacker}还剩{attacker_list[5]}点SP")
        if additional_damage > 0:
            self.ui.textBrowser_4.append(f"{attacker}对{target}造成了额外的{additional_damage}点伤害")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
