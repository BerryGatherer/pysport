# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_bulk_edit.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication


class Ui_bulk_edit(object):
    def setupUi(self, bulk_edit):
        bulk_edit.setObjectName("bulk_edit")
        bulk_edit.setWindowModality(QtCore.Qt.WindowModal)
        bulk_edit.resize(288, 327)
        bulk_edit.setSizeGripEnabled(False)
        bulk_edit.setModal(True)
        self.button_box = QtWidgets.QDialogButtonBox(bulk_edit)
        self.button_box.setGeometry(QtCore.QRect(-100, 290, 318, 23))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.participants_grou_box = QtWidgets.QGroupBox(bulk_edit)
        self.participants_grou_box.setGeometry(QtCore.QRect(20, 0, 141, 75))
        self.participants_grou_box.setObjectName("participants_grou_box")
        self.widget = QtWidgets.QWidget(self.participants_grou_box)
        self.widget.setGeometry(QtCore.QRect(10, 23, 89, 42))
        self.widget.setObjectName("widget")
        self.participants_layout = QtWidgets.QVBoxLayout(self.widget)
        self.participants_layout.setContentsMargins(0, 0, 0, 0)
        self.participants_layout.setObjectName("participants_layout")
        self.all_radio_button = QtWidgets.QRadioButton(self.widget)
        self.all_radio_button.setChecked(True)
        self.all_radio_button.setObjectName("all_radio_button")
        self.participants_layout.addWidget(self.all_radio_button)
        self.selected_radio_button = QtWidgets.QRadioButton(self.widget)
        self.selected_radio_button.setObjectName("selected_radio_button")
        self.participants_layout.addWidget(self.selected_radio_button)
        self.widget1 = QtWidgets.QWidget(bulk_edit)
        self.widget1.setGeometry(QtCore.QRect(20, 80, 248, 197))
        self.widget1.setObjectName("widget1")
        self.properties_layout = QtWidgets.QGridLayout(self.widget1)
        self.properties_layout.setContentsMargins(0, 0, 0, 0)
        self.properties_layout.setObjectName("properties_layout")
        self.group_check_box = QtWidgets.QCheckBox(self.widget1)
        self.group_check_box.setObjectName("group_check_box")
        self.properties_layout.addWidget(self.group_check_box, 0, 0, 1, 1)
        self.group_combo_box = QtWidgets.QComboBox(self.widget1)
        self.group_combo_box.setObjectName("group_combo_box")
        self.properties_layout.addWidget(self.group_combo_box, 0, 1, 1, 3)
        self.team_check_box = QtWidgets.QCheckBox(self.widget1)
        self.team_check_box.setObjectName("team_check_box")
        self.properties_layout.addWidget(self.team_check_box, 1, 0, 1, 1)
        self.team_combo_box = QtWidgets.QComboBox(self.widget1)
        self.team_combo_box.setObjectName("team_combo_box")
        self.properties_layout.addWidget(self.team_combo_box, 1, 1, 1, 3)
        self.start_check_box = QtWidgets.QCheckBox(self.widget1)
        self.start_check_box.setObjectName("start_check_box")
        self.properties_layout.addWidget(self.start_check_box, 2, 0, 1, 2)
        self.start_time_edit = QtWidgets.QTimeEdit(self.widget1)
        self.start_time_edit.setObjectName("start_time_edit")
        self.properties_layout.addWidget(self.start_time_edit, 2, 2, 1, 2)
        self.start_group_check_box = QtWidgets.QCheckBox(self.widget1)
        self.start_group_check_box.setObjectName("start_group_check_box")
        self.properties_layout.addWidget(self.start_group_check_box, 3, 0, 1, 3)
        self.start_group_spin_box = QtWidgets.QSpinBox(self.widget1)
        self.start_group_spin_box.setObjectName("start_group_spin_box")
        self.properties_layout.addWidget(self.start_group_spin_box, 3, 3, 1, 1)
        self.comment_check_box = QtWidgets.QCheckBox(self.widget1)
        self.comment_check_box.setObjectName("comment_check_box")
        self.properties_layout.addWidget(self.comment_check_box, 4, 0, 1, 2)
        self.comment_edit = QtWidgets.QLineEdit(self.widget1)
        self.comment_edit.setObjectName("comment_edit")
        self.properties_layout.addWidget(self.comment_edit, 4, 2, 1, 2)
        self.status_check_box = QtWidgets.QCheckBox(self.widget1)
        self.status_check_box.setObjectName("status_check_box")
        self.properties_layout.addWidget(self.status_check_box, 5, 0, 1, 1)
        self.status_layout = QtWidgets.QVBoxLayout()
        self.status_layout.setObjectName("status_layout")
        self.not_classified_check_box = QtWidgets.QCheckBox(self.widget1)
        self.not_classified_check_box.setEnabled(False)
        self.not_classified_check_box.setObjectName("not_classified_check_box")
        self.status_layout.addWidget(self.not_classified_check_box)
        self.without_team_check_box = QtWidgets.QCheckBox(self.widget1)
        self.without_team_check_box.setEnabled(False)
        self.without_team_check_box.setObjectName("without_team_check_box")
        self.status_layout.addWidget(self.without_team_check_box)
        self.chip_rented_check_box = QtWidgets.QCheckBox(self.widget1)
        self.chip_rented_check_box.setEnabled(False)
        self.chip_rented_check_box.setObjectName("chip_rented_check_box")
        self.status_layout.addWidget(self.chip_rented_check_box)
        self.properties_layout.addLayout(self.status_layout, 5, 1, 1, 3)

        self.retranslateUi(bulk_edit)
        self.button_box.accepted.connect(bulk_edit.accept)
        self.button_box.rejected.connect(bulk_edit.reject)
        QtCore.QMetaObject.connectSlotsByName(bulk_edit)

    def retranslateUi(self, bulk_edit):
        _translate = QtCore.QCoreApplication.translate
        bulk_edit.setWindowTitle(_translate("bulk_edit", "Dialog"))
        self.participants_grou_box.setTitle(_translate("bulk_edit", "Participants to modify"))
        self.all_radio_button.setText(_translate("bulk_edit", "All filtered"))
        self.selected_radio_button.setText(_translate("bulk_edit", "Selected only"))
        self.group_check_box.setText(_translate("bulk_edit", "Change group"))
        self.team_check_box.setText(_translate("bulk_edit", "Change team"))
        self.start_check_box.setText(_translate("bulk_edit", "change start time"))
        self.start_time_edit.setDisplayFormat(_translate("bulk_edit", "HH:mm:ss"))
        self.start_group_check_box.setText(_translate("bulk_edit", "change start group"))
        self.comment_check_box.setText(_translate("bulk_edit", "change comment"))
        self.status_check_box.setText(_translate("bulk_edit", "change status"))
        self.not_classified_check_box.setText(_translate("bulk_edit", "not classified"))
        self.without_team_check_box.setText(_translate("bulk_edit", "without a team"))
        self.chip_rented_check_box.setText(_translate("bulk_edit", "chip rented"))

def main(argv):
    app = QApplication(argv)
    mw = QDialog()
    obj = Ui_bulk_edit()
    obj.setupUi(mw)
    mw.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main(sys.argv)