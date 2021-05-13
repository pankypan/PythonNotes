# Python小知识点

## PEP8规范

### 变量

```python
# 常量：大写加下划线
USER_CONSTANT = "a constant"


# 私有变量 : 小写和一个前导下划线
"""
  Python 中不存在私有变量一说，若是遇到需要保护的变量，使用小写和一个前导下划线。但这只是
  程序员之间的一个约定，用于警告说明这是一个私有变量，外部类不要去访问它。但实际上，外部类还
  是可以访问到这个变量。
  """
_private_value = "my private value" 


# 内置变量 : 小写，两个前导下划线和两个后置下划线
"""
  两个前导下划线会导致变量在解释期间被更名。这是为了避免内置变量和其他变量产生冲突。用户
  定义的变量要严格避免这种风格。以免导致混乱
  """
__class__ = "inner value"
```



### 函数和方法

总体而言应该使用，**小写和下划线**。但有些比较老的库使用的是混合大小写，即首单词小写，之后每个单词第一个字母大写，其余小写。但现在，**小写和下划线已成为规范**    

**私有方法 ：小写和一个前导下划线**
这里和私有变量一样，并不是真正的私有访问权限。同时也应该注意一般函数不要使用两个前导下划线(当遇到两个前导下划线时，Python 的名称改编特性将发挥作用)。

**特殊方法 ：小写和两个前导下划线，两个后置下划线**
这种风格只应用于特殊函数，比如操作符重载等。
**函数参数 : 小写和下划线，缺省值等号两边无空格**

```python
def my_function(para_one, para_two):
    pass

class MyTest(object):
    __instance = None  # 私有类属性
    
    def _private_method(self):  # 私有方法
        pass
    
    def __new__(self):  # 特殊方法
        pass
```



### 类

**类总是使用驼峰格式命名**，即所有单词首字母大写其余字母小写。类名应该简明，精确，并足以从中理解类所完成的工作。常见的一个方法是使用表示其类型或者特性的后缀，例如:

`SQLEngine`，`MimeTypes `对于基类而言，可以使用一个 Base 或者 Abstract 前缀` BaseCookie`，`AbstractGroup`



### 模块和包

除特殊模块` __init__ `之外，模块名称都使用不带下划线的小写字母。
若是它们实现一个协议，那么通常使用 lib 为后缀，例如:

```python
import smtplib
import os
import sys
```



### 关于参数

1. 不要用断言来实现静态类型检测。断言可以用于检查参数，但不应仅仅是进行静态类型检测。Python 是动态类型语言，静态类型检测违背了其设计思想。断言应该用于避免函数不被毫无意义的调用。
2. 不要滥用 `*args `和` **kwargs`。`*args` 和` **kwargs` 参数可能会破坏函数的健壮性。它们使签名变得模糊，而且代码常常开始在不应该的地方构建小的参数解析器。



### 其它

```python
#  使用 has 或 is 前缀命名布尔元素
is_connect = True
has_member = False

# 用复数形式命名序列
members = ['user_1', 'user_2']

# 用显式名称命名字典
person_address = {'user_1': '10 road WD', 'user_2': '20 street huafu'}

# 避免通用名称
诸如 list, dict, sequence 或者 element 这样的名称应该避免

# 避免现有名称
诸如 os, sys 这种系统已经存在的名称应该避免
```



### 一些数字

一行列数 : PEP 8 规定为 79 列。根据自己的情况，比如不要超过满屏时编辑器的显示数。
一个函数 : 不要超过 30 行代码, 即可显示在一个屏幕类，可以不使用垂直游标即可看到整函数。
一个类 : 不要超过 200 行代码，不要有超过 10 个方法。一个模块 不要超过 500 行



### 验证脚本

可以安装一个 pep8 脚本用于验证你的代码风格是否符合 PEP8





## Python2与Python3的区别

### 1)核心类差异

