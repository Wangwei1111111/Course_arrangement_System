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
def to_excel():
    columns = ["上课时间", "学生", "教师", "科目"]
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
                                    row = ["*" + class_time[class_num], student, "*" + teacher + "*", subject]
                            else:
                                row = [class_time[class_num], student, teacher, subject]
                            df_schedule = df_schedule.append(pd.Series(row, index=columns), ignore_index=True)
            # 在每节课后添加一行空行
            df_schedule = df_schedule.append(pd.Series([None]*len(columns), index=columns), ignore_index=True)

    columns_t = ["教师", "学生", "科目", "上课时间"]
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
                                    row = ["*" + teacher + "*", student, subject, "*" + class_time[class_num]]
                            else:
                                row = [teacher, student, subject, class_time[class_num]]
                            df_schedule_teacher = df_schedule_teacher.append(pd.Series(row, index=columns_t), ignore_index=True)
            # 在每个教师的课表后添加一行空行
            df_schedule_teacher = df_schedule_teacher.append(pd.Series([None]*len(columns_t), index=columns_t), ignore_index=True)

    columns_s = ["学生", "教师", "科目", "上课时间"]
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
                                    row = [student, "*" + teacher + "*", subject, "*" + class_time[class_num]]
                            else:
                                row = [student, teacher, subject, class_time[class_num]]
                            df_schedule_student = df_schedule_student.append(pd.Series(row, index=columns_s), ignore_index=True)
            # 在每个教师的课表后添加一行空行
            df_schedule_student = df_schedule_student.append(pd.Series([None]*len(columns_s), index=columns_s), ignore_index=True)

    # 创建ExcelWriter对象，指定目标Excel文件的名称
    with pd.ExcelWriter('schedule.xlsx') as writer:
        df_schedule.to_excel(writer, sheet_name='总课表', index=False)
        df_schedule_teacher.to_excel(writer, sheet_name='教师课表', index=False)
        df_schedule_student.to_excel(writer, sheet_name='学生课表', index=False)

# 定义数据
students = ["睿哲", "保烨", "殿朝", "李淼", "杨雯雯", "玉轩", "紫琦", "容俞", "董静", "中乔", "戈钊",
            "春奥", "富甲", "庆晓", "恒英", "力家", "子涵", "育良", "美娜", "思蒙", "慧敏", "王青", "姿琪","梦宣","传聪","芳阁","黄心","彭真"]
teachers = ["传廷", "沈佳佳", "文琦", "贵强", "保发", "杜婷婷", "段", "王宇", "顾立", "延蒙", "沈琳琳",
            "于", "李战胜", "张书冬", "王炜", "郁", "马坤（高中）", "刘佳佳", "常", "志硕","晓晴","隋欣","张娜","崔","赵会"]
subjects = ["语文", "化学", "英语", "物理", "数学"]
student_teacher_subject = [
    ("玉轩", "沈琳琳", "语文"),
    ("玉轩", "贵强", "语文"),
    ("玉轩", "段", "语文"),
    ("玉轩", "张书冬", "语文"),
    ("玉轩", "传廷", "语文"),
    ("紫琦", "郁", "语文"),
    ("紫琦", "杜婷婷", "化学"),
    ("中乔", "沈琳琳", "化学"),
    ("中乔", "张书冬", "化学"),
    ("中乔", "常", "化学"),
    ("中乔", "沈佳佳", "化学"),
    ("戈钊", "晓晴", "化学"),
    ("戈钊", "李战胜", "化学"),
    ("戈钊", "传廷", "化学"),
    ("戈钊", "段", "化学"),
    ("春奥", "郁", "化学"),
    ("春奥", "隋欣", "英语"),
    ("春奥", "保发", "化学"),
    ("春奥", "常", "物理"),
    ("富甲", "李战胜", "物理"),
    ("睿哲", "志硕", "数学"),
    ("睿哲", "李战胜", "物理"),
    ("睿哲", "沈佳佳", "语文"),
    ("睿哲", "段", "英语"),
    ("子涵", "传廷", "物理"),
    ("子涵", "杜婷婷", "物理"),
    ("子涵", "马坤（高中）", "数学"),
    ("子涵", "于", "物理"),
    ("育良", "李战胜", "数学"),
    ("育良", "志硕", "数学"),
    ("育良", "杜婷婷", "数学"),
    ("育良", "张娜", "数学"),
    ("美娜", "延蒙", "物理"),
    ("美娜", "沈琳琳", "物理"),
    ("美娜", "段", "物理"),
    ("美娜", "张书冬", "物理"),
    ("芳阁", "杜婷婷", "化学"),
    ("芳阁", "崔", "化学"),
    ("芳阁", "沈佳佳", "化学"),
    ("芳阁", "常", "化学"),
    ("王青", "志硕", "数学"),
    ("王青", "赵会", "数学"),
    ("王青", "李战胜", "数学"),
    ("王青", "张娜", "数学"),
    ("梦宣", "杜婷婷", "化学"),
    ("梦宣", "段", "化学"),
    ("梦宣", "晓晴", "化学"),
    ("梦宣", "沈佳佳", "语文"),
    ("姿琪", "郁", "数学"),
    ("容俞", "隋欣", "英语"),
    ("容俞", "保发", "化学"),
    ("黄心", "郁", "化学"),
    ("黄心", "于", "化学"),
    ("董静", "志硕", "物理"),
    ("董静", "赵会", "物理"),
    ("董静", "杜婷婷", "物理"),
]

