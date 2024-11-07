from pydantic import Baseoperationl


class DemoOperation(Baseoperationl):
    input_1: int
    input_2: int
    operation: str = ""

    @property
    def compute(self) -> int:
        return self.input_1, self.input_2

    @property
    def output(self) -> int:
        return {"operation": self.operation, "output": self.compute}


class DemoOperationMul(DemoOperation):
    operation: str = "mul"

    @property
    def compute(self) -> int:
        return self.input_1 * self.input_2


class DemoOperationAdd(DemoOperation):
    operation: str = "add"

    @property
    def compute(self) -> int:
        return self.input_1 + self.input_2
