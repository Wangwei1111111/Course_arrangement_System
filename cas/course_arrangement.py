import datetime
from ortools.sat.python import cp_model
import database_queries as db
import pandas as pd

class_time = {
    0: '8:00~10:00',
    1: '10:00~12:00',
    2: '12:00~14:00',
    3: '14:00~16:00',
    4: '16:00~18:00',
    5: '18:00~20:00',
    6: '20:00~22:00',
    7: '22:00~24:00'
}

# 写入excel方法
# def to_excel():


def main():
    # 导入数据
    students = db.get_students()
    teachers = db.get_teachers()
    student_grade = db.get_student_grade()
    subjects = ["语文", "化学", "英语", "物理", "数学"]
    student_teacher_subject = db.get_student_teacher_subject()
    print('student_teacher_subject')

    # 创建一个列表，包含（学生，老师，课程）的元组，这些学生需要在一天内至少上两次他们指定的老师的课程
    special_student_teacher_subject = db.get_special_student_teacher_subject()

    # 定义特定的学生-老师-课程-时间组合
    specific_student_teacher_subject_time = db.get_specific_student_teacher_subject_time()

    # 学生的不可上课时间
    student_unavailable_periods = db.get_student_unavailable_periods()

    # 老师的不可用时间
    teacher_unavailable_periods = db.get_teacher_unavailable_periods()

    # 老师惩罚权重（默认为最低10）
    teacher_overtime = db.get_teacher_overtime()

    print('student_teacher_155415165156165')

    num_days = 1
    max_classes_per_day = 6

    while max_classes_per_day < 9:
        # 初始化 CP-SAT 模型
        model = cp_model.CpModel()
        print("((((()))))")
        # 创建变量
        schedule = {}
        for student in students:
            for teacher in teachers:
                for subject in subjects:
                    for day in range(num_days):
                        for class_num in range(max_classes_per_day):
                            var_name = f"s{student}_t{teacher}_{subject}_d{day}_c{class_num}"
                            schedule[var_name] = model.NewBoolVar(var_name)

        # 添加指定的学生-老师-课程-时间组合约束
        for student_name, teacher_name, subject_name, day, class_num in specific_student_teacher_subject_time:
            var_name = f"s{student_name}_t{teacher_name}_{subject_name}_d{day}_c{class_num}"
            model.Add(schedule[var_name] == 1)

        # 添加约束条件
        for student, teacher, subject in student_teacher_subject:
            for day in range(num_days):
                subject_classes = [
                    schedule[f"s{student}_t{teacher}_{subject}_d{day}_c{class_num}"]
                    for class_num in range(max_classes_per_day)
                ]
                model.Add(sum(subject_classes) >= 1)

        # 每个特定的学生-老师-课程组合一天内的课程至少为2次
        for student_name, teacher_name, subject_name in special_student_teacher_subject:
            class_vars = [
                schedule[f"s{student_name}_t{teacher_name}_{subject_name}_d{day}_c{class_num}"]
                for day in range(num_days)
                for class_num in range(max_classes_per_day)
            ]
            model.Add(sum(class_vars) >= 2)  

        # 在一天内，一个学生只能上一门课程一次
        for student in students:
            for teacher in teachers:
                for subject in subjects:
                    if (student, teacher, subject) not in special_student_teacher_subject:
                        for day in range(num_days):
                            student_subject_classes = [
                                schedule[f"s{student}_t{teacher}_{subject}_d{day}_c{class_num}"]
                                for class_num in range(max_classes_per_day)
                            ]
                            model.Add(sum(student_subject_classes) <= 1)

        # 老师每天最多上6节课
        for teacher in teachers:
            for day in range(num_days):
                teacher_classes = [schedule[f"s{student}_t{teacher}_{subject}_d{day}_c{class_num}"]
                                for student in students
                                for subject in subjects
                                for class_num in range(max_classes_per_day)]
                model.Add(sum(teacher_classes) <= max_classes_per_day)

        # 学生每天最多上6节课
        for student in students:
            for day in range(num_days):
                student_classes = [schedule[f"s{student}_t{teacher}_{subject}_d{day}_c{class_num}"]
                                for teacher in teachers
                                for subject in subjects
                                for class_num in range(max_classes_per_day)]
                model.Add(sum(student_classes) <= max_classes_per_day)

        # 在一个时间段内，学生只能上一门课程
        for student in students:
            for day in range(num_days):
                for class_num in range(max_classes_per_day):
                    student_classes = [
                        schedule[f"s{student}_t{teacher}_{subject}_d{day}_c{class_num}"]
                        for teacher in teachers
                        for subject in subjects
                    ]
                    model.Add(sum(student_classes) <= 1)

        # 在一个时间段内，老师只能教一门课程
        for teacher in teachers:
            for day in range(num_days):
                for class_num in range(max_classes_per_day):
                    teacher_classes = [
                        schedule[f"s{student}_t{teacher}_{subject}_d{day}_c{class_num}"]
                        for student in students
                        for subject in subjects
                    ]
                    model.Add(sum(teacher_classes) <= 1)

        # 添加学生不可上课的硬约束
        for student, unavailable_times in student_unavailable_periods.items():
            for day in range(num_days):
                for class_num in unavailable_times:
                    model.Add(sum(schedule[f"s{student}_t{teacher}_{subject}_d{day}_c{class_num}"]
                                for teacher in teachers
                                for subject in subjects) == 0)


        # 指定一个惩罚变量
        penalties = []

        # 定义一个用于存储overtime变量的字典
        overtime_vars = {}

        # 添加老师不可上课的软约束
        for teacher, unavailable_times in teacher_unavailable_periods.items():
            for day in range(num_days):
                for class_num in unavailable_times:
                    overtime = model.NewIntVar(0, max_classes_per_day, f'overtime_t{teacher}_d{day}_c{class_num}')
                    penalties.append(overtime * teacher_overtime[teacher])
                    # 将overtime变量保存在字典中
                    overtime_vars[(teacher, day, class_num)] = overtime
                    model.Add(overtime >= sum(schedule[f"s{student}_t{teacher}_{subject}_d{day}_c{class_num}"]
                                for student in students
                                for subject in subjects))

        # 添加目标函数，最小化惩罚
        model.Minimize(sum(penalties))

        # 求解模型
        solver = cp_model.CpSolver()
        status = solver.Solve(model)

        # 输出结果
        if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
            
            # 写入excel
            # to_excel()
            columns = ["上课时间", "学生", "教师", "科目", "课时", "年级"]
            df_schedule = pd.DataFrame(columns=columns)

            # 填充数据
            for day in range(num_days):
                for class_num in range(max_classes_per_day):
                    for student in students:
                        for teacher in teachers:
                            for subject in subjects:
                                var_name = f"s{student}_t{teacher}_{subject}_d{day}_c{class_num}"
                                if solver.Value(schedule[var_name]) == 1:
                                    if overtime_vars.__contains__((teacher, day, class_num)):
                                        if solver.Value(overtime_vars[(teacher, day, class_num)]) > 0:
                                            row = ["*" + class_time[class_num], student, "*" + teacher + "*", subject, 2.0, student_grade[student]]
                                    else:
                                        row = [class_time[class_num], student, teacher, subject, 2.0, student_grade[student]]
                                    df_schedule = df_schedule.append(pd.Series(row, index=columns), ignore_index=True)
                    # 在每节课后添加一行空行
                    df_schedule = df_schedule.append(pd.Series([None]*len(columns), index=columns), ignore_index=True)

            columns_t = ["教师", "学生", "科目", "上课时间", "课时", "年级"]
            df_schedule_teacher = pd.DataFrame(columns=columns_t)

            # 填充数据
            for day in range(num_days):
                for teacher in teachers:
                    for class_num in range(max_classes_per_day):
                        for student in students:
                            for subject in subjects:
                                var_name = f"s{student}_t{teacher}_{subject}_d{day}_c{class_num}"
                                if solver.Value(schedule[var_name]) == 1:
                                    if overtime_vars.__contains__((teacher, day, class_num)):
                                        if solver.Value(overtime_vars[(teacher, day, class_num)]) > 0:
                                            row = ["*" + teacher + "*", student, subject, "*" + class_time[class_num], 2.0, student_grade[student]]
                                    else:
                                        row = [teacher, student, subject, class_time[class_num], 2.0, student_grade[student]]
                                    df_schedule_teacher = df_schedule_teacher.append(pd.Series(row, index=columns_t), ignore_index=True)
                    # 在每个教师的课表后添加一行空行
                    df_schedule_teacher = df_schedule_teacher.append(pd.Series([None]*len(columns_t), index=columns_t), ignore_index=True)

            columns_s = ["学生", "教师", "科目", "上课时间", "课时", "年级"]
            df_schedule_student = pd.DataFrame(columns=columns_s)

            # 填充数据
            for day in range(num_days):
                for student in students:
                    for class_num in range(max_classes_per_day):
                        for teacher in teachers:
                            for subject in subjects:
                                var_name = f"s{student}_t{teacher}_{subject}_d{day}_c{class_num}"
                                if solver.Value(schedule[var_name]) == 1:
                                    if overtime_vars.__contains__((teacher, day, class_num)):
                                        if solver.Value(overtime_vars[(teacher, day, class_num)]) > 0:
                                            row = [student, "*" + teacher + "*", subject, "*" + class_time[class_num], 2.0, student_grade[student]]
                                    else:
                                        row = [student, teacher, subject, class_time[class_num], 2.0, student_grade[student]]
                                    df_schedule_student = df_schedule_student.append(pd.Series(row, index=columns_s), ignore_index=True)
                    # 在每个教师的课表后添加一行空行
                    df_schedule_student = df_schedule_student.append(pd.Series([None]*len(columns_s), index=columns_s), ignore_index=True)

            # 创建ExcelWriter对象，指定目标Excel文件的名称
            with pd.ExcelWriter('schedule.xlsx') as writer:
                df_schedule.to_excel(writer, sheet_name='总课表', index=False)
                df_schedule_teacher.to_excel(writer, sheet_name='教师课表', index=False)
                df_schedule_student.to_excel(writer, sheet_name='学生课表', index=False)
            
            # 写入数据库
            db.clear_schedule()
            for day in range(num_days):
                for class_num in range(max_classes_per_day):
                    for student in students:
                        for teacher in teachers:
                            for subject in subjects:
                                var_name = f"s{student}_t{teacher}_{subject}_d{day}_c{class_num}"
                                if solver.Value(schedule[var_name]) == 1:
                                    # 注意这里的日期应该是明天的日期
                                    date = datetime.date.today() + datetime.timedelta(days=1)
                                    db.write_schedule(student, teacher, date, class_num, 2.0, student_grade[student])
            
            print("success")
        
            break
        else:
            max_classes_per_day += 1

    print(max_classes_per_day)
    if max_classes_per_day >= 9:
        db.clear_schedule()
        columns = ["上课时间", "学生", "教师", "科目"]
        df_schedule = pd.DataFrame(columns=columns)
        df_schedule = df_schedule.append(pd.Series([None]*len(columns), index=columns), ignore_index=True)
        with pd.ExcelWriter('schedule.xlsx') as writer:
            df_schedule.to_excel(writer, sheet_name='总课表', index=False)