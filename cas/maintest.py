from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import pymysql
from formtest import FormWindow
from mainwindow import Ui_MainWindow
from noteachertest import Noteacher
from nostudenttest import Nostudent
from zhidingtest import ZhiWindow
import subprocess
import course_arrangement
# import cas_16_while


class MainWindo1w(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):

        super(MainWindo1w, self).__init__(parent)
        self.setupUi(self)

        # 创建数据库连接
        self.db = pymysql.connect(host='localhost', user='root', password='wwdcyy', database='course-arrangement system')

        # 创建QStandardItemModel
        self.model = QStandardItemModel(self)
        self.model2 = QStandardItemModel(self)

        # 将模型设置到视图中
        self.tableView.setModel(self.model)
        self.tableView_2.setModel(self.model2)

        # 查询数据并更新视图
        self.updateTableView("student_teacher_subject", self.model)
        self.updateTableView("student_his", self.model2)

        # 绑定按钮点击事件
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)
        self.pushButton_5.clicked.connect(self.show_last_two_classes)
        self.pushButton_6.clicked.connect(self.specifictime)
        self.pushButton_8.clicked.connect(self.openTeacherConstraintsWindow)
        self.pushButton_9.clicked.connect(self.openStudentConstraintsWindow)
        self.pushButton_4.clicked.connect(self.run_course_arrangement)

    def run_course_arrangement(self):  # 新增
        self.db.close()
        course_arrangement.main()

    def show_last_two_classes(self):
        self.last_two_classes_window = FormWindow(self.db)
        self.last_two_classes_window.show()

    def specifictime(self):
        self.specifictime = ZhiWindow(self.db)
        self.specifictime.show()


    def openTeacherConstraintsWindow(self):
        self.teacher_constraints_window = Noteacher(self.db)
        self.teacher_constraints_window.show()

    def openStudentConstraintsWindow(self):
        self.student_constraints_window = Nostudent(self.db)
        self.student_constraints_window.show()
    def updateTableView(self, table_name, model):
        # 执行查询
        cursor = self.db.cursor()
        if table_name == "student_teacher_subject":
            query = '''
            SELECT Student.name, Teacher.name, student_teacher_subject.subject 
            FROM student_teacher_subject 
            INNER JOIN Student ON student_teacher_subject.stu_id = Student.id 
            INNER JOIN Teacher ON student_teacher_subject.teacher_id = Teacher.id
            '''
        elif table_name == "student_his":
            query = '''
            SELECT Student.name, Teacher.name, student_his.subject 
            FROM student_his 
            INNER JOIN Student ON student_his.stu_id = Student.id 
            INNER JOIN Teacher ON student_his.teacher_id = Teacher.id
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

    def add(self):
        # 获取tableview当前选中行
        current_row = self.tableView.currentIndex().row()

        if current_row >= 0:
            # 获取选中行的学生姓名
            student_name = self.model.item(current_row, 0).text()
            # 获取选中行的老师姓名
            teacher_name = self.model.item(current_row, 1).text()  # Assuming teacher name is in column 1

            cursor = self.db.cursor()
            # 在student表中搜索该学生名字对应的id
            cursor.execute(f"SELECT id FROM Student WHERE name='{student_name}'")
            student_id = cursor.fetchone()[0]  # 假设name在Student表中是唯一的

            # 在teacher表中搜索该老师名字对应的id
            cursor.execute(f"SELECT id FROM Teacher WHERE name='{teacher_name}'")
            teacher_id = cursor.fetchone()[0]  # 假设name在Teacher表中是唯一的

            # 在student_teacher_subject表中搜索stu_id和teacher_id对应的行
            cursor.execute(
                f"SELECT * FROM student_teacher_subject WHERE stu_id={student_id} AND teacher_id={teacher_id}")
            student_teacher_entries = cursor.fetchall()

            # 将对应的行写入到student_his表中
            for entry in student_teacher_entries:
                cursor.execute(f"INSERT INTO student_his VALUES {entry}")
                self.db.commit()

            # 更新tableview_2
            self.updateTableView("student_his", self.model2)

    def delete(self):
        # 获取tableview_2当前选中行
        current_row = self.tableView_2.currentIndex().row()

        if current_row >= 0:
            # 获取选中行的学生姓名
            student_name = self.model2.item(current_row, 0).text()
            # 获取选中行的老师姓名
            teacher_name = self.model2.item(current_row, 1).text()  # Assuming teacher name is in column 1

            cursor = self.db.cursor()
            # 在student表中搜索该学生名字对应的id
            cursor.execute(f"SELECT id FROM Student WHERE name='{student_name}'")
            student_id = cursor.fetchone()[0]  # 假设name在Student表中是唯一的

            # 在teacher表中搜索该老师名字对应的id
            cursor.execute(f"SELECT id FROM Teacher WHERE name='{teacher_name}'")
            teacher_id = cursor.fetchone()[0]  # 假设name在Teacher表中是唯一的

            # 从student_his表中删除记录，并更新tableview_2
            try:
                cursor.execute(f"DELETE FROM student_his WHERE stu_id = {student_id} AND teacher_id = {teacher_id}")
                self.db.commit()
                self.updateTableView("student_his", self.model2)
            except Exception as e:
                print(f"Error occurred: {e}")

    #def show_last_two_classes(self):
    #self.last_two_classes_window = Ui_Form()  # assuming you have defined this class in form.py
    #self.last_two_classes_window.show()

#d#ef specifictime(self):
  #  self.specifictime = Ui_zhiding()  # assuming you have defined this class in form.py
 #   self.specifictime.show()

if __name__ == '__main__':
      import sys

      app = QtWidgets.QApplication(sys.argv)
      window = MainWindo1w()
      window.show()
      sys.exit(app.exec_())

