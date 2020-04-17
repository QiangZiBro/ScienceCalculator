"""
Author : QiangZiBro
Discription : In this module, we have three classes
    - Calculator : using regular expression to find science calculation, and replace with results
    - BaseCalculator : basic four fundamental operations of arithmetic
    - ExpressionReader : a class which is helpful in read number or operator
                         WHEN DO INFIX EXPRESSION TO SUFFIX EXPRESSION

    all we need is:
        from calculator import calculate,PRECISION
        calculate(text)
TODO:
"""
__all__ = ("calculate")

import math
import re
import logging
from utils import wrapper
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

num_pattern = r"((\d+\.\d+)|(\d+\.?)|(\.\d+))"  # 匹配 X.X X X. .X
pow_pattern = r"{}\^\({}\)".format(num_pattern, num_pattern)  # 匹配指数
factorial_pattern = r"{}!".format(num_pattern)
# 匹配科学计算 sin,cos,tan,ln,log,√ 【注，也可能匹配到上面都没，比如(11)
science_pattern = r"√?([a-z]{2,3})?\(-?" + num_pattern + "\)"


# 计算类
class Calculator:
    def __init__(self, expression):
        self.expression = expression

    def get_result(self):
        self.expression = self.process_science_variables()
        self.expression = self.pow()
        self.expression = self.factorial()
        self.expression = self.square()
        self.expression = self.science_calculator()
        return self.cal()

    def factorial(self):
        def _factorial(expr):
            expr = expr.group(0)
            num = expr[:-1]
            if num == "" or "." in num:
                raise NameError("wrong factorial number {}".format(num))
            else:
                num = int(num)
            result = math.factorial(num)
            result = str(result)
            return result

        self.expression = re.sub(factorial_pattern, _factorial, self.expression, count=0, flags=0)
        return self.expression

    def process_science_variables(self):
        """ Process π or e
        BUG FIXED: Will replace exp() to 2.7xp()
        :return:
        """
        self.expression = self.expression.replace("exp", "fuck")
        self.expression = self.expression.replace("e", str(math.e))
        self.expression = self.expression.replace("fuck", "exp")

        self.expression = self.expression.replace("π", str(math.pi))
        return self.expression

    def pow(self):
        """ calculate a^(b) in a expr
        :return: replaced expr
        """

        def _pow(pow_expr):

            pow_expr = pow_expr.group(0)
            pow_expr = pow_expr.split("^(")

            base = pow_expr[0]
            index = pow_expr[1][:-1]

            if base == "" or index == "":
                raise Exception("wrong pow expression:{}".format(pow_expr))
            else:
                base = float(base)
                index = float(index)
            result = math.pow(base, index)

            if result < 0:
                return wrapper(str(result))
            else:
                return str(result)

        self.expression = re.sub(pow_pattern, _pow, self.expression, count=0, flags=0)
        return self.expression

    def square(self):
        def _square(expr):
            pow_expr = expr.group(0)
            num = pow_expr[:-1]
            if num == "":
                raise Exception("wrong square expression:{}".format(expr))
            else:
                num = float(num)
            return str(num ** 2)

        square_pattern = r"({})?²".format(num_pattern)
        self.expression = re.sub(square_pattern, _square, self.expression, count=0, flags=0)
        return self.expression

    def science_calculator(self):
        """ Caculate something like tan(3) ln(2) √(3)
                Special case (3)

        :return:
        """

        def _science_calculate(expr):

            expr = expr.group(0)
            expr1 = expr.split("(")
            op = expr1[0]
            num = expr1[1][:-1]
            if num == "":
                raise NameError("wrong calculate for '{}'".format(expr))
            else:
                num = float(num)

            if op == "sin":
                result = math.sin(num)
            elif op == "cos":
                result = math.cos(num)
            elif op == "tan":
                result = math.tan(num)
            elif op == "log":
                result = math.log10(num)
            elif op == "ln":
                result = math.log(num)
            elif op == "√":
                result = math.sqrt(num)
            elif op == "exp":
                result = math.exp(num)
            elif op == "":
                result = num
            else:
                raise NameError("wrong operator for '{}'".format(op))

            if result < 0:
                return wrapper(str(result))
            else:
                return str(result)

        self.expression = re.sub(science_pattern, _science_calculate, self.expression, count=0, flags=0)
        return self.expression

    def cal(self):
        """ calculate for +-×÷
        :return:
        """
        return BaseCalculator(self.expression).get_result()


# 计算四则运算
class BaseCalculator:
    def __init__(self, expression):
        self.backorder_queue = self.cal_backorder_queue(expression)

    def get_result(self):
        s = []
        for i in self.backorder_queue:
            if i in "+-×÷()":
                a, b = s.pop(), s.pop()
                a, b = float(a), float(b)
                if i == "+":
                    result = a + b
                elif i == "-":
                    result = b - a
                elif i == "×":
                    result = a * b
                else:
                    result = b / a
                s.append(result)
            else:
                s.append(float(i))
        return s[-1]

    def cal_backorder_queue(self, expression):
        reader = ExpressionReader(expression)
        s1, backorder_queue = [], []
        for r in reader.read():
            if r in "+-×÷()":
                if r in "×÷(":
                    s1.append(r)
                elif r in "+-":
                    while len(s1) != 0 and s1[-1] in "×÷":
                        backorder_queue.append(s1.pop(-1))
                    s1.append(r)
                else:  # r == ")"
                    while len(s1) != 0 and s1[-1] != "(":
                        backorder_queue.append(s1.pop(-1))
                    s1.pop(-1)
            else:
                backorder_queue.append(r)
        while len(s1) != 0:
            backorder_queue.append(s1.pop())
        return backorder_queue


# 从表达式中读取一个数或操作符
class ExpressionReader:
    def __init__(self, expression):
        self.expression = expression
        if self.expression.startswith("-"):
            self.expression = "0" + self.expression

    def read(self):
        while self.expression != "":
            if self.expression[0] in "+-×÷()":
                result = self.expression[0]
                self.expression = self.expression[1:]
                yield result
            else:
                yield self.find_num()

    def find_num(self):
        science_num_pattern = r"^{}(e-?\d+)?".format(num_pattern)  # 匹配 `数字e整数` `数字e-整数` 或者 `数字`
        result = re.match(science_num_pattern, self.expression)
        self.expression = self.expression[result.span()[1]:]
        return result.group()


def calculate(expr, precision, percent=False):
    calc = Calculator(expr)
    result = calc.get_result()
    if percent:
        result = result * 100
    result = round(result, precision)
    equation = "{}={}".format(expr, result)
    logger.info("Precision {} {}=".format(precision, expr) + str(result))
    if expr == "520×1314":
        result = "qiangzibro ❤️  cyl"
    return result, equation


if __name__ == "__main__":
    exprs = [
        "(3+2)×(4+6)×sin(π)",
        "3²×tan(-1)",
        "3×4",
        "log(100)",
        "6×ln(3)",
        "exp(3)",
        "5!+1",
        "-3×2",
        "-0.4×log(0.4)-0.6×log(0.6)",
        "(11)"
        #  "1e-3" NOT ALLOWED
    ]
    for e in exprs:
        calculate(e, precision=9)
