from pydantic import BaseModel


class DemoOperation(BaseModel):
    input_1: int
    input_2: int
    mode: str = ""

    @property
    def compute(self) -> int:
        return self.input_1, self.input_2

    @property
    def output(self) -> int:
        return {"mode": self.mode, "output": self.compute}


class DemoOperationMul(DemoOperation):
    mode: str = "mul"

    @property
    def compute(self) -> int:
        return self.input_1 * self.input_2


class DemoOperationAdd(DemoOperation):
    mode: str = "add"

    @property
    def compute(self) -> int:
        return self.input_1 + self.input_2