1. Python3 对 Unicode 字符的原生支持。
   Python2 中使用 ASCII 码作为默认编码方式导致 string 有两种类型 str 和 unicode，Python3 只
   支持 unicode 的 string。Python2 和 Python3 字节和字符对应关系为：

   | python2 | python3 | 表现 |  转换  | 作用 |
   | :-----: | :-----: | :--: | :----: | :--: |
   |   str   |  bytes  | 字节 | encode | 存储 |
   | unicode |   str   | 字符 | decode | 显示 |

2. Python3 采用的是绝对路径的方式进行 import

3. Python2中存在老式类和新式类的区别，Python3统一采用新式类。新式类声明要求继承object，
   必须用新式类应用多重继承

4. Python3 使用更加严格的缩进。Python2 的缩进机制中，1 个 tab 和 8 个 space 是等价的，所
   以在缩进中可以同时允许 tab 和 space 在代码中共存。这种等价机制会导致部分 IDE 使用存在问题。
   Python3 中 1 个 tab 只能找另外一个 tab 替代，因此 tab 和 space 共存会导致报错：TabError:
   inconsistent use of tabs and spaces in indentation.



### 2)废弃类差异

1. print 语句被 Python3 废弃，统一使用 print 函数

2. exec 语句被 python3 废弃，统一使用 exec 函数

3. execfile 语句被 Python3 废弃，推荐使用 exec(open("./filename").read())

4. 不相等操作符"<>"被 Python3 废弃，统一使用"!="

5. long 整数类型被 Python3 废弃，统一使用 int

6. xrange 函数被 Python3 废弃，统一使用 range，Python3 中 range 的机制也进行修改并提高了大数据集生成效率

7. Python3 中这些方法再不再返回 list 对象：dictionary 关联的 keys()、values()、items()，zip()，map()，filter()，但是可以通过 list 强行转换：

   ```python
   mydict = dict()
   mydict = {"a": 1, "b": 2, "c": 3}
   mydict.keys()  # <built-in method keys of dict object at 0x000000000040B4C8>
   list(mydict.keys())  # ['a', 'c', 'b']
   ```

8. 迭代器 iterator 的 next()函数被 Python3 废弃，统一使用 next(iterator)

9. raw_input 函数被 Python3 废弃，统一使用 input 函数

10. 字典变量的 has_key 函数被 Python 废弃，统一使用 in 关键词

11. file 函数被 Python3 废弃，统一使用 open 来处理文件，可以通过 io.IOBase 检查文件类型

12. apply 函数被 Python3 废弃

13. 异常 StandardError 被 Python3 废弃，统一使用 Exception

</br>

### 3)修改类差异

1. 浮点数除法操作符“/”和“//”的区别
   “ / ”：
   Python2：若为两个整形数进行运算，结果为整形，但若两个数中有一个为浮点数，则结果为
   浮点数；
   Python3:为真除法，运算结果不再根据参加运算的数的类型。
   “//”：
   Python2：返回小于除法运算结果的最大整数；从类型上讲，与"/"运算符返回类型逻辑一致。
   Python3：和 Python2 运算结果一样。
2. 异常抛出和捕捉机制区别

  python2

```python
  raise IOError, "file error"  # 抛出异常
  except NameError, err：  # 捕捉异常
```

  python3

```python
  raise IOError("file error")  #抛出异常
  except NameError as err: #捕捉异常
```

3. for 循环中变量值区别

   Python2，for 循环会修改外部相同名称变量的值

   ```python
   i = 1
   print('comprehension: ', [i for i in range(5)])
   print('after:i = ', i)  # i = 4
   ```

   Python3，for 循环不会修改外部相同名称变量的值

   ```python
   i = 1
   print("comprehension: ", [i for i in range(5)])
   print('after: i = ', i)  # i = 1
   ```

4. round 函数返回值区别

   Python2，round 函数返回 float 类型值

   ```python
   isinstance(round(15.5),int)  #True
   ```

   Python3，round 函数返回 int 类型值

   ```python
   isinstance(round(15.5),float) #True
   ```

5. 比较操作符区别

   Python2 中任意两个对象都可以比较

   ```python
   11 < 'test'  # True
   ```

   Python3 中只有同一数据类型的对象可以比较

   ```python
   11 < 'test' # TypeError: unorderable types: int() < str()
   ```



