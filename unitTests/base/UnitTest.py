from scripts.interpreter.interpreter import Interpreter


class UnitTest:
    def __init__(self):
        self.inter = Interpreter()

    def full_run(self, file, target_pos):
        self.inter.read_file(f"unitTests/scripts/{file}")
        self.inter.run()
        self.equal(target_pos)
        self.inter.reset()

    def equal(self, target_pos):
        if not self.inter.got_error:
            print(self.inter.actor.position_x == target_pos[0] and self.inter.actor.position_y == target_pos[1])
        else:
            print("Процесс завершён ошибкой")