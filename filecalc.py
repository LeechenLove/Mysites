import psutil
import os
import datetime

'''
1.远程目标服务器
2.查看C盘大小和使用率
3.使用率大于某个值，遍历C盘查找并删除90天前且后缀名为.log的文件
:return:清理磁盘log文件
'''



# p1 = psutil.disk_usage(d[1][0])
# print(p1)


file_log = ".log1"
delay_time = datetime.timedelta(days=0)   #指定多少天前
now_time = datetime.datetime.now()
path = 'D:\\test'

def find_log(dir_path):
    dir_files = os.listdir(dir_path)  # 得到该文件夹下所有的文件
    for file in dir_files:
        file_path = os.path.join(dir_path, file)# 路径拼接成绝对路径
        if os.path.isfile(file_path) and file_path.endswith(file_log):
            create_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
            if create_time < (now_time - delay_time):
                # print(create_time)
                print(file_path)
                os.remove(file_path)
        if os.path.isdir(file_path):  # 如果目录，就递归子目录
            find_log(file_path)

if __name__ == '__main__':

    d = psutil.disk_partitions()
    find_log(path)
    # for x in range(len(d)):
    #     disk_dir = d[x].device
    #     disk_used = psutil.disk_usage(d[x][0])
    #     print(disk_dir.split(':')[0] + "盘大小(G)", disk_used.total / 1024 / 1024 / 1024)
    #
    #     if disk_used.percent > 40:
    #         print(disk_dir.split(':')[0])
    #         find_log(disk_dir)

