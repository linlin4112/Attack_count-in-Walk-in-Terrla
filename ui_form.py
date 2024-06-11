# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 811, 601))
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget.setStyleSheet(u"background-image: url(\".\\background.png\");\n"
"background-repeat: no-repeat;  \n"
"background-position: center;\n"
"background-attachment: fixed;\n"
"background-size: cover;")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_9 = QLabel(self.tab_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(470, 70, 121, 19))
        self.pushButton = QPushButton(self.tab_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 460, 92, 28))
        self.pushButton_3 = QPushButton(self.tab_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(200, 460, 111, 24))
        self.label_10 = QLabel(self.tab_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(640, 70, 31, 16))
        self.label_11 = QLabel(self.tab_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(730, 70, 54, 16))
        self.spinBox = QSpinBox(self.tab_3)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(580, 60, 50, 28))
        self.spinBox.setMinimum(1)
        self.comboBox_2 = QComboBox(self.tab_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(660, 60, 71, 27))
        self.pushButton_2 = QPushButton(self.tab_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(340, 460, 92, 28))
        self.layoutWidget = QWidget(self.tab_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 80, 431, 331))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_9 = QLineEdit(self.layoutWidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_2.addWidget(self.lineEdit_9, 4, 3, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 2, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 5, 2, 1, 1)

        self.lineEdit_5 = QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_2.addWidget(self.lineEdit_5, 1, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 6, 2, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 3, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_2.addWidget(self.lineEdit_4, 0, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 4, 2, 1, 1)

        self.lineEdit_6 = QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_2.addWidget(self.lineEdit_6, 0, 3, 1, 1)

        self.lineEdit_11 = QLineEdit(self.layoutWidget)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_2.addWidget(self.lineEdit_11, 6, 3, 1, 1)

        self.lineEdit_10 = QLineEdit(self.layoutWidget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_2.addWidget(self.lineEdit_10, 5, 3, 1, 1)

        self.lineEdit_8 = QLineEdit(self.layoutWidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_2.addWidget(self.lineEdit_8, 3, 3, 1, 1)

        self.lineEdit_7 = QLineEdit(self.layoutWidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_2.addWidget(self.lineEdit_7, 1, 3, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.layoutWidget1 = QWidget(self.tab_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(480, 100, 258, 220))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_64 = QLabel(self.layoutWidget1)
        self.label_64.setObjectName(u"label_64")

        self.verticalLayout_7.addWidget(self.label_64)

        self.textBrowser = QTextBrowser(self.layoutWidget1)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_7.addWidget(self.textBrowser)

        self.layoutWidget2 = QWidget(self.tab_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(480, 340, 258, 220))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.layoutWidget2)
        self.label_65.setObjectName(u"label_65")

        self.verticalLayout_8.addWidget(self.label_65)

        self.textBrowser_13 = QTextBrowser(self.layoutWidget2)
        self.textBrowser_13.setObjectName(u"textBrowser_13")

        self.verticalLayout_8.addWidget(self.textBrowser_13)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(90, 340, 111, 31))
        self.layoutWidget3 = QWidget(self.tab)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 60, 258, 220))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.layoutWidget3)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_3.addWidget(self.label_12)

        self.textBrowser_3 = QTextBrowser(self.layoutWidget3)
        self.textBrowser_3.setObjectName(u"textBrowser_3")

        self.verticalLayout_3.addWidget(self.textBrowser_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.pushButton_13 = QPushButton(self.tab_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(110, 490, 92, 28))
        self.layoutWidget4 = QWidget(self.tab_2)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(40, 60, 241, 411))
        self.gridLayout = QGridLayout(self.layoutWidget4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.layoutWidget4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 0, 1, 1, 1)

        self.lineEdit_12 = QLineEdit(self.layoutWidget4)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout.addWidget(self.lineEdit_12, 6, 1, 1, 1)

        self.lineEdit_13 = QLineEdit(self.layoutWidget4)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout.addWidget(self.lineEdit_13, 7, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.layoutWidget4)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.gridLayout.addWidget(self.checkBox_2, 9, 0, 1, 2)

        self.checkBox = QCheckBox(self.layoutWidget4)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(True)
        self.checkBox.setChecked(True)

        self.gridLayout.addWidget(self.checkBox, 3, 0, 1, 2)

        self.label_17 = QLabel(self.layoutWidget4)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 6, 0, 1, 1)

        self.lineEdit = QLineEdit(self.layoutWidget4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setInputMethodHints(Qt.ImhNone)

        self.gridLayout.addWidget(self.lineEdit, 4, 1, 1, 1)

        self.label_13 = QLabel(self.layoutWidget4)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)

        self.lineEdit_14 = QLineEdit(self.layoutWidget4)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        font = QFont()
        font.setBold(False)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit_14.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_14.setInputMethodHints(Qt.ImhNone)
        self.lineEdit_14.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.gridLayout.addWidget(self.lineEdit_14, 10, 1, 1, 1)

        self.label_19 = QLabel(self.layoutWidget4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777210, 16777215))
        self.label_19.setInputMethodHints(Qt.ImhNone)

        self.gridLayout.addWidget(self.label_19, 10, 0, 1, 1)

        self.label_14 = QLabel(self.layoutWidget4)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.layoutWidget4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_18 = QLabel(self.layoutWidget4)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 7, 0, 1, 1)

        self.label_15 = QLabel(self.layoutWidget4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setEnabled(True)
        self.label_15.setInputMethodHints(Qt.ImhNone)

        self.gridLayout.addWidget(self.label_15, 4, 0, 1, 1)

        self.label_16 = QLabel(self.layoutWidget4)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 2, 0, 1, 1)

        self.comboBox = QComboBox(self.layoutWidget4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)

        self.layoutWidget5 = QWidget(self.tab_2)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(330, 300, 258, 220))
        self.verticalLayout = QVBoxLayout(self.layoutWidget5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.layoutWidget5)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout.addWidget(self.label_21)

        self.textBrowser_5 = QTextBrowser(self.layoutWidget5)
        self.textBrowser_5.setObjectName(u"textBrowser_5")

        self.verticalLayout.addWidget(self.textBrowser_5)

        self.layoutWidget6 = QWidget(self.tab_2)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(330, 20, 258, 220))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.layoutWidget6)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_2.addWidget(self.label_20)

        self.textBrowser_4 = QTextBrowser(self.layoutWidget6)
        self.textBrowser_4.setObjectName(u"textBrowser_4")

        self.verticalLayout_2.addWidget(self.textBrowser_4)

        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Widget)
        self.checkBox.toggled.connect(self.label_15.setVisible)
        self.checkBox_2.clicked["bool"].connect(self.label_19.setVisible)
        self.checkBox_2.clicked["bool"].connect(self.lineEdit_14.setVisible)
        self.checkBox.toggled.connect(self.lineEdit.setVisible)
        self.pushButton.clicked["bool"].connect(self.spinBox.stepUp)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
