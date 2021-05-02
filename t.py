#
import json

# a = [i for i in range(0, 5)]
data = {
    'name':"sam"
}
jstr = json.dumps(data)

print(jstr)
data_json = json.loads(jstr)





print(data_json['name'])
with open("humidity.txt", "r") as f:
    result = json.load(f) #从文件中读取json字符串然后转换成python对象
    print(result['temperature'][0]) #输出{"name":"test"}
#
# data_reload = json.load(jstr)
# print(data_reload)

# filename = "data.json"
# with open(filename, 'w') as file_obj:
#     json.dump(data, file_obj)
# with open(filename, 'r') as file_obj:
#     jstr = json.load(file_obj)
#     print(jstr)
# import os
#
# print(os.getcwd())
# filenames = os.listdir()
# def str_num(string):
#     vec = string.split()
#     for i in range(len(vec)):
#         vec[i] = int(vec[i])
#     print(vec)
#     return vec
#
# for fname in filenames:
#     col_cnt = 0
#     with open(fname, 'r') as f:
#         lines = f.readlines()
#         print(fname, f.readlines())
#         line_cnt = 0
#
#         for l in lines:
#             l = l[0:-1]  # cut the \n
#             print(l, end='')
#             if not l.strip() == "":  # avoid empty line
#                 line_cnt += 1
#                 col_cnt = max(str_num(l))
#
#         print("line cnt = ", line_cnt)
#         print("col_cnt = ",col_cnt)
#
#
#
#








