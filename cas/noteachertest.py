from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from noteacher import Ui_noteacher


class Noteacher(QtWidgets.QWidget, Ui_noteacher):
    def __init__(self, db,parent=None):
        super(Noteacher, self).__init__(parent)
        self.setupUi(self)
        self.db = db  # pymysql.connect("localhost", "root", "123456", "course-arrangement system")

        # 创建QStandardItemModel
        self.model = QStandardItemModel(self)
        self.model2 = QStandardItemModel(self)

        # 将模型设置到视图中
        self.tableView.setModel(self.model)
        self.tableView_2.setModel(self.model2)

        # 查询数据并更新视图
        self.updateTableView("teacher", self.model)
        self.updateTableView("teacher_unavailable_periods", self.model2)

        # 选中的老师名字
        self.selected_teacher = ""

        # 绑定tableView选中事件
        self.tableView.selectionModel().selectionChanged.connect(self.handleSelectionChanged)

        # 绑定按钮点击事件
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)

    def updateTableView(self, table_name, model):
        # 执行查询
        cursor = self.db.cursor()
        if table_name == "teacher":
            query = "SELECT name, sum FROM teacher"
        elif table_name == "teacher_unavailable_periods":
            query = '''
            SELECT Teacher.name, teacher_unavailable_periods.class_num + 1
            FROM teacher_unavailable_periods
            INNER JOIN Teacher ON teacher_unavailable_periods.teacher_id = Teacher.id
            '''
        else:
            raise ValueError(f"Unsupported table name: {table_name}")

        cursor.execute(query)

        # 清除旧的数据
        model.removeRows(0, model.rowCount())

        # 获取并设置新的数据
        for row_data in cursor:
            row = []
            for item in row_data:
                cell = QStandardItem(str(item))
                row.append(cell)
            model.appendRow(row)

    def handleSelectionChanged(self, selected, deselected):
        # 获取选中的老师名字
        indexes = self.tableView.selectionModel().selectedRows()
        for index in indexes:
            self.selected_teacher = self.model.item(index.row(), 0).text()

    def add(self):
        # 获取checkbox的状态
        checkbox_states = [
            self.checkBox.isChecked(),
            self.checkBox_2.isChecked(),
            self.checkBox_3.isChecked(),
            self.checkBox_4.isChecked(),
            self.checkBox_5.isChecked(),
            self.checkBox_6.isChecked(),
        ]

        # 查询老师的id
        cursor = self.db.cursor()
        cursor.execute(f"SELECT id FROM teacher WHERE name='{self.selected_teacher}'")
        teacher_id = cursor.fetchone()[0]

        # 向teacher_unavailable_periods表中插入数据
        for i, state in enumerate(checkbox_states):
            if state:
                cursor.execute(f"INSERT INTO teacher_unavailable_periods (teacher_id, class_num) VALUES ({teacher_id}, {i})")

        # 提交事务
        self.db.commit()

        # 更新视图
        self.updateTableView("teacher_unavailable_periods", self.model2)

    def delete(self):
        # 获取tableview_2当前选中行
        current_row = self.tableView_2.currentIndex().row()

        if current_row >= 0:
            # 获取选中行的老师姓名和课程数
            cursor = self.db.cursor()
            teacher_name = self.model2.item(current_row, 0).text()
            class_num = int(self.model2.item(current_row, 1).text()) - 1

            # 在teacher表中搜索该名字对应的id
            cursor.execute(f"SELECT id FROM teacher WHERE name='{teacher_name}'")
            teacher_id = cursor.fetchone()[0]  # 假设name在Teacher表中是唯一的

            # 从teacher_unavailable_periods表中删除记录，并更新tableview_2
            try:
                cursor.execute(
                    f"DELETE FROM teacher_unavailable_periods WHERE teacher_id = {teacher_id} AND class_num = {class_num}")
                self.db.commit()
                self.updateTableView("teacher_unavailable_periods", self.model2)
            except Exception as e:
                print(f"Error occurred: {e}")


