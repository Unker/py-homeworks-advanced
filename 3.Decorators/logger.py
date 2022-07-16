from functools import wraps
from datetime import datetime
from pathlib import Path
import os


def logger(path='/', log_name='logger.log'):
    """
    декоратор - логгер. Записывает в файл дату и время вызова функции,
    имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
    Входной параметр – путь к логам
    """
    def decorator(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            log = ''
            log += f'=========={datetime.now()}==========\n'
            log += f'function {old_function.__name__} was called\n'
            log += f'with args: {args} \n     kwargs: {kwargs}\n'
            ret = old_function(*args, **kwargs)
            log += f'was returned: {ret}\n'
            log += '\n'
            Path(path).mkdir(parents=True, exist_ok=True)
            with open(os.path.join(path, log_name), 'a+', encoding="utf8") as f:
                f.write(log)
            return ret
        return new_function
    return decorator


if __name__ == '__main__':
    @logger(path='logs', log_name='tst.log')
    def tst_func(x1, x2=0, x3=2):
        return x1+x2*x3

    tst_func(x1=2, x2=5)
