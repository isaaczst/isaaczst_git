---
title: ocr
---

##
## 100行Python代码实现一款高精度免费OCR工具 - Jackpop的文章 - 知乎
### https://zhuanlan.zhihu.com/p/145449299
## 100行Python代码实现一款高精度免费OCR工具
Jackpop
哈尔滨工业大学 计算数学硕士​
## 近期Github开源了一款基于Python开发、名为Textshot的截图工具，刚开源不到半个月已经500+Star。
这两天抽空看了一下Textshot的源码，的确是一个值得介绍的项目。
相对于大多数OCR工具复杂工程、差强人意的效果，Textshot具有明显的优势， 项目简单 技术点丰富
## 项目简单
### Textshot整个项目只有1个Python文件、139行代码，没有复杂的第三方库应用，也不涉及过多后端算法的调用。
## 技术点丰富
### Textshot这个项目虽然只有短短的139行代码，但是，却涉及Python中多个方面的知识应用，
### UI开发
### 截图工具开发
### 后端引擎调用
### 通过这短短的项目，你不仅可以了解如何利用PyQt5实现一个用户界面，还可以学会如何使用pyscreenshot开发一款自己的截图工具。此外，还能够学会后端tesseract的调用。
### 换句话说，这短短的139行代码囊括了前端至后端的整个流程，而且涉及到截图和OCR两款工具的衔接。因此，Textshot虽然工程不大，却是一个非常完备、值得学习的项目。
## 本文就来剖析这个项目的源代码，教你一步一步实现自用且永久免费的截图&OCR工具！
## tesseract
### 目前OCR工具数不胜数，但是大多数都是在相同的后端算法上面进行了不同的封装而已。而真正在OCR核心做的较好、值得大书特书的，那么一定非tesseract莫属。
### tesseract早在1985就已经开始由HP实验室开始研发，而在1995年更是被评为最为准确的3款OCR工具之一。此后，tesseract被开源，经过Google对其不断的进行优化和升级，它目前已经成为OCR方面一款标杆性的工具。很多开源或者付费的OCR工具，都是直接调用tesseract或者对其进行稍许优化。
### 而今天介绍的Textshot就是直接调用tesseract后端引擎进行OCR识别。因此，Textshot只是实现了一款截图工具，起到前后端的串联作用，在OCR识别算法方面并没有做任何工作。
## tesseract安装
### 由于Textshot的OCR识别需要调用tesseract后端引擎，所以，首先需要安装tesseract。
### Windows版安装可以直接访问下载链接[1].
### Mac下可以使用Homebrew进行安装，
#### brew install tesseract
## Textshot
### Textshot是一款截图识别文字的OCR工具，因此，它主要涉及2个环境，截图，OCR识别
### Textshot首先通过截图获取需要进行文字识别的图像，然后对这副图像进行OCR文字识别，输出识别结果。
### 前面已经介绍了，Textshot的OCR识别阶段调用的是tesseract，所以只需要1行代码即可完成。
### 因此，Textshot的工作主要是围绕前端窗口和截图工具的实现方面。
## 截图工具
### 截图工具是我们经常会用到的一种工具，如何实现一款截图工具？
### 很多人会把它想的非常复杂，其实，Python中有很多可以实现截图的库或者函数，例如，pyscreenshot或者pillow中的ImageGrab函数，它的调用方式如下，
### shot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
### 也就是说，我们只需要把鼠标框选的起点和终点坐标传给grab方法就可以实现截图功能。
### 那么，现在问题就转化为如何获取鼠标框选的起点和终点？
### Textshot通过调用PyQt5并继承QWidget来实现鼠标框选过程中的一些方法来获取框选的起点和终点。
### Textshot继承和重写QWidget方法主要包括如下几个，
### keyPressEvent(self, event)：键盘响应函数
### paintEvent(self, event)：UI绘制函数
### mousePressEvent(self, event)：鼠标点击事件
### mouseMoveEvent(self, event)：鼠标移动事件
### mouseReleaseEvent(self, event)：鼠标释放事件
### 可以看出，上面重写的方法以及囊括了截图过程中涉及的各个动作，点击鼠标，拖动、绘制截图框，释放鼠标
#### class Snipper(QtWidgets.QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        self.setWindowTitle("TextShot")
        self.setWindowFlags(
            Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Dialog
        )

        self.is_macos = sys.platform.startswith("darwin")
        if self.is_macos:
            self.setWindowState(self.windowState() | Qt.WindowMaximized)
        else:
            self.setWindowState(self.windowState() | Qt.WindowFullScreen)

        self.setStyleSheet("background-color: black")
        self.setWindowOpacity(0.5)

        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))

        self.start, self.end = QtCore.QPoint(), QtCore.QPoint()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            QtWidgets.QApplication.quit()

        return super().keyPressEvent(event)

    def paintEvent(self, event):
        if self.start == self.end:
            return super().paintEvent(event)

        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(QtGui.QColor(255, 255, 255), 3))
        painter.setBrush(QtGui.QColor(255, 255, 255, 100))

        if self.is_macos:
            start, end = (self.mapFromGlobal(self.start), self.mapFromGlobal(self.end))
        else:
            start, end = self.start, self.end

        painter.drawRect(QtCore.QRect(start, end))
        return super().paintEvent(event)

    def mousePressEvent(self, event):
        self.start = self.end = QtGui.QCursor.pos()
        self.update()
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.end = QtGui.QCursor.pos()
        self.update()
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if self.start == self.end:
            return super().mouseReleaseEvent(event)

        x1, x2 = sorted((self.start.x(), self.end.x()))
        y1, y2 = sorted((self.start.y(), self.end.y()))