# 创建一个列表，包含（学生，老师，课程）的元组，这些学生需要在一天内至少上两次他们指定的老师的课程
special_student_teacher_subject = [
    ("梦宣", "沈佳佳", "语文"),
    ("紫琦", "杜婷婷", "化学"),
    ("子涵", "马坤（高中）", "数学"),
    ("育良", "志硕", "数学"),
    ("玉轩", "张书冬", "语文"),
]

# 定义特定的学生-老师-课程-时间组合
specific_student_teacher_subject_time = [
    ("富甲", "李战胜", "物理", 0, 5),
    ("玉轩", "张书冬", "语文", 0, 3),
    ("美娜", "沈琳琳", "物理", 0, 1),
    ("姿琪", "郁", "数学", 0, 5),
    ("玉轩", "张书冬", "语文", 0, 4),
    ("戈钊", "晓晴", "化学",0, 0),
    ("梦宣", "晓晴", "化学", 0, 5),
]

# 学生的不可上课时间
student_unavailable_periods = {'紫琦': [0, 2, 3],
                               '李淼': [0, 2, 5],
                               '中乔': [2, 5],
                               '富甲': [0, 1, 2, 3, 4],
                               '姿琪': [0, 1, 2, 3],
                               '睿哲': [5],
                               '容俞': [1,3,4,5],
                               '美娜': [0,3],
                               '戈钊': [2,5],
                               '春奥': [2,5],
                               '子涵': [2],
                               '育良': [2],
                               '芳阁': [2, 5],
                               '王青': [2],
                               '梦宣': [2],
                               '传聪': [0, 1, 2, 3, 4],
                               '保烨': [],
                               '殿朝': [],
                               '杨雯雯': [],
                               '玉轩': [],
                               '董静': [],
                               '庆晓': [],
                               '恒英': [],
                               '力家': [],
                               '思蒙': [],
                               '慧敏': [],
                               '黄心': [],
                               '彭真': [],}


# 老师的不可用时间
teacher_unavailable_periods = {'沈佳佳': [2],
                               '贵强': [0, 1, 3, 4],
                               '段': [5],
                               '于': [0, 1, 2, 3],
                               '马坤（高中）': [2, 3, 4, 5],
                               '张娜': [0, 1, 2, 3, 4],
                               '传廷': [1, 2, 3, 4],
                               '王宇': [1, 2, 3, 4, 5],
                               '常': [2],
                               '文琦': [2],
                               '保发': [0,1,2,5],
                               '杜婷婷': [2],
                               '延蒙': [2],
                               '沈琳琳': [2],
                               '李战胜': [5],
                               '张书冬': [2],
                               '王炜': [2],
                               '郁': [2],
                               '刘佳佳': [0,1,2,3,4],
                               '晓晴': [1,2,3,4],
                               '志硕': [2],
                               '隋欣': [2],
                               '崔': [2],
                               '赵会': [2],
                               "顾立": []}

