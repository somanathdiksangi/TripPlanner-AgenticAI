from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class CalculationInput(BaseModel):
    operation: str = Field(..., description="The mathematical expression to evaluate")

class CalculatorTools(BaseTool):
    name: str = "Make a calculation"
    description: str = """Useful to perform any mathematical calculations, 
    like sum, minus, multiplication, division, etc.
    The input should be a mathematical expression, e.g. '200*7' or '5000/2*10'"""
    args_schema: type[BaseModel] = CalculationInput

    def _run(self, operation: str) -> float:
        return eval(operation)

    async def _arun(self, operation: str) -> float:
        raise NotImplementedError("Async not implemented")
