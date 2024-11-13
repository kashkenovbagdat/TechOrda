from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, Dict, List
import operator

app = FastAPI()

# /hello
@app.get("/hello")
def hello():
    return {"hello": "world"}

# /create
class Item(BaseModel):
    item: int

@app.post("/create")
def create(item: Item):
    return {"newitem": item.item}

# /sum1n/{n}
@app.get("/sum1n/{n}")
def sum_1_to_n(n: int) -> Dict[str, int]:
    if n <= 0:
        raise HTTPException(status_code=400, detail="Parameter 'n' must be a positive integer")
    result = sum(range(1, n + 1))
    return {"result": result}

# /fibo
@app.get("/fibo")
def get_fibonacci(n: Optional[int] = 1):
    if not isinstance(n, int) or n <= 0:
        raise HTTPException(status_code=400, detail="Parameter 'n' must be a positive integer")
    
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    
    return {"result": a}

# /reverse
class ReverseRequest(BaseModel):
    string: str

@app.post("/reverse")
def reverse_string(request: ReverseRequest):
    reversed_str = request.string[::-1]
    return JSONResponse(content={"result": reversed_str})

# /list
elements: List[str] = []

class Element(BaseModel):
    element: str

@app.get("/list")
def get_elements():
    return {"result": elements}

@app.put("/list")
def add_element(item: Element):
    if not item.element:
        raise HTTPException(status_code=400, detail="Element cannot be empty")
    elements.append(item.element)
    return {"result": elements}

# /calculator
class Expression(BaseModel):
    expr: str

@app.post("/calculator")
def calculator(expression: Expression):
    try:
        parts = expression.expr.split(',')
        if len(parts) != 3:
            raise HTTPException(status_code=400, detail="Expression format must be 'num1,operator,num2'")
        
        num1, op, num2 = parts
        num1 = float(num1)
        num2 = float(num2)

        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        if op not in operations:
            raise HTTPException(status_code=400, detail="Invalid operator")

        if op == '/' and num2 == 0:
            raise HTTPException(status_code=403, detail="Division by zero is not allowed")

        result = operations[op](num1, num2)
        return JSONResponse(content={"result": result})

    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid numbers in expression")
    except Exception as e:
        raise HTTPException(status_code=500, detail={"error": str(e)})
