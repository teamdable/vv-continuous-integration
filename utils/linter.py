import subprocess
from typing import Tuple

def is_python_file(file_path: str) -> bool:
    if file_path.endswith('.py'):
        return True
    with open(file_path, 'r') as file:
        if file.readline().startswith('#!/usr/bin/env python'):
            return True
    return False


def get_pylint_score(file_path: str) -> Tuple[int, str]:
    try:
        output = subprocess.check_output(
            ['pylint --rcfile=action/.pylintrc', file_path],
            shell=True).decode('utf-8')
    except:
        return (0, "")
    else:
        score = output.split('Your code has been rated at ')[1].split('/')[0]
        return (int(score), output)
