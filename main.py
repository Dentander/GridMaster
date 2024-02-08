from scripts.interpreter.interpreter import Interpreter
import scripts.gui.qt as gui


if __name__ == "__main__":
    interpreter = Interpreter()
    gui.start(interpreter)