# 老师惩罚权重（默认为最低10）
teacher_overtime = {
    "沈佳佳": 10,
    "贵强": 10,
    "文琦": 10,
    "保发": 10,
    "段": 10,
    "马坤（高中）": 10,
    "常": 10,
    "传廷": 10,
    "杜婷婷": 10,
    "王宇": 10,
    "顾": 10,
    "延蒙": 10,
    "沈琳琳": 10,
    "于": 10,
    "李战胜": 10,
    "张书冬": 10,
    "王炜": 10,
    "郁": 10,
    "刘佳佳": 10,
    "志硕": 10,
    "随欣": 10,
    "张娜": 10,
    "晓晴": 10,
    "隋欣": 10,
    "崔": 10,
    "赵会": 10,
    "顾立": 10,
}

num_days = 1
max_classes_per_day = 6

while max_classes_per_day < 9:
    # 初始化 CP-SAT 模型
    model = cp_model.CpModel()

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

    # # 添加学生不可上课的软约束
    # for student, unavailable_times in student_unavailable_periods.items():
    #     for day in range(num_days):
    #         for class_num in unavailable_times:
    #             overtime = model.NewIntVar(0, max_classes_per_day, f'overtime_s{student}_d{day}_c{class_num}')
    #             penalties.append(overtime * 10)
    #             # 将overtime变量保存在字典中
    #             overtime_vars[(student, day, class_num)] = overtime
    #             model.Add(overtime >= sum(schedule[f"s{student}_t{teacher}_{subject}_d{day}_c{class_num}"]
    #                                      for teacher in teachers
    #                                      for subject in subjects))

    # 添加老师不可上课的软约束
    for teacher, unavailable_times in teacher_unavailable_periods.items():
        for day in range(num_days):
            for class_num in unavailable_times:
                overtime = model.NewIntVar(0, max_classes_per_day, f'overtime_t{teacher}_d{day}_c{class_num}')
                # model.Add(overtime >= sum(schedule[f"s{student}_t{teacher}_{subject}_d{day}_c{class_num}"]
                #                          for student in students
                #                          for subject in subjects) - 1)
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
        print("*** 以一天 {} 节课排 ***".format(max_classes_per_day))

        print("\n课表：")
        for day in range(num_days):
            print(f"Day {day + 1}:")
            for class_num in range(max_classes_per_day):
                print("第{}节课".format(class_num+1))
                for student in students:
                    for teacher in teachers:
                        for subject in subjects:
                            var_name = f"s{student}_t{teacher}_{subject}_d{day}_c{class_num}"
                            if solver.Value(schedule[var_name]) == 1:
                                print(f"  {student} 跟 {teacher} 上 {subject} 课")
        print("\n教师课表：")
        for day in range(num_days):
            for teacher in teachers:
                print(f"{teacher} 老师：")
                for class_num in range(max_classes_per_day):
                    for student in students:
                        for subject in subjects:
                            var_name = f"s{student}_t{teacher}_{subject}_d{day}_c{class_num}"
                            if solver.Value(schedule[var_name]) == 1:
                                print(f"第 {class_num+1} 给 {student} 上课")

        print("\n学生课表：")
        for day in range(num_days):
            for student in students:
                print(f"{student} 学生：")
                for class_num in range(max_classes_per_day):
                    for teacher in teachers:
                        for subject in subjects:
                            var_name = f"s{student}_t{teacher}_{subject}_d{day}_c{class_num}"
                            if solver.Value(schedule[var_name]) == 1:
                                print(f"第 {class_num+1} 跟 {teacher} 上课")
        
        to_excel()
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
                                db.write_schedule(student, teacher, date, class_num)

        # 输出每个老师的惩罚
        print('\n惩罚详情：')
        for (teacher, day, class_num), overtime_var in overtime_vars.items():
            if solver.Value(overtime_var) > 0:
                print(f'在第{day+1}天的第{class_num+1}节课，老师{teacher}有额外的课需要上，惩罚值为: {solver.Value(overtime_var) * teacher_overtime[teacher]}')
        break
    else:
        max_classes_per_day += 1

if max_classes_per_day >= 9:
    print("没有解决方案")
    db.clear_schedule()
    columns = ["上课时间", "学生", "教师", "科目"]
    df_schedule = pd.DataFrame(columns=columns)
    df_schedule = df_schedule.append(pd.Series([None]*len(columns), index=columns), ignore_index=True)
    with pd.ExcelWriter('schedule.xlsx') as writer:
        df_schedule.to_excel(writer, sheet_name='总课表', index=False)
