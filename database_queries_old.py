import mysql.connector

def execute_query(query):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="wwdcyy",
        database="Course-arrangement System"
    )
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

# 所有学生
def get_students():
    query = "SELECT name FROM student"
    result = execute_query(query)
    students = [row[0] for row in result]
    return students

#所有老师
def get_teachers():
    query = "SELECT name FROM teacher"
    result = execute_query(query)
    teachers = [row[0] for row in result]
    return teachers

# 学生 - 老师 - 科目
def get_student_teacher_subject():
    query = "SELECT s.name, t.name, sts.subject FROM student_teacher_subject sts JOIN student s ON s.id = sts.stu_id JOIN teacher t ON t.id = sts.teacher_id"
    result = execute_query(query)
    student_teacher_subject = result
    return student_teacher_subject

# 创建一个列表，包含（学生，老师，课程）的元组，这些学生需要在一天内至少上两次他们指定的老师的课程
def get_special_student_teacher_subject():
    special_student_teacher_subject = []
    query = "SELECT s.name, t.name, st.subject FROM student_twice st left join student s on s.id = st.stu_id LEFT JOIN teacher t on t.id = st.teacher_id LEFT JOIN student_teacher_subject sts on sts.stu_id = sts.stu_id AND sts.teacher_id = st.teacher_id"
    result = execute_query(query)
    if result:
        special_student_teacher_subject = result
    return special_student_teacher_subject

# 定义特定的学生-老师-课程-时间组合
def get_specific_student_teacher_subject_time():
    specific_student_teacher_subject_time = []
    query = "SELECT s.name, t.name, sts.subject, st.class_num FROM specific_time st left join student s on s.id = st.stu_id LEFT JOIN teacher t on t.id = st.teacher_id LEFT JOIN student_teacher_subject sts on sts.stu_id = sts.stu_id AND sts.teacher_id = st.teacher_id"
    result = execute_query(query)
    if result:
        specific_student_teacher_subject_time = [(c[0], c[1], c[2], 0, c[3]) for c in result]
    return specific_student_teacher_subject_time

# 学生不可上课时间
def get_student_unavailable_periods():
    student_unavailable_periods = {}
    query = "SELECT id FROM student"
    result = execute_query(query)
    students_id = [s[0] for s in result]
    for stu_id in students_id:
        query = "SELECT class_num FROM student_unavailable_periods s WHERE s.stu_id = {}".format(stu_id)
        result = execute_query(query)
        if result:
            s_unavailable_times = [u[0] for u in result]
            query = "SELECT name FROM student WHERE student.id = {}".format(stu_id)
            result = execute_query(query)
            student_unavailable_periods[result[0]] = s_unavailable_times
        else:
            query = "SELECT name FROM student WHERE student.id = {}".format(stu_id)
            result = execute_query(query)
            student_unavailable_periods[result[0]] = []
    return student_unavailable_periods

# 学生不可上课时间
def get_teacher_unavailable_periods():
    teacher_unavailable_periods = {}
    query = "SELECT id FROM teacher"
    result = execute_query(query)
    teachers_id = [s[0] for s in result]
    for teacher_id in teachers_id:
        query = "SELECT class_num FROM teacher_unavailable_periods t WHERE t.teacher_id = {}".format(teacher_id)
        result = execute_query(query)
        if result:
            t_unavailable_times = [u[0] for u in result]
            query = "SELECT name FROM teacher WHERE teacher.id = {}".format(teacher_id)
            result = execute_query(query)
            teacher_unavailable_periods[result[0]] = t_unavailable_times
        else:
            query = "SELECT name FROM teacher WHERE teacher.id = {}".format(teacher_id)
            result = execute_query(query)
            teacher_unavailable_periods[result[0]] = []
    return teacher_unavailable_periods

# 教师惩罚权重
def get_teacher_overtime():
    query = "SELECT punish FROM teacher"
    result = execute_query(query)
    teacher_overtime = [row[0] for row in result]
    return teacher_overtime

def write_schedule(student, teacher, date, class_num):
    # 创建连接
    cnx = mysql.connector.connect(user='root', password='wwdcyy',
                                  host='localhost',
                                  database='Course-arrangement System')
    cursor = cnx.cursor()

    # 定义要执行的SQL语句
    add_schedule = ("INSERT INTO schedule "
                   "(stu_name, teacher_name, date, class_num) "
                   "VALUES (%s, %s, %s, %s)")

    # 定义要插入的数据
    data_schedule = (student, teacher, date, class_num)

    # 执行SQL语句
    cursor.execute(add_schedule, data_schedule)
    cnx.commit()

    # 关闭游标和连接
    cursor.close()
    cnx.close()

def clear_schedule():
    cnx = mysql.connector.connect(user='root', password='wwdcyy',
                                host='localhost',
                                database='Course-arrangement System')
    cursor = cnx.cursor()

    truncate_table = "TRUNCATE TABLE schedule"
    cursor.execute(truncate_table)

    cnx.commit()
    cursor.close()
    cnx.close()

# students = get_students()
# for s in students:
#     print(s)