### 4)第三方工具包差异

我们在pip官方下载源pypi搜索Python2.7和Python3.5的第三方工具包数可以发现，Python2.7
版本对应的第三方工具类目数量是 28523,Python3.5 版本的数量是 12457，这两个版本在第三方工具
包支持数量差距相当大。
我们从数据分析的应用角度列举了常见实用的第三方工具包（如下表），并分析这些工具包在
Python2.7 和 Python3.5 的支持情况：

|   分类   |    工具名     |                用途                 |
| :------: | :-----------: | :---------------------------------: |
| 数据收集 |    scrapy     |           网页采集，爬虫            |
| 数据收集 | scrapy-redis  |             分布式爬虫              |
| 数据收集 |   selenium    |        web 测试，仿真浏览器         |
| 数据处理 | beautifulsoup |    网页解释库，提供 lxml 的支持     |
| 数据处理 |     lxml      |             xml 解释库              |
| 数据处理 |     xlrd      |           excel 文件读取            |
| 数据处理 |     xlwt      |           excel 文件写入            |
| 数据处理 |    xlutils    |       excel 文件简单格式修改        |
| 数据处理 |    pywin32    | excel 文件的读取写入及复杂格式定制  |
| 数据处理 |  Python-docx  |         Word 文件的读取写入         |
| 数据分析 |     numpy     |        基于矩阵的数学计算库         |
| 数据分析 |    pandas     |        基于表格的统计分析库         |
| 数据分析 |     scipy     | 科学计算库，支持高阶抽象和复杂模型  |
| 数据分析 |  statsmodels  |     统计建模和计量经济学工具包      |
| 数据分析 | scikit-learn  |           机器学习工具库            |
| 数据分析 |    gensim     |         自然语言处理工具库          |
| 数据分析 |     jieba     |           中文分词工具库            |
| 数据存储 | MySQL-python  |         mysql 的读写接口库          |
| 数据存储 |  mysqlclient  |         mysql 的读写接口库          |
| 数据存储 |  SQLAlchemy   |          数据库的 ORM 封装          |
| 数据存储 |    pymsql     |        sql server 读写接口库        |
| 数据存储 |     redis     |          redis 的读写接口           |
| 数据存储 |    PyMongo    |         mongodb 的读写接口          |
| 数据呈现 |  matplotlib   |         流行的数据可视化库          |
| 数据呈现 |    seaborn    | 美观的数据可是湖库，基于 matplotlib |
| 工具辅助 |    chardet    |            字符检查工具             |
| 工具辅助 | ConfigParser  |          配置文件读写支持           |
| 工具辅助 |   requests    |        HTTP 库，用于网络访问        |



### 5)工具安装问题

windows 环境
Python2 无法安装 mysqlclient。Python3 无法安装 MySQL-python、 flup、functools32、Gooey、Pywin32 、webencodings。
matplotlib 在 python3 环境中安装报错：The following required packages can not be built:freetype, png。需要手动下载安装源码包安装解决。
scipy 在 Python3 环境中安装报错，numpy.distutils.system_info.NotFoundError，需要自己手工下载对应的安装包，依赖 numpy,pandas 必须严格根据 python 版本、操作系统、64 位与否。运行matplotlib 后发现基础包 numpy+mkl 安装失败，需要自己下载，国内暂无下载源

centos 环境下
Python2 无法安装mysql-python和 mysqlclient包，报错：EnvironmentError: mysql_config not found，解决方案是安装 mysql-devel 包解决。使用 matplotlib 报错：no module named _tkinter，安装 Tkinter、tk-devel、tc-devel 解决。
pywin32 也无法在 centos 环境下安装





## sort 与 sorted 区别：

### sort()

sort()是列表list的方法之一

```python
L.sort(key=None, reverse=False)
```



### sorted()

sorted() 函数可以对任意可迭代对象排序。返回一个列表

sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。

list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的list，而不是在原来的基础上进行的操作

