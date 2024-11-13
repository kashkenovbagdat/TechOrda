from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, Dict
import operator

app = FastAPI()

# Маршрут /hello
@app.get("/hello")
def hello():
    return {"hello": "world"}

# Маршрут /create
@app.post("/create")
def create(item: int):
    return {"newitem": item}

# Маршрут /sum1n/{n}
@app.get("/sum1n/{n}")
def sum_1_to_n(n: int) -> Dict[str, int]:
    result = sum(range(1, n + 1))
    return {"result": result}

# Маршрут /fibo
@app.get("/fibo")
def get_fibonacci(n: Optional[int] = 1):
    if n <= 0:
        return {"result": None}
    
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    
    return {"result": a}

# Маршрут /reverse
@app.post("/reverse")
def reverse_string(string: str = Header(...)):
    reversed_str = string[::-1]
    return JSONResponse(content={"result": reversed_str})

# Глобальный массив для сохранения элементов
elements = []

# Модель для запроса
class Element(BaseModel):
    element: str

# Маршрут /list (GET)
@app.get("/list")
def get_elements():
    return {"result": elements}

# Маршрут /list (PUT)
@app.put("/list")
def add_element(item: Element):
    elements.append(item.element)
    return {"result": elements}

# Модель данных для запросов на калькулятор
class Expression(BaseModel):
    expr: str

# Маршрут /calculator
@app.post("/calculator")
def calculator(expression: Expression):
    try:
        num1, op, num2 = expression.expr.split(',')
        num1 = float(num1)
        num2 = float(num2)

        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        if op not in operations:
            raise HTTPException(status_code=403, detail={"error": "zerodiv"})
        
        result = operations[op](num1, num2)
        return JSONResponse(content={"result": result})
    
    except ValueError:
        raise HTTPException(status_code=400, detail={"error": "invalid"})
    except Exception as e:
        raise HTTPException(status_code=500, detail={"error": str(e)})
