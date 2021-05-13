# Python反射

对编程语言比较熟悉的朋友，应该知道“反射”这个机制。Python作为一门动态语言，当然不会缺少这一重要功能。然而，在网络上却很少见到有详细或者深刻的剖析论文。下面结合一个web路由的实例来阐述python的反射机制的使用场景和核心本质

+ `hasattr()`
+ `getattr()`
+ `setattr()`
+ `delattr()`

## 引子

```python
def f1():
    print("This is function 1")
    
   
s = 'f1'
print("%s is a string" % s)
```

在上面的代码中，我们必须区分两个概念，f1和“f1"。前者是函数f1的函数名，后者只是一个叫”f1“的字符串，两者是不同的事物。我们可以用f1()的方式调用函数f1，但我们不能用"f1"()的方式调用函数。说白了就是，**不能通过字符串来调用名字看起来相同的函数！**

</br>

## web实例

考虑有这么一个场景，根据用户输入的url的不同，调用不同的函数，实现不同的操作，也就是一个url路由器的功能，这在web框架里是核心部件之一。下面有一个精简版的示例：

首先，有一个commons模块，它里面有几个函数，分别用于展示不同的页面，代码如下：

`commons.py`

```python
def login():
    print("This is a login html")
    
   
def logout():
    print("This is a logout html")
    
    
def home():
    print("This is home html")
```

其次，有一个visit模块，作为程序入口，接受用户输入，展示相应的页面，代码如下：（这段代码是比较初级的写法）

`visit.py`

```python
import commons


def run():
    inp = input("请输入您想访问的url: ").strip()
    if inp == "login":
        commons.login()
    elif inp == "logout":
        commons.logout()
    elif inp == "home":
        commons.home()
    else:
        print("404")
        
        
if __name__ == "__main__":
    run()
```

我们运行visit.py，输入：home，页面结果如下：

```python
# 请输入您想访问的url: home
# This is home html
```

这就实现了一个简单的WEB路由功能，根据不同的url，执行不同的函数，获得不同的页面。

然而，让我们考虑一个问题，如果commons模块里有成百上千个函数呢(这非常正常)?。难道你在visit模块里写上成百上千个elif?显然这是不可能的！那么怎么破？

</br>

## 反射机制

仔细观察visit中的代码，我们会发现用户输入的url字符串和相应调用的函数名好像！如果能用这个字符串直接调用函数就好了！但是，前面我们已经说了字符串是不能用来调用函数的。为了解决这个问题，python为我们提供一个强大的内置函数：**getattr**我们将前面的visit修改一下，代码如下：

```python
import commons


def run():
    inp = input("请输入您想访问的url： ")
    func = getattr(commons, inp)
    

if __name__ == "__main__":
    run()
```

首先说明一下getattr函数的使用方法：它接收2个参数，前面的是**一个对象或者模块**，后面的是**一个字符串**，**注意了！是个字符串！**

例子中，用户输入储存在`inp`中，这个`inp`就是个字符串，`getattr`函数让程序去`commons`这个模块里，寻找一个叫`inp`的成员（是叫，不是等于），这个过程就相当于我们把一个字符串变成一个函数名的过程。然后，把获得的结果赋值给`func`这个变量，实际上`func`就指向了`commons`里的某个函数。最后通过调用`func`函数，实现对`commons`里函数的调用。这完全就是一个动态访问的过程，一切都不写死，全部根据用户输入来变化。

执行上面的代码，结果和最开始的是一样的。

## 进一步完善

上面的代码还有个小瑕疵，那就是如果用户输入一个非法的url，比如jpg，由于在commons里没有同名的函数，肯定会产生运行错误，具体如下：

```python
请输入您想访问页面的url：  jpg
Traceback (most recent call last):
  File "F:/Python/pycharm/s13/reflect/visit.py", line 16, in <module>
    run()
  File "F:/Python/pycharm/s13/reflect/visit.py", line 11, in run
    func = getattr(commons,inp)
AttributeError: module 'commons' has no attribute 'jpg'
```

那怎么办呢？其实，python考虑的很全面了，它同样提供了一个叫hasattr的内置函数，用于判断commons中是否具有某个成员。我们将代码修改一下：

```python
import commons
 
def run():
    inp = input("请输入您想访问页面的url：  ").strip()
    if hasattr(commons,inp):
        func = getattr(commons,inp)
        func()
    else:
        print("404")
 
if __name__ == '__main__':
    run()
```

通过`hasattr`的判断，可以防止非法输入错误，并将其统一定位到错误页面。

其实，研究过python内置函数的朋友，应该注意到还有`delattr`和`setattr`两个内置函数。从字面上已经很好理解他们的作用了。

python的四个重要内置函数：`getattr、hasattr、delattr和setattr`较为全面的实现了基于字符串的反射机制。<mark>他们都是对内存内的模块进行操作，并不会对源文件进行修改。</mark>

