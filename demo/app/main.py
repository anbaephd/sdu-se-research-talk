import os

import uvicorn
from fastapi import FastAPI, status

from .operations import DemoOperation, DemoOperationAdd, DemoOperationMul
from .utils import HealthCheck

SelectedDemoOperation = {
    "mul": DemoOperationMul,
    "add": DemoOperationAdd,
}.get(os.getenv("DEMOOPS"), DemoOperation)

app = FastAPI()


@app.get(
    "/health",
    summary="Perform a Health Check",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
async def get_health() -> HealthCheck:
    return HealthCheck(status="OK")


# Create a product
@app.post(
    "/",
    summary="Perform a ENV defined operation",
    status_code=status.HTTP_200_OK,
)
async def create_product(do: SelectedDemoOperation):
    return do.output


def main() -> None:
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)


if __name__ == "__main__":
    main()

# curl -X POST http://0.0.0.0:8080/ -H 'Content-Type: application/json' -d '{"input_1":12, "input_2":1}'