#if QT_CONFIG(whatsthis)
        self.tabWidget.setWhatsThis(QCoreApplication.translate("Widget", u"<html><head/><body><p>\u5bfc\u5165\u6570\u636e</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_9.setText(QCoreApplication.translate("Widget", u"\u73b0\u5728\u4f60\u6b63\u5728\u7f16\u8f91\uff1a\u7b2c", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u4e0b\u4e00\u4e2a\u6570\u636e", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"\u4fdd\u5b58\u6570\u636e", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"\u540d", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"\u6570\u636e", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Widget", u"PL", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Widget", u"\u654c\u4eba", None))

        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"\u8bfb\u53d6\u6570\u636e", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u8840\u91cf", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"\u6cd5\u6297", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u654c\u4eba\u6570\u91cf", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"SP\uff08PL\u7279\u6709\u6570\u636e\uff09", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u540d\u5b57", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u901f\u5ea6/\u5148\u653b", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"\u7269\u6297", None))
        self.label.setText(QCoreApplication.translate("Widget", u"PL\u6570\u91cf", None))
        self.label_64.setText(QCoreApplication.translate("Widget", u"PL\u6570\u636e\uff1a", None))
        self.label_65.setText(QCoreApplication.translate("Widget", u"\u654c\u4eba\u6570\u636e\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Widget", u"\u5bfc\u5165\u6570\u636e", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"\u8ba1\u7b97\u914d\u901f\u5217\u8868", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"\u914d\u901f\u7ed3\u679c\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"\u901f\u5ea6\u6392\u8868", None))
        self.pushButton_13.setText(QCoreApplication.translate("Widget", u"\u5f00\u59cb\u8ba1\u7b97", None))
        self.checkBox_2.setText(QCoreApplication.translate("Widget", u"\u9020\u6210\u8ffd\u52a0\u653b\u51fb", None))
        self.checkBox.setText(QCoreApplication.translate("Widget", u"\u672c\u6b21\u653b\u51fb\u6d88\u8017SP", None))
        self.label_17.setText(QCoreApplication.translate("Widget", u"\u9020\u6210\u4f24\u5bb3\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"\u653b\u51fb\u8005\u540d\u5b57\uff1a", None))
        self.label_19.setText(QCoreApplication.translate("Widget", u"\u8ffd\u52a0\u653b\u51fb\u4f24\u5bb3\uff1a", None))
        self.label_14.setText(QCoreApplication.translate("Widget", u"\u53d7\u51fb\u8005\u540d\u5b57\uff1a", None))
        self.label_18.setText(QCoreApplication.translate("Widget", u"\u4f24\u5bb3\u500d\u7387\uff1a", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"\u6d88\u8017SP\uff1a", None))
        self.label_16.setText(QCoreApplication.translate("Widget", u"\u4f24\u5bb3\u7c7b\u578b\uff1a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Widget", u"\u7269\u7406", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Widget", u"\u6cd5\u672f", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Widget", u"\u771f\u4f24", None))

        self.label_21.setText(QCoreApplication.translate("Widget", u"\u72b6\u6001\u4e00\u89c8\uff1a", None))
        self.label_20.setText(QCoreApplication.translate("Widget", u"\u6218\u6597\u65e5\u5fd7\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"\u6218\u6597\u8ba1\u7b97", None))
    # retranslateUi

