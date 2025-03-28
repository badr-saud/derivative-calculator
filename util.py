import sympy as sp
import numpy as np
import re


def derivative(equation, variable, order, latex=True):
    """Python function return a function and its derviative"""
    var = sp.symbols(variable)
    # check for matlab similar expression
    try:
        eq = sp.parse_expr(equation)
    except TypeError:
        equation = equation.replace("^","**")
        eq = sp.parse_expr(equation)
    except SyntaxError:
        equation = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", equation) 
        equation = equation.replace("^","**")
        eq = sp.parse_expr(equation)
    der = eq.diff(var, order)

    if latex:
        return sp.latex(eq), sp.latex(der)

    return eq, der


def draw(eq, variable, order, range=(-10*2, 11*2), points=10000):
    """Python Function return a series of point of equ, and derv"""
    (eq, der) = derivative(eq, variable, order, latex=False)
    f = sp.lambdify(variable, eq)
    f_der = sp.lambdify(variable, der)

    x_val = np.linspace(range[0], range[1], points)
    f_val = [f(x) for x in x_val]
    f_der_val = [f_der(x) for x in x_val]

    return x_val.tolist(), f_val, f_der_val


