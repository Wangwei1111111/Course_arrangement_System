# Course_arrangement_System
based on Google Ortools CP-SAT, for solving the scheduling problem of a tutoring institution. Python3.7  
</br>
[CP-SAT求解器](https://developers.google.cn/optimization/cp/cp_solver?hl=zh-cn)  
</br>
**解决问题**：为一个补习机构的一对一课程写自动排课  
**约束**：一天六节课；学生-教师-科目对应关系；学生不能上课时间；教师不能上课时间（软）；某些学生要指定上课时间；某些学生一天要上两次同一个老师的课。  
</br>
**cas文件夹**中是JY用PYQT写的学生管理，用于对数据库进行学生教师课程信息的增删改查。  
</br>
**database_queries.py**定义了连接操作数据库的方法  
</br>
</br>
自动排课使用CP-SAT求解器，输入各种约束来进行自动排课。</br>
其中教师不能上课时间为软约束，模型可能会在某个教师不能上课时间为其安排课程并加入惩罚，模型会找到能满足所有约束条件且惩罚达到最小的解决方案。</br>
由于补习机构要求过于奇葩，约束太多，不是人排的（他们自己人工每天排课要排3h+），所以加入一个循环，当每天上6节课排不出来时，会增加到7节课，最大为9。</br>
最终会在输出的excel文件中用*标注出不在约束时间内的课程计划。</br>
</br>
由于自动排课程序和JY写的pyqt产生冲突，找不出bug出现在哪，于是把两个文件分开打包。  
config.ini没用，直接把数据库配置写在程序里了。打包使用pyinstaller。
