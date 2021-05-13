# python的unittest使用

## unittest介绍

`unittest`是python内置的**单元测试框架**，具备**编写用例**、**组织用例**、**执行用例**、**输出报告**等自动化框架的条件。

**使用unittest前需要了解该框架的五个概念:**

- `test case`

  ```python
  """
  一个完整的测试单元，执行该测试单元可以完成对某一个问题的验证
  完整体现在：
  	测试前环境准备(setUp)
  	执行测试代码(run)
  	测试后环境还原(tearDown)
  """
  ```

- `test suite`

  ```python
  """
  多个测试用例的集合，测试套件或测试计划；
  """
  ```

- `testLoader`

  ```python
  """
  加载TestCase到TestSuite中的，其中loadTestsFrom__()方法用于寻找TestCase，
  并创建它们的实例，然后添加到TestSuite中，返回TestSuite实例；
  """
  ```

- `test runner`

  ```python
  """
  执行测试用例，并将测试结果保存到TextTestResult实例中，包括运行了多少测试用例，
  成功了多少，失败了多少等信息
  """
  ```

- `test fixture`

  ```python
  """
  一个测试用例的初始化准备及环境还原，主要是setUp() 和 setDown()方法
  """
  ```





## unittest工作原理

**通过unittest类调用分析，可将框架的工作流程概况如下：**

1. 编写TestCase
2. 由TestLoader加载TestCase到TestSuite
3. 然后由TextTestRunner来运行TestSuite
4. 最后将运行的结果保存在TextTestResult中





## 使用案例

### 待测模块myfunc

`myfunc.py`

```python
def is_prime(number):
    if number < 0 or number in (0, 1):
        return False
    for element in range(2, number):
        if number % element == 0:
            return False
    return True


def add(a, b):
    return a + b


def divide(a, b):
    return a / b
```



### unittest编写测试用例

使用`unittest`对`myfunc`进行单元测试，

- 首先需要导入`unittest`框架和待测模块`myfunc`，
- 定义的测试用例方法类需要继承`unittest.TestCase`
- 测试用例方法是以`test`开头作为标识，
- 用例的执行结果以`assetxxx`断言结果决定，如果断言返回为false，将抛出assetError异常。

`test_myfunc_1.py`

```python
import unittest
from myfunc import is_prime, add, divide


class TestMyFunc(unittest.TestCase):
    def setUp(self):
        print('每个测试用例执行前都会调用setUp方法准备环境')

    def tearDown(self):
        print('每个测试用例执行后都会调用tearDown方法进行环境清理')

    def test_is_prime(self):
        print('is_prime')
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-3))

    def test_add(self):
        print('add')
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_divide(self):
        print('divide')
        self.assertEqual(2, divide(6, 3))
        self.assertNotEqual(2, divide(5, 2))


if __name__ == '__main__':
    unittest.main()
```



### 框架如何解决自动化需求的4个问题

- 如何控制顺序
- 如何多个用例共用setUp、tearDown
- 如何跳过用例
- 如何生成html格式的测试报告



#### 如何控制顺序

在`unittest`中，用例是以`test`开头的方法定义的，**默认执行顺序是根据用例名称升序进行**，如上面的用例，
实际执行顺序为：`test_add-->test_divide-->test_is_prime`,而不是用例定义的先后顺序。

在`unittest`中解决**用例执行顺序**的问题是**使用TestSuite**，代码如下：

```python
if __name__ == '__main__':
    # 1 使用TestSuite控制用例顺序，用例的执行顺序是由添加到TestSuite的顺序决定的
    tests = [TestMyFunc('test_is_prime'), TestMyFunc('test_add'), TestMyFunc('test_divide')]

    suite = unittest.TestSuite()
    suite.addTests(tests)  # 将测试用例增加到测试套件

    runner = unittest.TextTestRunner()
    runner.run(suite)
```



#### 如何让多个用例共用setUp、tearDown

unittest的setup、teardown会在每个用例执行前后执行一次，如上面测试用例类中有3个测试用例，那么每个用例执行前会执行setup，执行后会执行teardown，即setup、teardown总共会调用三次，但考虑实际自动化测试场景，多个用例只需执行一次setup，全部用例执行完成后，执行一次teardown，针对该种场景，`unittest`的处理方法是使用`setupclass、teardownclass`，注意`@classmethod`的使用，
如下：

```python
class TestMyFunc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('在所有测试用例执行前会调用setUpClass方法准备环境')

    @classmethod
    def tearDownClass(cls):
        print('在所有测试用例执行完毕后会调用tearDownClass方法进行环境清理')
```



#### 如何跳过用例

在自动化测试中，经常会遇到挑选用例的情况，在`unittest`中的解决方法**是使用`skip装饰器`，**其中`skip装饰器`主要有3种：

- `unittest.skip(reason)`
- `unittest.skipIf(condition,reason)`
- `unittest.skipUnless(condition,reason)`即在满足condition条件下跳过该用例，reason用于描述跳过的原因

实例代码如下：

```python
import unittest
import sys

from myfunc import is_prime, add, divide


class TestMyFunc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('在所有测试用例执行前会调用setUpClass方法准备环境')

    @classmethod
    def tearDownClass(cls):
        print('在所有测试用例执行完毕后会调用tearDownClass方法进行环境清理')

    def test_is_prime(self):
    	...

    def test_add(self):
        ...

    @unittest.skipUnless(sys.platform.startswith('linux'), 'requires Linux')
    def test_divide(self):
        print('divide')
        self.assertEqual(2, divide(6, 3))
        self.assertNotEqual(2, divide(5, 2))
```



#### 如何生成html格式的测试报告

Unittest中默认生成的报告格式为txt，如果想生成html格式的报告，可以使用HtmlTestRunner模块，
安装后导入该模块，使用HTMLTestRunner代替默认的TextTestRunner()执行测试用例即可。实例代码如下：









































