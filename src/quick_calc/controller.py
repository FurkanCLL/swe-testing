from src.quick_calc.engine import CalculatorEngine


class CalculatorController:
    def __init__(self, engine=None):
        self.engine = engine or CalculatorEngine()

        # define attributes here so IDE stops warning
        self.left = None
        self.op = None
        self.current = ""
        self.display = "0"

        self.reset()
    def reset(self):
        self.left = None
        self.op = None
        self.current = ""   # typed digits as string
        self.display = "0"

    def press(self, key: str) -> str:
        if key == "C":
            self.reset()
            return self.display

        if key in "0123456789.":
            # avoid multiple dots
            if key == "." and "." in self.current:
                return self.display

            self.current += key
            self.display = self.current if self.current else "0"
            return self.display

        if key in "+-*/":
            # if left not set, take current as left
            if self.left is None:
                self.left = self._current_as_number(default=0)
            else:
                # if user presses operator again after typing right operand
                if self.current != "":
                    self.left = self._apply(self.left, self.op, self._current_as_number(default=0))

            self.op = key
            self.current = ""
            self.display = str(self.left)
            return self.display

        if key == "=":
            if self.op is None:
                # nothing to compute
                self.display = str(self._current_as_number(default=self.left if self.left is not None else 0))
                return self.display

            right = self._current_as_number(default=0)
            try:
                result = self._apply(self.left if self.left is not None else 0, self.op, right)
            except ZeroDivisionError:
                self.reset()
                self.display = "Error"
                return self.display

            # after equals, keep result as left so user can continue
            self.left = result
            self.current = ""
            self.op = None
            self.display = str(result)
            return self.display

        # unknown key, ignore
        return self.display

    def _current_as_number(self, default=0):
        if self.current == "" or self.current == ".":
            return default
        # int if possible, else float
        if "." in self.current:
            return float(self.current)
        return int(self.current)

    def _apply(self, a, op, b):
        if op == "+":
            return self.engine.add(a, b)
        if op == "-":
            return self.engine.subtract(a, b)
        if op == "*":
            return self.engine.multiply(a, b)
        if op == "/":
            return self.engine.divide(a, b)
        return a