```python
# sorted()语法
sorted(iterable[, cmp[, key[, reverse]]])
```

参数说明：

+ iterable --  可迭代对象
+ cmp --  比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0
+ key --  主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序
+ reverse --  排序规则，reverse = True  降序 ， reverse = False 升序（默认）

#### 单个排序法则：

```python
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
new_students = sorted(students, key=lambda s: s[2])
print(new_students)  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```



#### 多种排序法则：

```python
s = 'asdf234GDSdsf234578'  # 排序：小写-大写-奇数-偶数
new_s1 = "".join(sorted(s, key=lambda x: [x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x]))
print(new_s1)  # addffssDGS335722448
```

原理：

```python
print(sorted([True, False]))  # [False, True]
# Boolean 的排序会将 False 排在前，True排在后  
```

1. x.isdigit()的作用把iterable分成两部分，数字和非数字，数字在后，非数字在前

   ```python
   new_s1 = "".join(sorted(s, key=lambda x: [x.isdigit()]))
   print(new_s1)  # asdfGDSdsf234234578
   ```

2. x.isdigit() and int(x) % 2 == 0的作用是将数字部分分成两部分，偶数（在后）和奇数（在前）

   ```python
   new_s1 = "".join(sorted(s, key=lambda x: [x.isdigit(), x.isdigit() and int(x) % 2 == 0]))
   print(new_s1)  # asdfGDSdsf335724248
   ```

3. x.isupper()的作用是在前面基础上,保证字母小写在前大写在后

   ```python
   new_s1 = "".join(sorted(s, key=lambda x: [x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper()]))
   print(new_s1)  # asdfdsfGDS335724248
   ```

4. 最后的x表示在前面基础上,对所有类别数字或字母排序

   ```python
   new_s1 = "".join(sorted(s, key=lambda x: [x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x]))
   print(new_s1)  # addffssDGS335722448
   ```



### 面试题

lst = [7, -8, 5, 4, 0, -2, -5]

要求:

1. 正数在前负数在后
2. 正数从小到大
3. 负数从大到小

```python
lst = [7, -8, 5, 4, 0, -2, -5]
new_lst1 = sorted(lst, key=lambda x: [x < 0, x < 0 and -x, x >= 0 and x])  # -3 < 0 and -(-3) ==> 3
new_lst2 = sorted(lst, key=lambda x: [x < 0, abs(x)])
print(new_lst1)  # [0, 4, 5, 7, -2, -5, -8]
print(new_lst2)  # [0, 4, 5, 7, -2, -5, -8]
```



## python变量与地址的关系

在C语言中，系统会为每个变量分配内存空间，当改变变量的值时，改变的是内存空间中的值，变量的地址是不改变的。

而在python中，Python采用的是基于值的管理方式。

当给变量赋值时，系统会为这个值分配内存空间，然后让这个变量指向这个值；当改变变量的值时，系统会为这个新的值分配另一个内存空间，然后还是让这个变量指向这个新值。

也就是说，<mark>**C语言中变量变的是内存空间中的值，不变的是地址；而在Python中，变量变的是地址，不变的是内存空间中的值**。</mark>

```python
x = 12
print(x)

x = 3.14
print(x)
```

同时，如果没有任何变量指向内存空间的某个值，这个值称为垃圾数据，系统会自动将其删除，回收它占用的内存空间。

同时，如果没有任何变量指向内存空间的某个值，这个值称为垃圾数据，系统会自动将其删除，回收它占用的内存空间。

另外，我们可以使用python的id()函数来查看变量的内存地址。

```python
a = 2.0
b = 2.0
pirnt(id(a))  # 2658670250000
pirnt(id(b))  # 2658670249968

a = 2
b = 2
print(id(a))  # 140725523280176
print(id(b))  # 140725523280176
```

我们看到，当a,b都是2.0时，它们的地址不一样，说明系统为a,b分配了不同的内存空间。但是，当a,b都是2时，它们的地址是一样的，怎么回事呢？这是因为，为了提高内存空间的利用效率，对于一些比较小的整型变量(int)使用了相同的内存空间。如果数值比较大，地址就不一样了。

