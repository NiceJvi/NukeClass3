# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\develop\tdclass\batch_transcoder\frontend\mvc\main_ui.ui'
#
# Created: Fri Jun  5 19:51:11 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_BatchTranscoder(object):
    def setupUi(self, BatchTranscoder):
        BatchTranscoder.setObjectName("BatchTranscoder")
        BatchTranscoder.resize(1108, 635)
        self.verticalLayoutWidget = QtGui.QWidget(BatchTranscoder)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1091, 611))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.show_list = QtGui.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_list.sizePolicy().hasHeightForWidth())
        self.show_list.setSizePolicy(sizePolicy)
        self.show_list.setObjectName("show_list")
        self.horizontalLayout_2.addWidget(self.show_list)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.preset_list = QtGui.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_list.sizePolicy().hasHeightForWidth())
        self.preset_list.setSizePolicy(sizePolicy)
        self.preset_list.setObjectName("preset_list")
        self.horizontalLayout_2.addWidget(self.preset_list)
        self.add_source_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.add_source_button.setObjectName("add_source_button")
        self.horizontalLayout_2.addWidget(self.add_source_button)
        self.run_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.run_button.setObjectName("run_button")
        self.horizontalLayout_2.addWidget(self.run_button)
        self.clear_button = QtGui.QPushButton(self.verticalLayoutWidget)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_2.addWidget(self.clear_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = QtGui.QScrollArea(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(550, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaContentsWidget = QtGui.QWidget()
        self.scrollAreaContentsWidget.setGeometry(QtCore.QRect(0, 0, 548, 574))
        self.scrollAreaContentsWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaContentsWidget.setObjectName("scrollAreaContentsWidget")
        self.scrollArea.setWidget(self.scrollAreaContentsWidget)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.information_group = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.information_group.setObjectName("information_group")
        self.information_table = QtGui.QTableView(self.information_group)
        self.information_table.setGeometry(QtCore.QRect(20, 20, 501, 251))
        self.information_table.setObjectName("information_table")
        self.verticalLayout_3.addWidget(self.information_group)
        self.parameter_group = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.parameter_group.setObjectName("parameter_group")
        self.verticalLayout_3.addWidget(self.parameter_group)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(BatchTranscoder)
        QtCore.QMetaObject.connectSlotsByName(BatchTranscoder)

    def retranslateUi(self, BatchTranscoder):
        BatchTranscoder.setWindowTitle(QtGui.QApplication.translate("BatchTranscoder", "Batch Transcoder", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("BatchTranscoder", "Show:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("BatchTranscoder", "Preset:", None, QtGui.QApplication.UnicodeUTF8))
        self.add_source_button.setText(QtGui.QApplication.translate("BatchTranscoder", "Add Source", None, QtGui.QApplication.UnicodeUTF8))
        self.run_button.setText(QtGui.QApplication.translate("BatchTranscoder", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_button.setText(QtGui.QApplication.translate("BatchTranscoder", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.information_group.setTitle(QtGui.QApplication.translate("BatchTranscoder", "Information", None, QtGui.QApplication.UnicodeUTF8))
        self.parameter_group.setTitle(QtGui.QApplication.translate("BatchTranscoder", "Additional Parameters", None, QtGui.QApplication.UnicodeUTF8))

