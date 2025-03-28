from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from util import derivative, draw
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"),name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.post("/calc")
def calc(
    request: Request,
    equation: str = Form(...),
    variable: str = Form(...),
    order: int = Form(...),
):
    (eq, der) = derivative(equation, variable, order)
    (x_val, f_val, f_der_val) = draw(equation, variable, order, range=(-2,2))
    print(type(x_val), type(f_val), type(f_der_val))
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "eq": eq,
            "variable": variable,
            "order": order,
            "der": der,
            "x_val": json.dumps(x_val),
            "f_val": json.dumps(f_val),
            "f_der_val": json.dumps(f_der_val),
        },
    )
