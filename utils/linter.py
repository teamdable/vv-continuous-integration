from io import StringIO
from typing import Tuple

from pylint.lint import Run
from pylint.reporters.text import TextReporter

def is_python_file(file_path: str) -> bool:
    if file_path.endswith('.py'):
        return True
    with open(file_path, 'r') as file:
        if file.readline().startswith('#!/usr/bin/env python'):
            return True
    return False


def get_pylint_score(file_path: str) -> Tuple[int, str]:
    try:
        pylint_output = StringIO()
        reporter = TextReporter(output=pylint_output)
        Run([file_path, '--rcfile=action/.pylintrc'], reporter=reporter, do_exit=False)
        output = pylint_output.getvalue()
    except:
        return (0.0, "")
    else:
        score = float(output.split('Your code has been rated at ')[1].split('/')[0])
        return (score, output)
