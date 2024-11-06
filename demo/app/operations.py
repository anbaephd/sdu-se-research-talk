from pydantic import BaseModel


class DemoOperation(BaseModel):
    input_1: int
    input_2: int

    @property
    def compute(self) -> int:
        return self.input_1, self.input_2

    @property
    def output(self) -> int:
        return {"output": self.compute}


class DemoOperationMul(DemoOperation):
    @property
    def compute(self) -> int:
        return self.input_1 * self.input_2

    @property
    def output(self) -> int:
        return {"output": self.compute}


class DemoOperationAdd(DemoOperation):
    @property
    def compute(self) -> int:
        return self.input_1 + self.input_2

    @property
    def output(self) -> int:
        return {"output": self.compute}
