print('=' * 20, '欢迎使用员工管理系统', '=' * 20)
print('请选择要做的操作：')
print('\t1.查询员工')
print('\t2.添加员工')
print('\t3.删除员工')
print('\t4.退出系统')
list = ['猴哥\t23\t男\t花果山', '猪八戒\t28\t男\t高老庄']
while True:  # 因为要反复出现
    x = input('请选择(1-4):')
    if x == '1':
        print('序号\t姓名\t年龄\t性别\t住址')
        i = 1
        for emp in list:
            print(i, '\t', emp)
            i += 1
    elif x == '2':
        t1 = input('请输入员工姓名：')
        t2 = input('请输入员工年龄：')
        t3 = input('请输入员工性别：')
        t4 = input('请输入员工地址：')
        string = t1 + '\t' + t2 + '\t' + t3 + '\t' + t4
        print('以下信息将被添加到数据库中：', string)
        cv = input('确认添加?Y/N?')
        if cv == 'Y':
            list.append(string)
            print('成功添加新员工', t1, '信息')
        else:
            print('未添加新员工信息')

    elif x == '3':
        r1 = input('请输入待删除的员工编号：')
        r2 = int(r1) - 1
        list.pop(r2)
    elif x == '4':
        break
print('-' * 60)
