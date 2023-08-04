from PyQt5.QtGui import QStandardItem
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import pymysql

from zhiding import Ui_zhiding



class ZhiWindow(QtWidgets.QWidget, Ui_zhiding):
    def __init__(self, db, parent=None):
        super(ZhiWindow, self).__init__(parent)
        self.setupUi(self)
        self.db = db

        self.model = QStandardItemModel(self)
        self.model2 = QStandardItemModel(self)

        # 将模型设置到视图中
        self.tableView.setModel(self.model)
        self.tableView_2.setModel(self.model2)

        # 查询数据并更新视图
        self.updateTableView("student_his", self.model)
        self.updateTableView("specific_time", self.model2)

        # Connect button click events to your new methods
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)

        # Map checkboxes to values
        self.checkbox_map = {
            self.checkBox_6: 1,
            self.checkBox_7: 2,
            self.checkBox_8: 3,
            self.checkBox_9: 4,
            self.checkBox_10: 5,
            self.checkBox_11: 6,
        }

    # UpdateTableView, Delete remain the same...
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
        elif table_name == "specific_time":
            query = '''
            SELECT Student.name, Teacher.name, specific_time.class_num 
            FROM specific_time
            INNER JOIN Student ON specific_time.stu_id = Student.id 
            INNER JOIN Teacher ON specific_time.teacher_id = Teacher.id
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
      try:
        current_row = self.tableView.currentIndex().row()

        if current_row >= 0:
            # 获取选中行的学生姓名
            student_name = self.model.item(current_row, 0).text()

            # 在student表中搜索该名字对应的id
            cursor = self.db.cursor()
            cursor.execute(f"SELECT id FROM Student WHERE name='{student_name}'")
            student_id = cursor.fetchone()[0]  # 假设name在Student表中是唯一的

            # 利用搜索到的id在student_his搜索与该id对应的stu_id
            cursor.execute(f"SELECT * FROM student_his WHERE stu_id='{student_id}'")
            student_subjects = cursor.fetchall()

            # 获取勾选的checkbox对应的值
            selected_value = None
            for checkbox, value in self.checkbox_map.items():
                if checkbox.isChecked():
                    selected_value = value
                    break

            if selected_value is not None:
                # 将stu_id对应的行写入到specific_time表中
                for student_subject in student_subjects:
                    cursor.execute(
                        f"INSERT INTO specific_time(stu_id, teacher_id, class_num) VALUES ({student_subject[0]}, {student_subject[1]}, {selected_value})")
                    self.db.commit()

                # 更新tableview_2

                self.updateTableView("specific_time", self.model2)
      except Exception as e:
          print(f"An error occurred: {e}")

    def delete(self):
        # 获取tableview_2当前选中行
        current_row = self.tableView_2.currentIndex().row()

        if current_row >= 0:
            # 获取选中行的学生姓名和特定的时间
            cursor = self.db.cursor()
            student_name = self.model2.item(current_row, 0).text()
            class_num = int(self.model2.item(current_row, 2).text()) - 1 # 注意这里我们获取的是第3列，即class_num

            # 在student表中搜索该名字对应的id
            cursor.execute(f"SELECT id FROM Student WHERE name='{student_name}'")
            student_id = cursor.fetchone()[0]  # 假设name在Student表中是唯一的

            # 从specific_time表中删除记录，并更新tableview_2
            try:
                cursor.execute(f"DELETE FROM specific_time WHERE stu_id = {student_id} AND class_num = {class_num}")
                self.db.commit()
                self.updateTableView("specific_time", self.model2)
            except Exception as e:
                print(f"Error occurred: {e}")

