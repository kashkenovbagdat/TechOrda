
#////////////////////////////////////////////////////////////
from fastapi import FastAPI

app=FastAPI()

@app.get("/hello")
def hello():
    return{"hello":"world"}

@app.post("/create")
def create(item:int):
    return {"newitem":item}
#////////////////////////////////////////////////////////////
from fastapi import FastAPI
from typing import Dict

app = FastAPI()

@app.get("/sum1n/{n}")
def sum_1_to_n(n: int) -> Dict[str, int]:
    result = sum(range(1, n + 1))
    return {"result": result}
#////////////////////////////////////////////////////////////
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/fibo")
def get_fibonacci(n: Optional[int] = 1):
    if n <=0:
        return {"result": None}
    
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    
    return {"result": a}
#////////////////////////////////////////////////////////////
from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/reverse")
def reverse_string(string: str = Header(...)):

    reverse_string = string[::-1]
    return JSONResponse(content={"result": reverse_string})
#////////////////////////////////////////////////////////////
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Глобальный массив для сохранения элементов
elements = []

# Модель для запроса
class Element(BaseModel):
    element: str

@app.put("/list")
def add_element(item: Element):
    elements.append(item.element)  # Добавляем только строку из объекта Element
    return {"result": elements}

@app.get("/list")
def get_elements():
    return {"result": elements}
#////////////////////////////////////////////////////////////
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()
#Глобальный массив для храния элементов
elements = []

# модель данных для запросов
class Element(BaseModel):
    element: str #Поле для добавления элемента

#Эндпоин для добавления элемента в массив
@app.put("/list")
def add_element(item: Element):
    elements.append(item.element) #добавление элемента в глобальный массивы
    return JSONResponse(content={"return": elements})


# Эндпоинт для получения всех элементов из массива
@app.get("/list")
def get_elements():
    return JSONResponse(content={"result": elements})


#////////////////////////////////////////////////////////////

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import operator

app = FastAPI()

# Модель данных для запросов
class Expression(BaseModel):
    expr: str # Строка, содержащая математическое выражение

#Эндпоинт для вычисления математического выражения

@app.post("/calculator")
def calculator(expression: Expression):

    try:
        #
        num1, op, num2 = expression.expr.split(',')
        num1 = float(num1) #
        num2 = float(num2) #

        #
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        if op not in operations:
            #
            raise HTTPException(status_code=403, detail={"error": "zerodiv"})
        #
        result = operations[op](num1, num2)
        return JSONResponse(content={"result": result})
    
    except ValueError:
    #
         raise HTTPException(status_code=400, detail={"error": "ivalid"})
    except Exception as e:
        #
        raise HTTPException(status_code=500, detail={"error": str(e)})