### 然后启动截图界面，
#### QtCore.QCoreApplication.setAttribute(Qt.AA_DisableHighDpiScaling)
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
snipper = Snipper(window)
snipper.show()
### 用户拖动、框选窗口，会获取窗口的起点和终点的坐标，这时候可以调用下面语句进行截图，获取需要OCR识别的文本图像，
#### shot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
## OCR文字识别
### 通过ImageGrab.grab截取到文本图像shot，下一步就是要把图像内容输入给后端的tesseract引擎，让它把图像转化为字符串
### result = pytesseract.image_to_string(img, timeout=2, lang=(sys.argv[1] if len(sys.argv) > 1 else None))
### 到这里，就实现了一款准确度高、永久免费的OCR工具。
## 回顾一下Textshot的项目，我们会发现截图坐标范围内的图像、OCR识别只需要2行代码，大多数都是在围绕获取窗口起点和终点坐标在开发。换句话说，Textshot这个项目对OCR核心部分并没有做任何更改，只是在产品包装方面做了一些巧妙的工作。
## 我们其实也可以发散思维，产生更多与众不同的产品思路，例如，
## 通过Python的第三方PDF处理库实现一款PDF文本识别工具
tesseract结合web框架实现一个网页端OCR工具
结合tesseract和Google、有道翻译API实现一款OCR+翻译工具
...
##
---
## 截屏、文字提取一气呵成，超实用OCR开源小工具 - 机器之心的文章 - 知乎
https://zhuanlan.zhihu.com/p/145011923
## 项目链接：
### https://github.com/ianzhao05/textshot
## 使用方法
### 运行 textshot.py，在屏幕上打开一个 overlay，在你希望提取的文字区域画一个矩形。
### 使用可选的命令行参数指定语言。
#### 例如，python textshot.py eng + fra 将使用英语作为主要语言，使用法语作为次要语言。
#### 默认值为英语（eng）。
#### 同时确保为其他语言安装了适用于 Tesseract 的数据文件。
### 建议将热键附加到此工具上。
#### 对于 Windows 来说，可以使用 AutoHotkey 脚本来完成此操作；textshot.ahk 同时也包含一个可以使用的示例 AHK 脚本。
#### 如果是 Ubuntu 系统，可以打开「键盘设置」，其中显示了所有 Gnome 快捷方式。底部有一个「+」按钮，可用于添加你自己的快捷方式。
#### 单击并将其命令设置为 / usr / bin / python3 <path-to-textshot.py>。
##### 如果使用的是 venv，则上面的 python3 路径应指向 venv 的 python3 而不是全局 python3。
#### ...
#### 并通过将目录添加到系统路径来确保可以从命令行访问 tesseract。
## Tessract 的使用
### 该工具在受控条件下也能很好地运行，但是如果存在大量噪声或者图像输入 Tesseract 前未经恰当处理，则性能较差。
### Tesseract 支持 Unicode（UTF-8）字符集，可以识别超过 100 种语言，还包含多种输出支持，比如纯文本、PDF、TSV 等。
### 但是为了得到更好的 OCR 结果，还必须提升提供给 Tesseract 的图像的质量。值得注意的是，在执行实际的 OCR 之前，Tesseract 会在内部执行多种不同的图像处理操作（使用 Leptonica 库）。通常情况下表现不错，但在一些特定的情况下的效果却不够好，导致准确度显著下降。
### 在将图像传递给 Tesseract 之前，可以尝试以下图像处理技术，但具体使用哪些技术取决于使用者想要读取的图像：
#### 反转图像
#### 重新缩放
#### 二值化
#### 移除噪声
#### 旋转/调整倾斜角度
#### 移除边缘
### 所有这些操作都可以使用 OpenCV 或通过 Python 使用 numpy 实现。
