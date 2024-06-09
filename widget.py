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
        self.setWindowTitle("行于泰拉规则书战斗计算器（适配0.21和0.3）")  # 设置窗口标题
        self.PL_Data = []
        self.Enemy_Data = []

        # 将SpinBox最小值设置为1
        self.ui.spinBox.setMinimum(1)

        # 连接信号和槽
        self.ui.lineEdit_4.editingFinished.connect(self.create_pl_data)
        self.ui.lineEdit_5.editingFinished.connect(self.create_enemy_data)
        self.ui.comboBox_2.currentTextChanged.connect(self.update_spinbox_limit)
        self.ui.spinBox.valueChanged.connect(self.update_line_edits)
        self.ui.pushButton_4.clicked.connect(self.sort_and_display_third_element)
        self.ui.pushButton_3.clicked.connect(self.export_to_json)
        self.ui.pushButton_2.clicked.connect(self.import_from_json)

        self.line_edits = [self.ui.lineEdit_6, self.ui.lineEdit_7, self.ui.lineEdit_8, self.ui.lineEdit_9,
                           self.ui.lineEdit_10, self.ui.lineEdit_11]
        for line_edit in self.line_edits:
            line_edit.editingFinished.connect(self.update_data)

        self.ui.lineEdit_3.editingFinished.connect(self.validate_lineEdit_3)
        self.ui.lineEdit_2.editingFinished.connect(self.validate_lineEdit_2)
        self.ui.pushButton_13.clicked.connect(self.calculate_damage)
        self.ui.pushButton_13.clicked.connect(self.refresh_all_data)

        # 设置布局，使TabWidget随窗口大小变化
        layout = QVBoxLayout(self)
        layout.addWidget(self.ui.tabWidget)
        self.setLayout(layout)

        # 确保TabWidget按比例调整大小
        self.ui.tabWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 初始化UI
        self.update_ui()

    def create_pl_data(self):
        """根据lineEdit_4的输入创建PL_Data列表"""
        try:
            num = int(self.ui.lineEdit_4.text())
            self.PL_Data = [[] for _ in range(num)]
            self.update_spinbox_limit()
        except ValueError:
            pass

    def create_enemy_data(self):
        """根据lineEdit_5的输入创建Enemy_Data列表"""
        try:
            num = int(self.ui.lineEdit_5.text())
            self.Enemy_Data = [[] for _ in range(num)]
            self.update_spinbox_limit()
        except ValueError:
            pass

    def update_spinbox_limit(self):
        """根据ComboBox_2的选择更新SpinBox的上限"""
        current_text = self.ui.comboBox_2.currentText()
        if current_text == "PL":
            self.ui.spinBox.setMaximum(len(self.PL_Data))
            self.ui.label_8.show()
            self.ui.lineEdit_11.show()
        else:
            self.ui.spinBox.setMaximum(len(self.Enemy_Data))
            self.ui.label_8.hide()
            self.ui.lineEdit_11.hide()
        # 确保SpinBox的值在新的范围内
        self.ui.spinBox.setValue(min(self.ui.spinBox.maximum(), self.ui.spinBox.value()))
        self.update_line_edits()

    def update_data(self):
        """更新PL_Data或Enemy_Data中的数据"""
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
        """更新TextBrowser中的内容"""
        text_browser.clear()
        for i, data in enumerate(data_list):
            if data:
                text_browser.append(f"{prefix}_{i + 1}: {', '.join(data)}")

    def sort_and_display_third_element(self):
        """排序并显示所有列表的第三个元素"""
        combined_data = []

        # 合并PL_Data和Enemy_Data，并确保有第三个元素的存在
        for i, lst in enumerate(self.PL_Data):
            if len(lst) > 2:
                combined_data.append((lst[0], float(lst[2])))

        for i, lst in enumerate(self.Enemy_Data):
            if len(lst) > 2:
                combined_data.append((lst[0], float(lst[2])))

        # 排序
        sorted_data = sorted(combined_data, key=lambda x: x[1], reverse=True)

        # 在textBrowser_3中显示排序后的数据
        self.ui.textBrowser_3.clear()
        for first, third in sorted_data:
            self.ui.textBrowser_3.append(f"{first}: {third}")

    def export_to_json(self):
        """导出数据到JSON文件"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Data", "", "JSON Files (*.json);;All Files (*)",
                                                   options=options)
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
        """从JSON文件导入数据"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Import Data", "", "JSON Files (*.json);;All Files (*)",
                                                   options=options)
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
        """更新LineEdits中的数据"""
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
                for i, le in enumerate(self.line_edits[:5]):
                    le.setText(data[i] if i < len(data) else "")
                self.ui.lineEdit_11.setText(data[5] if len(data) > 5 else "")
            else:
                for le in self.line_edits[:5]:
                    le.clear()
                self.ui.lineEdit_11.clear()

    def update_ui(self):
        """更新UI"""
        self.update_spinbox_limit()
        self.update_text_browser(self.ui.textBrowser, self.PL_Data, "PL_Data")
        self.update_text_browser(self.ui.textBrowser_13, self.Enemy_Data, "Enemy_Data")
        self.refresh_all_data()

    def validate_lineEdit_3(self):
        """验证lineEdit_3中的输入"""
        input_text = self.ui.lineEdit_3.text()
        is_valid = any(input_text == data[0] for data in self.PL_Data + self.Enemy_Data)
        if not is_valid:
            QMessageBox.warning(self, "Invalid Input", "lineEdit_3 input is not in any list. Please re-enter.")
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_3.setFocus()

        # 检查input_text是否在PL_Data中，并相应地显示或隐藏CheckBox
        in_pl_data = any(input_text == data[0] for data in self.PL_Data)
        self.ui.checkBox.setChecked(in_pl_data)
        self.ui.checkBox.setVisible(in_pl_data)

    def validate_lineEdit_2(self):
        """验证lineEdit_2中的输入"""
        input_text = self.ui.lineEdit_2.text()
        is_valid = any(input_text == data[0] for data in self.PL_Data + self.Enemy_Data)
        if not is_valid:
            QMessageBox.warning(self, "Invalid Input", "lineEdit_2 input is not in any list. Please re-enter.")
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_2.setFocus()

    def calculate_damage(self):
        """计算伤害并更新相应列表数据"""
        attacker = self.ui.lineEdit_3.text()
        target = self.ui.lineEdit_2.text()
        try:
            sp_cost = float(self.ui.lineEdit.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid SP cost.")
            return

        attacker_list = None
        target_list = None

        for data in self.PL_Data + self.Enemy_Data:
            if data and data[0] == attacker:
                attacker_list = data
            if data and data[0] == target:
                target_list = data

        if not attacker_list or not target_list:
            QMessageBox.warning(self, "Error", "Invalid attacker or target.")
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

        self.ui.textBrowser_4.append(
            f"{attacker}对{target}造成了{temp_damage}点{attack_type}伤害并消耗了{sp_cost}SP，{target}还剩{target_list[1]}点HP，{attacker}还剩{attacker_list[5]}点SP")
        if additional_damage > 0 and final_hp > 0:
            self.ui.textBrowser_4.append(f"{attacker}对{target}造成了额外的{additional_damage}点伤害")

        self.refresh_all_data()

    def refresh_all_data(self):
        """刷新所有列表数据并在TextBrowser_5中显示"""
        self.ui.textBrowser_5.clear()
        for i, data in enumerate(self.PL_Data):
            if data:
                self.ui.textBrowser_5.append(f"{data[0]}：HP {data[1]}，SP {data[5]}")
        for i, data in enumerate(self.Enemy_Data):
            if data:
                self.ui.textBrowser_5.append(f"{data[0]}：HP {data[1]}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
