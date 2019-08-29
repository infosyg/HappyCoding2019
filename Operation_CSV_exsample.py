import csv

#首先我们定义一个函数用于读取csv文件
def csv_reader():
    '''写入csv文件'''
    #将下面的内容写入到csv头部信息，
    # 比如  headers = ['编号','课程','讲师']
    headers = ['编号', '课程', '讲师']
    #定义一个变量用来写入csv内容。
    rows = [
        (1, 'python', 'fighter.lu'),
        (2, 'c#', 'fighter.lu'),
        (3, '.net', 'fighter.lu')
    ]
    #下面使用with open as 方法进行csv文件的写入，代码目录下生成csv文件.
    with open('my_course.csv', 'w', encoding='utf-8', newline='')as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    '''
    代码解析：
    1. csv.reader(f)读取的是f对象，也就是读取出来的内容
    2. .writerow(headers)方法是写入头部信息
    3. .writerows(rows)写入所有行内容
    '''

#主函数入口
if __name__ == '__main__':
    csv_reader()

#定义一个函数csv_reader()用来读取csv文件
def csv_writer():
    '''读取csv文件'''
    with open('my_course.csv',encoding='utf-8')as f:
        reader = csv.DictReader(f)#字典表DictReader 列表读取reader
        headers = next(reader)#迭代一次
        print(headers)
        for row in reader:
            print(row)
            #print(row['编号'])

#运行 主函数
if __name__ == '__main__':
    csv_writer()
    csv_reader()

#输出读取的csv结果