```python
a = 2
b = 2
print(id(a))  # 140725523280176
print(id(b))  # 140725523280176

a = 222
b = 222
print(id(a))  # 140725523287216
print(id(b))  # 140725523287216

a = 2222
b = 2222
print(id(a))  # 2658670249520
print(id(b))  # 2658670249776
```





## Python赋值、深浅copy

### assignment

<mark>在 Python 中，对象的赋值就是简单的对象引用</mark>，这点和 C++不同，如下所示

```python
a = [1, 2, 'hello', ['python', 'C++']]
b = a
a[0] = 'abc'
print(b)

a = b = 3
a =345
print(b)
```

在上述情况下，a 和 b 是一样的，他们指向同一片内存，b 不过是 a 的别名，是引用.
我们可以使用 `b is a` 去判断，返回 `True`，表明他们地址相同，内容相同，也可以使用` id()`函数来查看两个列表的地址是否相同。
**赋值操作(包括对象作为参数、返回值)不会开辟新的内存空间，它只是复制了对象的引用**。



### shallow copy

<mark>浅拷贝会**创建新对象**，其内容非原对象本身的引用，而是原对象内**第一层对象**的**引用**。</mark>

浅拷贝有三种形式:

+ 切片操作

  ```python
  b = a[:]
  c = [x for x in a]
  ```

+ 工厂函数

  ```python
  b = list(a)
  ```

+ copy 模块中的 copy 函数

  ```python
  b = copy.copy(a)
  ```

  

​	浅拷贝产生的列表 b 不再是列表 a 了，使用 is 判断可以发现他们不是同一个对象，使用 id 查看，他们也不指向同一片内存空间。但是当我们使用 `id(x) for x in a 和 id(x) for x in b` 来查看 `a 和 b `中元素的地址时，可以看到二者包含的元素的地址是相同的。
​	在这种情况下，列表 a 和 b 是不同的对象，修改列表 b 理论上不会影响到列表 a。但是要注意的是，<mark>浅拷贝之所以称之为浅拷贝，是它仅仅只拷贝了一层，在列表 a 中有一个嵌套的list，如果我们修改了它，情况就不一样了</mark>。
​	比如：`a[3].append('java')`。查看列表 b，会发现列表 b 也发生了变化，这是因为，我们修改了嵌套的 `list`，修改外层元素，会修改它的引用，让它们指向别的位置，修改嵌套列表中的元素，列表的地址并未发生变化，指向的都是用一个位置。

```python
import copy

a = [1, 2, 3, ['a', 'b', 'c']]
b = copy.copy(a)
a[0] = 'change'
print('a:', a)
print('b:', b)

a[-1][1] = 'abc'
print('a:', a)
print('b:', b)
```



### deep copy

深拷贝只有一种形式，**copy 模块中的 deepcopy()函数**。
深拷贝和浅拷贝对应，<mark>深拷贝拷贝了对象的所有元素，包括多层嵌套的元素</mark>。因此，它的时间和空间开销要高。
同样的对列表 a，如果使用 b = copy.deepcopy(a)，再修改列表 b 将不会影响到列表 a，即使嵌套的列表具有更深的层次，也不会产生任何影响，因为<mark>深拷贝拷贝出来的对象根本就是一个全新的对象，不再与原来的对象有任何的关联</mark>



### 拷贝注意点

对于非容器类型，如数字、字符，以及其他的**“原子”类型**，没有拷贝一说，**产生的都是原对象的引用**。
如果元组变量值包含原子类型对象，即使采用了深拷贝，也只能得到浅拷贝。



### 面试题

```python
import copy
a = [1, 2, 3, [4, 5], 6]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
b.append(10)
c[3].append(11)
d[3].append(12)
print(a, b, c, d, sep='\n')
"""
[1, 2, 3, [4, 5, 11], 6, 10]
[1, 2, 3, [4, 5, 11], 6, 10]
[1, 2, 3, [4, 5, 11], 6]
[1, 2, 3, [4, 5, 12], 6]
"""
```

