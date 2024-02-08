from PySide6 import QtTest, QtWidgets, QtGui, QtCore
import qdarktheme
import sys

from PySide6.QtGui import QIcon

interpreter = None


class Code(QtWidgets.QScrollArea):
    def __init__(self, parent = None):
        super().__init__(parent = parent)
        self.setWidgetResizable(True)
        content = QtWidgets.QWidget(self)
        self.setWidget(content)
        lay = QtWidgets.QVBoxLayout(content)
        self.code = QtWidgets.QTextEdit(content)
        self.code.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.code.setWordWrapMode(QtGui.QTextOption.WrapMode())
        lay.addWidget(self.code)
        self.setContentsMargins(0,0,0,0)
        self.code.setPlainText("CODE HERE")
        self.code.setAcceptRichText(False)
        self.code.setTabStopDistance(QtGui.QFontMetricsF(self.code.font()).horizontalAdvance(' ') * 4)

    def setText(self, text):
        self.code.setText(text)
    
    def getText(self):
        return self.code.toPlainText()


class ErrorPlace(QtWidgets.QScrollArea):
    def __init__(self, parent = None):
        super().__init__(parent = parent)
        self.setWidgetResizable(True)
        content = QtWidgets.QWidget(self)
        self.setWidget(content)
        lay = QtWidgets.QVBoxLayout(content)
        self.label = QtWidgets.QTextEdit(content)
        self.label.setReadOnly(1)
        self.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label.setWordWrapMode(QtGui.QTextOption.WrapMode())
        lay.addWidget(self.label)
        self.setContentsMargins(0,0,0,0)
        self.setMaximumHeight(200)

    def setError(self, text):
        self.label.setTextColor("Red")
        self.label.setText(text)
        self.label.setTextColor("Red")
    
    def setAllGood(self):
        self.label.setTextColor("Green")
        self.label.setText("NO ERRORS")
        self.label.setTextColor("Green")


class ToolBox(QtWidgets.QGroupBox):
    def __init__(self, parent = None):
        super().__init__(parent = parent)

        self.parent = parent

        self.start_stop = 0

        self.main_vbox = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_vbox)

        self.size = 35

        self.code_edit = Code()
        self.error_place = ErrorPlace()
        self.error_place.setAllGood()

        self.save_button = QtWidgets.QToolButton(self)
        self.save_button.setIcon(QtGui.QIcon("data/icons/save.svg"))
        self.save_button.setIconSize(QtCore.QSize(self.size, self.size))
        self.save_button.setFixedWidth(self.size)
        self.save_button.setFixedHeight(self.size)
        self.save_button.clicked.connect(self.saveFile)
        
        self.open_button = QtWidgets.QToolButton(self)
        self.open_button.setIcon(QtGui.QIcon("data/icons/open.svg"))
        self.open_button.setIconSize(QtCore.QSize(self.size, self.size))
        self.open_button.setFixedWidth(self.size)
        self.open_button.setFixedHeight(self.size)
        self.open_button.clicked.connect(self.openFile)

        self.run_button = QtWidgets.QToolButton(self)
        self.run_button.setIcon(QtGui.QIcon("data/icons/run.svg"))
        self.run_button.setIconSize(QtCore.QSize(self.size, self.size))
        self.run_button.setFixedWidth(self.size)
        self.run_button.setFixedHeight(self.size)
        self.run_button.clicked.connect(self.error_place.setAllGood)
        self.run_button.clicked.connect(self.run)

        self.stop_button = QtWidgets.QToolButton(self)
        self.stop_button.setIcon(QtGui.QIcon("data/icons/stop.svg"))
        self.stop_button.setIconSize(QtCore.QSize(self.size, self.size))
        self.stop_button.setFixedWidth(self.size)
        self.stop_button.setFixedHeight(self.size)
        self.stop_button.clicked.connect(self.stop)

        self.toolbox_groupbox = QtWidgets.QGroupBox()
        self.toolbox_hbox = QtWidgets.QHBoxLayout()
        self.toolbox_groupbox.setLayout(self.toolbox_hbox)

        self.toolbox_hbox.addWidget(self.save_button)
        self.toolbox_hbox.addWidget(self.open_button)
        self.toolbox_hbox.addWidget(self.run_button)
        self.toolbox_hbox.addWidget(self.stop_button)

        self.toolbox_groupbox.setMinimumHeight(self.size)

        self.main_vbox.addWidget(self.toolbox_groupbox)
        self.main_vbox.addWidget(self.code_edit)
        self.main_vbox.addWidget(self.error_place)

        self.setContentsMargins(0,0,0,0)
    
    def stop(self):
        self.start_stop = 0
        self.parent.parent.viewbox.ChangePlayerPos(0, 0)

    def run(self):
        global interpreter
        self.start_stop = 1
        code = self.code_edit.getText()
        
        interpreter.reset()
        interpreter.read_code_from_TextEdit(code)
        self.parent.parent.viewbox.ChangePlayerPos(0, 0)
        while interpreter.finished() != 1 and interpreter.error_finish() != 1 and self.start_stop:
            interpreter.execute_current_line()
            self.parent.parent.viewbox.ChangePlayerPos(interpreter.getX(), interpreter.getY())
            QtTest.QTest.qWait(100)
        
        if(interpreter.error_finish()):
            self.error_place.setError(interpreter.get_error())
        else:
            self.error_place.setAllGood()
        
    def openFile(self):
        global interpreter
        
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open code file", filter = "Text files (*.txt)" )

        interpreter.reset()
        try:
            with open(filename[0]) as file:
                try:
                    text = file.read()
                    self.code_edit.setText(text)
                    interpreter.read_code_from_TextEdit(text)
                except Exception as exception:
                    self.error_place.setError('COULD NOT OPEN FILE')
        except Exception as exception:
            pass
    
    def saveFile(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
        try:
            file = open(name[0],'w')
            text = self.code_edit.getText()
            file.write(text)
            file.close()
        except Exception as _:
            pass


class LeftBox(QtWidgets.QGroupBox):
    def __init__(self, parent = None):
        super().__init__(parent = parent)

        self.parent = parent

        self.vbox = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.vbox)

        self.toolbox = ToolBox(self)
        self.setContentsMargins(0,0,0,0)
        self.vbox.setContentsMargins(0,0,0,0)

        self.vbox.addWidget(self.toolbox)


class ViewBoxWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent = parent)

        self.size = 30

        self.setMinimumWidth(self.size * 21)

        self.segments = []

        for i in range(21):
            for j in range(21):
                self.segment = QtWidgets.QLabel(self)
                self.segment.setPixmap(QtGui.QIcon("data/icons/place-segment.svg").pixmap(self.size, self.size))
                
                self.segment.setMinimumHeight(self.size)
                self.segment.setMaximumHeight(self.size)
                self.segment.setMaximumWidth(self.size)
                self.segment.setMinimumWidth(self.size)
                self.segment.move(i * self.size, j * self.size)

                self.segments.append(self.segment)

        self.player = QtWidgets.QLabel(self)
        self.player.setPixmap(QtGui.QIcon("data/icons/player.svg").pixmap(self.size, self.size))
        self.player.setMinimumHeight(self.size)
        self.player.setMaximumHeight(self.size)
        self.player.setMaximumWidth(self.size)
        self.player.setMinimumWidth(self.size)

        self.setMinimumHeight(self.size * 21)

        self.ChangePlayerPos(0, 0)
        

    def ChangePlayerPos(self, x_i, y_i):
        x, y = self.ConvertCoords(x_i, y_i)
        self.player.move(x * self.size, y * self.size)
    
    def ConvertCoords(self, x, y):
        return [x, abs(y-20)]
                

class ViewBox(QtWidgets.QGroupBox):
    def __init__(self, parent = None):
        super().__init__(parent = parent)
        self.setContentsMargins(0,0,0,0)

        self.vbox = QtWidgets.QHBoxLayout(self)
        self.vbox.setContentsMargins(0,0,0,0)

        self.widget = ViewBoxWidget(self)
        self.vbox.addWidget(self.widget)

        self.setLayout(self.vbox)
    
    def ChangePlayerPos(self, x, y):
        self.widget.ChangePlayerPos(x, y)


class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GridMaster - 4FUN IDE")
        self.setWindowIcon(QIcon('data/icons/logo.ico'))

        self.main_group = QtWidgets.QGroupBox(self)
        self.main_group.setContentsMargins(0,0,0,0)

        self.main_hbox = QtWidgets.QHBoxLayout()
        self.main_hbox.setContentsMargins(0,0,0,0)
        self.main_group.setLayout(self.main_hbox)


        self.leftbox = LeftBox(self)
        self.viewbox = ViewBox()


        self.main_hbox.addWidget(self.leftbox)
        self.main_hbox.addWidget(self.viewbox)

        self.setCentralWidget(self.main_group)


def start(inter):
    global interpreter
    interpreter = inter

    app = QtWidgets.QApplication([])

    qdarktheme.setup_theme()
    gui = GUI()
    gui.show()
    sys.exit(app.exec())