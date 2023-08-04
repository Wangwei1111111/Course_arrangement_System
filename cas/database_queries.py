import mysql.connector
from configparser import ConfigParser

def read_db_config(filename='config.ini', section='mysql'):
    """读取配置文件中的数据库连接信息"""
    # 创建一个ConfigParser对象
    parser = ConfigParser()
    # 读取配置文件
    parser.read(filename)
    # 获取指定section中的配置信息
    db_config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db_config

def execute_query(query):
    # 从配置文件中读取数据库连接信息
    db_config = read_db_config()
    conn = mysql.connector.connect(**db_config, use_pure=True)
    # print(conn)
    cursor = conn.cursor()
    # print('llllllll')
    cursor.execute(query)
    result = cursor.fetchall()
    # print('WWWWWWW')
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
    query = "SELECT s.name, t.name, st.subject FROM student_twice st left join student s on s.id = st.stu_id LEFT JOIN teacher t on t.id = st.teacher_id"
    result = execute_query(query)
    if result:
        special_student_teacher_subject = result
    return special_student_teacher_subject

# 定义特定的学生-老师-课程-时间组合
def get_specific_student_teacher_subject_time():
    specific_student_teacher_subject_time = []
    query = "SELECT s.name, t.name, sts.subject, st.class_num FROM specific_time st INNER JOIN student s ON s.id = st.stu_id INNER JOIN teacher t ON t.id = st.teacher_id INNER JOIN student_teacher_subject sts ON sts.stu_id = st.stu_id AND sts.teacher_id = st.teacher_id"
    result = execute_query(query)
    if result:
        specific_student_teacher_subject_time = [(c[0], c[1], c[2], 0, c[3]) for c in result]
    return specific_student_teacher_subject_time

# 学生不可上课时间
def get_student_unavailable_periods():
    student_unavailable_periods = {}
    query = "SELECT id, name FROM student"
    result = execute_query(query)
    # print(len(result))
    for stu_id, stu_name in result:
        query = "SELECT class_num FROM student_unavailable_periods s WHERE s.stu_id = {}".format(stu_id)
        result = execute_query(query)
        if result:
            s_unavailable_times = [int(u[0]) for u in result]
            student_unavailable_periods[stu_name] = s_unavailable_times
        else:
            student_unavailable_periods[stu_name] = []
    return student_unavailable_periods

# 老师不可上课时间
def get_teacher_unavailable_periods():
    teacher_unavailable_periods = {}
    query = "SELECT id, name FROM teacher"
    result = execute_query(query)
    for teacher_id, teacher_name in result:
        query = "SELECT class_num FROM teacher_unavailable_periods t WHERE t.teacher_id = {}".format(teacher_id)
        result = execute_query(query)
        if result:
            t_unavailable_times = [int(u[0]) for u in result]
            teacher_unavailable_periods[teacher_name] = t_unavailable_times
        else:
            teacher_unavailable_periods[teacher_name] = []
    return teacher_unavailable_periods

# 教师惩罚权重
def get_teacher_overtime():
    teacher_overtime = {}
    query = "SELECT name, punish FROM teacher"
    result = execute_query(query)
    for row in result:
        teacher_name = row[0]
        punish = int(row[1])
        teacher_overtime[teacher_name] = punish
    return teacher_overtime

# 获取学生年级，字典
def get_student_grade():
    student_grade = {}
    query = "SELECT name, grade FROM student"
    result = execute_query(query)
    for row in result:
        student_name = row[0]
        grade = row[1]
        student_grade[student_name] = grade
    return student_grade

def write_schedule(student, teacher, date, class_num, time, grade):
    # 创建连接
    db_config = read_db_config()
    cnx = mysql.connector.connect(**db_config, use_pure=True)
    cursor = cnx.cursor()

    # 定义要执行的SQL语句
    add_schedule = ("INSERT INTO schedule "
                   "(stu_name, teacher_name, date, class_num, time, grade) "
                   "VALUES (%s, %s, %s, %s, %s, %s)")

    # 定义要插入的数据
    data_schedule = (student, teacher, date, class_num, time, grade)

    # 执行SQL语句
    cursor.execute(add_schedule, data_schedule)
    cnx.commit()

    # 关闭游标和连接
    cursor.close()
    cnx.close()

def clear_schedule():
    db_config = read_db_config()
    cnx = mysql.connector.connect(**db_config, use_pure=True)
    cursor = cnx.cursor()

    truncate_table = "TRUNCATE TABLE schedule"
    cursor.execute(truncate_table)

    cnx.commit()
    cursor.close()
    cnx.close()

# students = get_students()
# for s in students:
#     print(s)

# special_student_teacher_subject = get_special_student_teacher_subject()
# print(special_student_teacher_subject)

# specific_student_teacher_subject_time = get_specific_student_teacher_subject_time()
# print(specific_student_teacher_subject_time)

# student_un = get_student_unavailable_periods()
# print(student_un)

# teacher_un = get_teacher_unavailable_periods()
# print(teacher_un)

# teacher_overtime = get_teacher_overtime()
# print(teacher_overtime)e

# student_grade = get_student_grade()
# print(student_grade)