## 动态导入模块

上面的例子是在某个特定的目录结构下才能正常实现的，也就是commons和visit模块在同一目录下，并且所有的页面处理函数都在commons模块内。如下图：

![948404-20160611234648715-2037989511](assets/948404-20160611234648715-2037989511.png)

但在现实使用环境中，页面处理函数往往被分类放置在不同目录的不同模块中，也就是如下图：

![948404-20160611235720511-1977401480](assets/948404-20160611235720511-1977401480.png)



难道我们要在visit模块里写上一大堆的import 语句逐个导入account、manage、commons模块吗？要是有1000个这种模块呢？

刚才我们分析完了基于字符串的反射，实现了动态的函数调用功能，我们不禁会想那么能不能动态导入模块呢？这完全是可以的！

**python提供了一个特殊的方法：__import__(字符串参数)。通过它，我们就可以实现类似的反射功能。__import__()方法会根据参数，动态的导入同名的模块。**

我们再修改一下上面的visit模块的代码。

```python
def run():
    inp = input("请输入您想访问页面的url：  ").strip()
    modules, func = inp.split("/")
    obj = __import__(modules)
    if hasattr(obj, func):
        func = getattr(obj, func)
        func()
    else:
        print("404")
 
if __name__ == '__main__':
    run()
```

运行一下：

```python
请输入您想访问页面的url：  commons/home
这是网站主页面！
 
请输入您想访问页面的url：  account/find
这是一个查找功能页面！
```

我们来分析一下上面的代码：

首先，我们并没有定义任何一行import语句；

其次，用户的输入inp被要求为类似“commons/home”这种格式，其实也就是模拟web框架里的url地址，斜杠左边指向模块名，右边指向模块中的成员名。

然后，modules,func = inp.split("/")处理了用户输入，使我们获得的2个字符串，并分别保存在modules和func变量里。

接下来，最关键的是obj = __import__(modules)这一行，它让程序去导入了modules这个变量保存的字符串同名的模块，并将它赋值给obj变量。

最后的调用中，getattr去modules模块中调用func成员的含义和以前是一样的。

总结：通过__import__函数，我们实现了基于字符串的动态的模块导入。

同样的，这里也有个小瑕疵！

如果我们的目录结构是这样的：

![948404-20160612002138605-2025008087](assets/948404-20160612002138605-2025008087.png)

那么在visit的模块调用语句中，必须进行修改，我们想当然地会这么做：

```python
def run():
    inp = input("请输入您想访问页面的url：  ").strip()
    modules, func = inp.split("/")
    obj = __import__("lib." + modules)      #注意字符串的拼接
    if hasattr(obj, func):
        func = getattr(obj, func)
        func()
    else:
        print("404")
 
if __name__ == '__main__':
    run()
```

改了这么一个地方:obj = __import__("lib." + modules)，看起来似乎没什么问题，和import lib.commons的传统方法类似，但实际上运行的时候会有错误。

```python
请输入您想访问页面的url：  commons/home
404
 
请输入您想访问页面的url：  account/find
404
```

为什么呢？因为**对于lib.xxx.xxx.xxx这一类的模块导入路径，__import__默认只会导入最开头的圆点左边的目录**，也就是“lib”。我们可以做个测试，在visit同级目录内新建一个文件，代码如下：

```python
obj = __import__("lib.commons")
print(obj)
```

执行结果：

```python
<module 'lib' (namespace)>
```

这个问题怎么解决呢？加上`fromlist = True`参数即可！

```python
def run():
    inp = input("请输入您想访问页面的url：  ").strip()
    modules, func = inp.split("/")
    obj = __import__("lib." + modules, fromlist=True)  # 注意fromlist参数
    if hasattr(obj, func):
        func = getattr(obj, func)
        func()
    else:
        print("404")
 
if __name__ == '__main__':
    run()
```

至此，**动态导入模块**的问题基本都解决了，只剩下最后一个，那就是万一用户输入错误的模块名呢？比如用户输入了`somemodules/find`，由于实际上不存在`somemodules`这个模块，必然会报错！那有没有类似上面`hasattr`内置函数这么个功能呢？答案是没有！碰到这种，你只能通过**异常处理**来解决。

</br>

## 总结

可能有人会问python不是有两个内置函数`exec`和`eval`吗？他们同样能够执行字符串。比如：

```python
exec("print('haha')")
 
结果：
 
haha
```

那么直接使用它们不行吗？非要那么费劲地使用`getattr，__import__`干嘛？

其实，在上面的例子中，围绕的核心主题是如何**利用字符串驱动不同的事件，比如导入模块、调用函数等等**，这些都是**python的反射机制，是一种编程方法、设计模式的体现，凝聚了高内聚、松耦合的编程思想**，不能简单的用执行字符串来代替。当然，`exec`和`eval`也有它的舞台，在web框架里也经常被使用。









