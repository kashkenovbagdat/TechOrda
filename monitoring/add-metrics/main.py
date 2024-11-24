from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

app = FastAPI()

#Метрика Counter для отслеживания количества запросов
http_requests_total =Counter(
    'http_request_total',
    'Number of HTTP request received',
    ['method','endpoint']
)

#Метрика Histogram для отслеживания времени выполнения запросов

http_requests_milliseconds = Histogram(
    'http_requests_milliseconds',
    'Duration of HTTP requests in milliseconds',
    ['method', 'endpoint']
)


# Мертрики Gauge для хранения последних результатов
last_sum1n = Gauge('last_sum1n', 'Value store last result of sum1n')
last_fibo = Gauge('last_fibo', 'Value store last result of sum1n')
list_size = Gauge('list_size', 'Value stores current list size')
last_calculator = Gauge('last_calculator', 'value stores last result of calculator')


# Метрика Counter для отслеживания ошибок в калькуляторе 
errors_calculator_total = Counter(
    'erroes_calculator_total',
    'Number of errors in calculator'
)


# Middleware для мониторинга запросов
class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        method = request.method
        endpoint = request.url.path
        start_time = time.time()

        # Увеличиваем счетчик запросов
        http_requests_total.labels(method=method, endpoint=endpoint).inc()

        # Обрабатываем запрос
        response = await call_next(request)

        # Записываем длительность запроса
        duration = (time.time() - start_time) * 1000  # в миллисекундах
        http_requests_milliseconds.labels(method=method, endpoint=endpoint).observe(duration)

        return response

app.add_middleware(MetricsMiddleware)

# Пример обработчиков с обновлением метрик
@app.get("/sum1n/{n}")
async def sum1n(n: int):
    result = sum(range(1, n + 1))
    last_sum1n.set(result)
    return {"result": result}

@app.get("/fibo/{n}")
async def fibo(n: int):
    # Функция для вычисления n-го числа Фибоначчи
    def fibonacci(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    result = fibonacci(n)
    last_fibo.set(result)
    return {"result": result}

@app.get("/calculator")
async def calculator(a: int, b: int, operation: str):
    try:
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b == 0:
                errors_calculator_total.inc()
                return {"error": "ZeroDivisionError"}
            result = a / b
        else:
            errors_calculator_total.inc()
            return {"error": "Invalid operation"}
        last_calculator.set(result)
        return {"result": result}
    except Exception:
        errors_calculator_total.inc()
        return {"error": "Calculation error"}

@app.get("/list_size")
async def list_size_endpoint():
    # Пример списка, размер которого мы мониторим
    sample_list = [1, 2, 3, 4, 5]  # можно изменить на актуальный список
    list_size.set(len(sample_list))
    return {"size": len(sample_list)}

# Эндпоинт для экспорта метрик
@app.get("/metrics")
async def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)