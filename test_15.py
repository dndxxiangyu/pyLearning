# 文件读写
# 在磁盘上读写文件的功能都是操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘
# 所以读写文件就是请求操作系统打开一个文件对象，然后通过操作系统提供的接口从这个文件对象中读取数据，或写入数据
try:
    f = open('d:/test.txt', 'r')
    # print(f.read())
finally:
    print(f)
    if f:
        f.close()

# 免去了close
with open('d:/test.txt', 'r') as f:
    for x in f.readlines():
        print(x.strip())

# file-like Object：像open函数返回的这种有个read()方法的对象

f = open('d:/test1.txt', 'w', encoding='utf-8')
f.write("吴向禹")
f.close()

with open("d:/test1.txt", 'r', encoding='utf-8') as f:
    print(f.read())

import os
# 创建文件夹
os.mkdir('d:/text2')
os.mknod('d:/text.txt')