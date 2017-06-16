import logging
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView, QHeaderView

from sportorg.app.models.memory_model import PersonProxyModel, CourseMemoryModel


class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setAcceptDrops(False)
        self.setToolTip("")
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setAutoFillBackground(False)
        self.course_layout = QtWidgets.QGridLayout(self)
        self.course_layout.setObjectName("course_layout")

        self.CourseTable = QtWidgets.QTableView(self)
        self.CourseTable.setObjectName("CourseTable")
        proxy_model = PersonProxyModel(self)
        proxy_model.setSourceModel(CourseMemoryModel())
        self.CourseTable.setModel(proxy_model)
        self.CourseTable.setSortingEnabled(True)
        self.CourseTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        hor_header = self.CourseTable.horizontalHeader()
        assert (isinstance(hor_header, QHeaderView))
        hor_header.setSectionsMovable(True)
        hor_header.setDropIndicatorShown(True)
        hor_header.setSectionResizeMode(QHeaderView.ResizeToContents)

        def course_double_clicked(index):
            print('clicked on ' + str(index.row()))
            logging.info('clicked on ' + str(index.row()))

        self.CourseTable.doubleClicked.connect(course_double_clicked)
        self.course_layout.addWidget(self.CourseTable)

    def get_table(self):
        return self.CourseTable