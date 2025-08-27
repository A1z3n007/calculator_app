def calculate(expression):
    try:
        allowed_chars = "0123456789+-*/.() "
        if all(char in allowed_chars for char in expression):
            return eval(expression)
        else:
            raise ValueError("Недопустимые символы в выражении")
    except (SyntaxError, ZeroDivisionError, ValueError) as e:
        return f"Ошибка: {e}"