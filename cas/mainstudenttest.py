
from mainstudent import Ui_mainstudent
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import pymysql
import sys
class UneditableStandardItem(QStandardItem):
    def __init__(self, *args, **kwargs):
        super(UneditableStandardItem, self).__init__(*args, **kwargs)

    def flags(self):
        return super(UneditableStandardItem, self).flags() & ~QtCore.Qt.ItemIsEditable

class MainStudent(QtWidgets.QMainWindow, Ui_mainstudent):
    def __init__(self, parent=None):
        super(MainStudent, self).__init__(parent)
        self.setupUi(self)

        # 创建数据库连接
        self.db = pymysql.connect(host='localhost', user='root', password='wwdcyy', database='course-arrangement system')

        # 创建QStandardItemModel
        self.model = QStandardItemModel(self)

        # 将模型设置到视图中
        self.tableView.setModel(self.model)

        # 查询数据并更新视图
        self.updateTableView("student")

        # 绑定按钮点击事件
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)
        self.pushButton_4.clicked.connect(self.update_info)
        self.pushButton_5.clicked.connect(self.confirm_changes)


        # 创建一个集合存储新行的索引
        self.new_rows = set()

    def updateTableView(self, table_name):
        # 执行查询
        #cursor = self.db.cursor()
        #cursor.execute(f"SELECT * FROM {table_name}")

        # 清除旧的数据
        #self.model.removeRows(0, self.model.rowCount())

        # 获取并设置新的数据
        #for row_data in cursor:
         #   row = []
         #   for item in row_data:
          #      cell = QStandardItem(str(item))
           #     row.append(cell)
            #self.model.appendRow(row)
        cursor = self.db.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")

        # 清除旧的数据
        self.model.removeRows(0, self.model.rowCount())

        # 获取并设置新的数据
        for row_data in cursor:
            row = []
            for i, item in enumerate(row_data):
                if i in (4, 5):  # 假设 'sum' 和 'paid' 是第 5 和第 6 列
                    cell = UneditableStandardItem(str(item))
                else:
                    cell = QStandardItem(str(item))
                row.append(cell)
            self.model.appendRow(row)

    def add(self):
        # 在模型中添加空行
        self.model.appendRow([QStandardItem() for _ in range(self.model.columnCount())])

        # 添加新行的索引到集合中
        self.new_rows.add(self.model.rowCount() - 1)

    def confirm_changes(self):
        # 检查每一行是否有空白的项
        for i in self.new_rows:
            if any(self.model.item(i, j) is None or self.model.item(i, j).text() == "" for j in range(self.model.columnCount())):
                continue  # 如果这一行有空白的项，则跳过

            # 弹出对话框询问用户是否确认增加
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("您是否确认增加一个学生?")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            ret = msgBox.exec()

            # 如果用户点击了“是”，则将新行的数据写入数据库
            if ret == QtWidgets.QMessageBox.Yes:
                cursor = self.db.cursor()
                # 请根据您的学生表的列定义填充这个列表
                values = [self.model.data(self.model.index(i, j)) for j in range(self.model.columnCount())]
                cursor.execute(f"INSERT INTO student VALUES ({', '.join(['%s']*len(values))})", values)
                self.db.commit()

        # 清空新行的索引集合
        self.new_rows.clear()

    def delete(self):
        # 获取选中的

        # 获取选中的行
        indexes = self.tableView.selectionModel().selectedRows()
        for index in indexes:
            student_name = self.model.item(index.row(), 1).text()  # 假设第一列是学生的名字
            # 删除这个学生
            cursor = self.db.cursor()
            cursor.execute(f"DELETE FROM student WHERE name = '{student_name}'")
            self.db.commit()
        # 更新视图
        self.updateTableView("student")


    def update_info(self):
        # 执行查询获取当前数据库中的数据
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM student")
        db_data = list(cursor)

        # 创建一个空字典来存储更改的数据
        changes = {}

        # 检查每一行是否有更改
        for i in range(self.model.rowCount()):
            model_data = [self.model.data(self.model.index(i, j)) for j in range(self.model.columnCount())]
            db_row_data = db_data[i]

            # 跳过 'sum' 和 'paid' 列
            for j in (4, 5):  # 假设 'sum' 和 'paid' 是第 5 和第 6 列
                model_data[j] = db_row_data[j]

            if model_data != db_row_data:
                # 如果这一行有更改，将其添加到changes字典中
                changes[i] = model_data

        # 如果有数据被修改，则弹出对话框询问用户是否确认更改
        if changes:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("您是否确认更改学生信息?")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            ret = msgBox.exec()

            # 如果用户点击了“是”，则将更改提交到数据库
            if ret == QtWidgets.QMessageBox.Yes:
                cursor = self.db.cursor()
                # 遍历changes字典并提交更改
                for row_index, row_data in changes.items():
                    # 这里假设你的学生表有一个名为"id"的列，作为主键
                    cursor.execute(
                        f"UPDATE student SET id = %s, name = %s, grade = %s, phone = %s,sum = %s, paid = %s WHERE id = %s",
                        row_data + [db_data[row_index][0]])
                self.db.commit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainStudent()
    window.show()
    sys.exit(app.exec_())