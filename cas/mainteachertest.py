
from mainteacher import Ui_mainteacher
import sys
from PyQt5 import QtWidgets, QtCore
import pymysql
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from teacherselecttest import TeacherSelect


class MainTeacher(QtWidgets.QMainWindow, Ui_mainteacher):
    def __init__(self, parent=None):
        super(MainTeacher, self).__init__(parent)
        self.setupUi(self)
        # 创建数据库连接
        self.db = pymysql.connect(host='localhost', user='root', password='wwdcyy', database='course-arrangement system')

        # 创建QStandardItemModel
        self.model = QStandardItemModel(self)

        # 将模型设置到视图中
        self.tableView.setModel(self.model)

        # 查询数据并更新视图
        self.updateTableView("teacher")

        # 绑定按钮点击事件
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)
        #self.pushButton_3.clicked.connect(self.view_details)  # Assuming you have a function defined for this.
        self.pushButton_4.clicked.connect(self.update_info)  # Bind the update info event
        self.pushButton_3.clicked.connect(self.open_teacher_detail)
        self.new_rows = set()

    def updateTableView(self, table_name):
            # 执行查询
            cursor = self.db.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")

            # 清除旧的数据
            self.model.removeRows(0, self.model.rowCount())

            # 获取并设置新的数据
            for row_data in cursor:
                row = []
                for item in row_data:
                    cell = QStandardItem(str(item))
                    row.append(cell)
                self.model.appendRow(row)

    def add(self):
            # 在模型中添加空行
            self.model.appendRow([QStandardItem() for _ in range(self.model.columnCount())])

            # 添加新行的索引到集合中
            self.new_rows.add(self.model.rowCount() - 1)



    def delete(self):
            # 获取选中的

            # 获取选中的行
            indexes = self.tableView.selectionModel().selectedRows()
            for index in indexes:
                teacher_name = self.model.item(index.row(), 1).text()  # 假设第一列是学生的名字
                # 删除这个学生
                cursor = self.db.cursor()
                cursor.execute(f"DELETE FROM student WHERE name = '{teacher_name}'")
                self.db.commit()
            # 更新视图
            self.updateTableView("student")

    def update_info(self):
        # 执行查询获取当前数据库中的数据

            cursor = self.db.cursor()
            cursor.execute("SELECT * FROM teacher")
            db_data = list(cursor)

            # 创建一个空字典来存储更改的数据
            changes = {}

            # 检查每一行是否有更改
            for i in range(self.model.rowCount()):
                model_data = [self.model.data(self.model.index(i, j)) for j in range(self.model.columnCount())]

                # 检查这行是不是新添加的行
                if i in self.new_rows:
                    changes[i] = model_data
                else:
                    if model_data != db_data[i]:
                        # 如果这一行有更改，将其添加到changes字典中
                        changes[i] = model_data

            # 如果有数据被修改，则弹出对话框询问用户是否确认更改
            if changes:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setText("您是否确认更改教师信息?")
                msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                ret = msgBox.exec()

                # 如果用户点击了“是”，则将更改提交到数据库
                if ret == QtWidgets.QMessageBox.Yes:
                    cursor = self.db.cursor()
                    # 遍历changes字典并提交更改
                    for row_index, row_data in changes.items():
                        # 这里假设你的教师表有一个名为"id"的列，作为主键
                        if row_index in self.new_rows:
                            cursor.execute(
                                f"INSERT INTO teacher (id, name, phone, day_sum, sum, punish) VALUES (%s, %s, %s, %s, %s, %s)",
                                row_data)
                        else:
                            cursor.execute(
                                f"UPDATE teacher SET id = %s, name = %s, phone = %s, day_sum = %s, sum = %s, punish = %s WHERE id = %s",
                                row_data + [db_data[row_index][0]])
                    self.db.commit()

            # 清空新行集合
            self.new_rows.clear()
    def open_teacher_detail(self):
        # 打开教师课时明细界面
        self.teacher_detail = TeacherSelect()
        self.teacher_detail.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainTeacher()
    window.show()
    sys.exit(app.exec_())