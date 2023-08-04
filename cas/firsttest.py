import pymysql
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from mainstudent import Ui_mainstudent  # 导入学生管理界面
from mainstudenttest import MainStudent
from mainteacher import Ui_mainteacher  # 导入老师管理界面
from mainteachertest import MainTeacher
from maintest import MainWindo1w
from mainwindow import Ui_MainWindow# 导入排课界面
from first import Ui_first

class MainApp(QtWidgets.QMainWindow, Ui_first):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.db = pymysql.connect(host='localhost', user='root', password='wwdcyy', database='course-arrangement system')
        # 创建QStandardItemModel
        self.model = QStandardItemModel(self)

        # 将模型设置到视图中
        self.tableView.setModel(self.model)

        # 查询数据并更新视图
        self.updateTableView("schedule")

        # 将按钮点击事件与处理函数关联
        self.pushButton.clicked.connect(self.open_student_manager)
        self.pushButton_2.clicked.connect(self.open_teacher_manager)
        self.pushButton_3.clicked.connect(self.open_course_scheduler)
        self.pushButton_4.clicked.connect(self.update_sum)
    def updateTableView(self, table_name):


            self.model.removeRows(0, self.model.rowCount())

            cursor = self.db.cursor()

            if table_name == "schedule":
                # 执行查询
                cursor.execute("SELECT stu_name, teacher_name, date,class_num + 1 FROM schedule")
            else:
                # 执行查询
                cursor.execute(f"SELECT * FROM {table_name}")

            # 获取并设置新的数据
            for row_data in cursor:
                row = []
                for item in row_data:
                    cell = QStandardItem(str(item))
                    row.append(cell)
                self.model.appendRow(row)

            # 执行查询
            #cursor = self.db.cursor()
            #cursor.execute(f"SELECT * FROM {table_name}")

            # 清除旧的数据
            #self.model.removeRows(0, self.model.rowCount())

            # 获取并设置新的数据
            #for row_data in cursor:
             #   row = []
              #  for item in row_data:
               #     cell = QStandardItem(str(item))
                #    row.append(cell)
                #self.model.appendRow(row)

    def open_student_manager(self):
        # 打开学生管理界面
        self.course_scheduler = MainStudent()  # MainWindow类需要有一个无参构造器
        self.course_scheduler.show()

    def open_teacher_manager(self):
        # 打开老师管理界面
        self.course_scheduler = MainTeacher()  # MainWindow类需要有一个无参构造器
        self.course_scheduler.show()

    def open_course_scheduler(self):
        # 打开排课界面
        self.course_scheduler = MainWindo1w()  # MainWindow类需要有一个无参构造器
        self.course_scheduler.show()

    def update_sum(self):
        try:
            # 获取选中行的信息
            selected_row = self.tableView.currentIndex().row()
            selected_student_name = self.tableView.model().item(selected_row, 0).text()
            selected_teacher_name = self.tableView.model().item(selected_row, 1).text()
            selected_class_num = str(int(self.tableView.model().item(selected_row, 3).text()) - 1)  # 获取class_num字段，然后将其减1

            # 更新student表的sum字段
            cursor = self.db.cursor()
            cursor.execute("UPDATE student SET sum=sum+2 WHERE name=%s", (selected_student_name,))

            # 更新teacher表的sum字段
            cursor.execute("UPDATE teacher SET sum=sum+2 WHERE name=%s", (selected_teacher_name,))

            # 将选中的行的数据插入到schedule_mirror表中
            cursor.execute(
                "INSERT INTO schedule_mirror SELECT * FROM schedule WHERE stu_name=%s AND teacher_name=%s AND class_num=%s",
                (selected_student_name, selected_teacher_name, selected_class_num))

            # 从schedule表中删除选中的行
            cursor.execute("DELETE FROM schedule WHERE stu_name=%s AND teacher_name=%s AND class_num=%s",
                           (selected_student_name, selected_teacher_name, selected_class_num))

            # 提交数据库事务
            self.db.commit()

            # 更新表格显示
            self.updateTableView("schedule")
        except Exception as e:
            print(f"Error occurred: {e}")

    #def update_sum(self):
      #try:

        # 获取选中行的信息
        #selected_row = self.tableView.currentIndex().row()
        #selected_student_name = self.tableView.model().item(selected_row, 0).text()
        #selected_teacher_name = self.tableView.model().item(selected_row, 1).text()

        # 更新student表的sum字段
        #cursor = self.db.cursor()
        #cursor.execute("UPDATE student SET sum=sum+2 WHERE name=%s", (selected_student_name,))

        # 更新teacher表的sum字段
        #cursor.execute("UPDATE teacher SET sum=sum+2 WHERE name=%s", (selected_teacher_name,))

        # 提交数据库事务
        #self.db.commit()

        # 更新表格显示
        #self.updateTableView("schedule")
     # except Exception as e:
      #    print(f"Error occurred: {e}")


# 下面是应用程序入口
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainApp()
    MainWindow.show()
    sys.exit(app.exec_())

