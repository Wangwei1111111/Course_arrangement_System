import pymysql
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from teacherselect import Ui_teacherselect  # 导入老师查询界面


class TeacherSelect(QtWidgets.QMainWindow, Ui_teacherselect):
    def __init__(self, parent=None):
        super(TeacherSelect, self).__init__(parent)
        self.setupUi(self)

        # 创建数据库连接
        self.db = pymysql.connect(host='localhost', user='root', password='wwdcyy', database='course-arrangement system')

        # 创建QStandardItemModel
        self.model1 = QStandardItemModel(self)
        self.model2 = QStandardItemModel(self)

        # 将模型设置到视图中
        self.tableView.setModel(self.model1)
        self.tableView_2.setModel(self.model2)

        # 绑定按钮点击事件
        self.pushButton.clicked.connect(self.query_teacher)

    def query_teacher(self):
        try:
            teacher_name = self.lineEdit.text()

            # 查询并更新tableview
            cursor = self.db.cursor()
            cursor.execute("SELECT * FROM schedule_mirror WHERE teacher_name = %s", (teacher_name,))
            self.update_table_view(cursor, self.model1)

            # 查询并更新tableview_2
            cursor.execute("SELECT teacher_name, grade, SUM(time) FROM schedule_mirror WHERE teacher_name = %s GROUP BY grade",
                           (teacher_name,))
            self.update_table_view(cursor, self.model2)

        except Exception as e:
            print(f"Error occurred: {e}")

    @staticmethod
    def update_table_view(cursor, model):
        # 清除旧的数据
        model.removeRows(0, model.rowCount())

        # 获取并设置新的数据
        for row_data in cursor:
            row = [QStandardItem(str(item)) for item in row_data]
            model.appendRow(row)

# 下面是应用程序入口
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = TeacherSelect()
    MainWindow.show()
    sys.exit(app.exec_())
