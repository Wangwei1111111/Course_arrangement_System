
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from form import Ui_Form



class FormWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, db, parent=None):
        super(FormWindow, self).__init__(parent)
        self.setupUi(self)
        self.db = db#pymysql.connect("localhost", "root", "123456", "course-arrangement system")

        self.model = QStandardItemModel(self)
        self.model2 = QStandardItemModel(self)

        # 将模型设置到视图中
        self.tableView.setModel(self.model)
        self.tableView_2.setModel(self.model2)

        # 查询数据并更新视图
        self.updateTableView("student_his", self.model)
        self.updateTableView("student_twice", self.model2)

        # Connect button click events to your new methods
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)

    def updateTableView(self, table_name, model):
        # 执行查询
        cursor = self.db.cursor()
        if table_name == "student_his":
            query = '''
            SELECT Student.name, Teacher.name, student_his.subject 
            FROM student_his 
            INNER JOIN Student ON student_his.stu_id = Student.id 
            INNER JOIN Teacher ON student_his.teacher_id = Teacher.id
            '''
        elif table_name == "student_twice":
            query = '''
            SELECT Student.name, Teacher.name, student_twice.subject 
            FROM student_twice 
            INNER JOIN Student ON student_twice.stu_id = Student.id 
            INNER JOIN Teacher ON student_twice.teacher_id = Teacher.id
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
            # 获取选中行的学生姓名和老师姓名
            student_name = self.model.item(current_row, 0).text()
            teacher_name = self.model.item(current_row, 1).text()

            cursor = self.db.cursor()
            # 在student表中搜索该学生名字对应的id
            cursor.execute(f"SELECT id FROM Student WHERE name='{student_name}'")
            student_id = cursor.fetchone()[0]  # 假设name在Student表中是唯一的

            # 在teacher表中搜索该老师名字对应的id
            cursor.execute(f"SELECT id FROM Teacher WHERE name='{teacher_name}'")
            teacher_id = cursor.fetchone()[0]  # 假设name在Teacher表中是唯一的

            # 利用搜索到的id在student_his搜索与该id对应的stu_id和teacher_id
            cursor.execute(f"SELECT * FROM student_his WHERE stu_id={student_id} AND teacher_id={teacher_id}")
            student_subjects = cursor.fetchall()

            # 将stu_id对应的行写入到student_twice表中
            for student_subject in student_subjects:
                cursor.execute(f"INSERT INTO student_twice VALUES {student_subject}")
                self.db.commit()

            # 更新tableview_2
            self.updateTableView("student_twice", self.model2)

    def delete(self):
        # 获取tableview_2当前选中行
        current_row = self.tableView_2.currentIndex().row()

        if current_row >= 0:
            # 获取选中行的学生姓名和老师姓名
            student_name = self.model2.item(current_row, 0).text()
            teacher_name = self.model2.item(current_row, 1).text()

            cursor = self.db.cursor()
            # 在student表中搜索该学生名字对应的id
            cursor.execute(f"SELECT id FROM Student WHERE name='{student_name}'")
            student_id = cursor.fetchone()[0]  # 假设name在Student表中是唯一的

            # 在teacher表中搜索该老师名字对应的id
            cursor.execute(f"SELECT id FROM Teacher WHERE name='{teacher_name}'")
            teacher_id = cursor.fetchone()[0]  # 假设name在Teacher表中是唯一的

            # 从student_twice表中删除记录，并更新tableview_2
            try:
                cursor.execute(f"DELETE FROM student_twice WHERE stu_id = {student_id} AND teacher_id = {teacher_id}")
                self.db.commit()
                self.updateTableView("student_twice", self.model2)
            except Exception as e:
                print(f"Error occurred: {e}")

