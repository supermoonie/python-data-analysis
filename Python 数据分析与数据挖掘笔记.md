[TOC]

# Python 数据分析与数据挖掘笔记

**numpy 的使用：**

```python
import numpy

# 创建一个一维数组
x = numpy.array(['a', 'b', '1', '2'])
# 创建一个二维数组
y = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 排序
y.sort()
# 取最大值与最小值
y.max()
y.min()
# 切片
x[1:2]
x[1:]
x[1:-1]
```

**pandas 的使用：**

_pandas 为Python 提供了高性能，易于使用的数据机构和数据分析工具_

三个数据结构：

- 系列（Series）：具有均匀数据的一维数组结构
- 数据帧（DataFrame）：具有异构数据的二维数组
- 面板（Panel）：具有异构数据的三维数据结构

```python
import pandas as pda

a = pda.Series([1, 3, 5, 7, 9])
# 指定索引
a = pda.Series([1, 3, 5, 7, 9], index = [1, 2, 3, 4, 5])

b = pda.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = pda.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['one', 'two', 'three'])
b = pda.DataFrame({'one': [1, 2, 3], 'two': [4, 5, 6]})
# one 这一列对应的行的值都为 1 
b = pda.DataFrame({'one': 1, 'two': [5, 6, 6]})
b = pda.DataFrame({'one': [4, 5, 6], 'two': [1, 2, 3], 'three': list(str(789))})
# 取头部数据，默认前五行
b.head()
b.head(2)
# 取尾部数据，默认后五行
b.tail()
b.tail(2)
# describe() 函数用来计算有关DataFrame 列的统计信息的摘要
b.describe()
# 转置
b.T
```

__数据导入：__

```python
import pandas as pda

# 从csv 中读取数据
csv = pda.read_csv('./stock_px.csv')
# 排序
csv.sort_values(by='SPX')
# 从excel 中读取数据
excel = pda.read_excel('./arima_data.xls')
# 从MySql 中读取数据

```

__matplotlib__

```python
import matplotlib.pylab as pyl
import numpy

x = [0, 1, 2, 3, 4, 5]
y = [2, 6, 4, 10, 8, 1]
# plot(x轴数据, y轴数据, 展现形式)
pyl.plot(x, y)
# pyl.plot(x, y, 'o')
'''
颜色：
c-cyan-青色
r-red-红色
m-magente-品红
g-green-绿色
b-blue-蓝色
y-yellow-黄色
k-black-黑色
w-white-白色
'''
'''
线条样式：
- 直线
-- 虚线
-. -.形式
: 细小虚线
'''
'''
点的样式：
s-方形
h-六边形
H-六边形
*-星号
+-加号
x-x型
d-菱形
D-菱形
p-五角形
'''
pyl.title('show')
pyl.xlabel('x-x')
pyl.ylabel('y-y')
pyl.xlim(0, 5)
pyl.ylim(0, 20)
pyl.show()
# 生成随机数
```



