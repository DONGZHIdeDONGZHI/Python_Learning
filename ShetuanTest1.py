'''
1．环境题：在个人电脑上安装 Python 解释器，并安装 PyCharm 或 VS Code（二选一）。
在终端中查看 Python 版本和解释器路径，新建并运行 hello.py。说明“.py 文件”“Python 解
释器”和“PyCharm 或 VS Code”分别有什么作用。'''

#查看python版本：win+r
#解释器路径：下方黄色部分  D:\Anaconda3download\envs\pylearn\python.exe
#1. .py 文件：Python 源代码文件，纯文本，需由解释器读取执行；后缀让编辑器和系统识别类型，提供高亮、补全等支持。
#2. Python 解释器：真正执行代码的程序，负责解析语法、生成字节码并运行，同时管理模块导入和内存。不同环境/版本的解释器，可用库和结果可能不同。
#3. VS Code：代码编辑器或 IDE，本身不执行代码，运行仍依赖配置的解释器；提供编辑、补全、调试、终端集成和虚拟环境管理等功能。

#Python 代码阅读
'''temperatures = [24.5, 27.0, 30.5, 29.0, 32.0]
high_count = 0
for value in temperatures:
    if value >= 30:
        high_count += 1
print(max(temperatures))    #32.0
print(sum(temperatures) / len(temperatures))    #28.6
print(high_count)   #2
'''

#说明 for、if、max、sum、len 分别完成了什么工作。
#1.for : 遍历列表里面的数字，把每个温度值给value
#2.if : 条件判断，满足条件时候执行缩进的代码块
#3.max : 内置函数，返回温度中的最大值
#4.min : 内置函数，返回温度中的最小值
#5.len : 内置函数，返回温度列表中数据的总数有几个，求平均数要作除数

#Python 调试题
'''n = input("请输入一个正整数：")  #input默认返回字符串，要强制改成int才能被用在range里面，range需要整数参数
total = 0
for i in range(1, n):   #范围不对，这么写取到的实际上只有1，2，3……n-1，原因是左闭右开，改成n+1
    total += i
print("1 到 n 的和为：", total)'''

#改正以后的：
'''
# 1. 获取输入并强制转换为整数
n = int(input("请输入一个正整数: "))

total = 0

# 2. range 范围改为 n+1，确保包含 n
for i in range(1, n + 1):
    total += i

print("1 到 n 的和为: ",total)  #也可以改成print(f"1 到 {n} 的和为: {total}")，类似C中的操作
'''

#4．函数题：编写函数 classify_temperature(value)。value<10 返回“偏低”，10≤value<30 
#返回“正常”，value≥30 返回“偏高”。至少用 3 组输入测试它。
'''
def classify_temperature(temp):
    if temp < 0:
        return "寒冷"
    elif temp < 15:
        return "凉爽"
    elif temp < 25:
        return "温暖"
    else:
        return "炎热"

print(classify_temperature(-5))   # 寒冷
print(classify_temperature(10))   # 凉爽
print(classify_temperature(20))   # 温暖
print(classify_temperature(30))   # 炎热
'''

#5．虚拟环境题：安装 Anaconda 并创建一个新的 Python 虚拟环境，在环境中安装 NumPy
#和 pandas。使用 PyCharm 或 VS Code 建立一个新项目，并为该项目选择刚刚创建的虚
#拟环境。记录创建过程和成功运行程序的截图。已经熟悉 Miniforge 或 uv 的同学可以继续
#使用原有工具，零基础同学直接使用 Anaconda 即可。

#已经创建完成，使用Anaconda，并成功安装NumPy和pandas，该文件即在虚拟环境中运行