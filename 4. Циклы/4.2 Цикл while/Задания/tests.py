import os
import sys
from typing import Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.stdout.reconfigure(encoding="utf-8")

from tester import TaskConfig, TestCase, exact_match, run_module

_BASE_DIR = os.path.dirname(__file__)


def _float_validator(output: str, expected: float) -> Tuple[bool, str]:
    try:
        actual = float(output.strip())
    except ValueError:
        return False, f"Ожидалось вещественное число, получено: {output!r}"
    tolerance = 1e-6 * max(1.0, abs(expected))
    if abs(actual - expected) > tolerance:
        return False, f"Ожидалось ≈{expected}, получено {actual}"
    return True, ""


TASKS = [
    TaskConfig(
        task_id="46",
        name="Исполнитель раздвоитель",
        filename="Задание 46.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase("179\n20", "-1\n:2\n-1\n:2\n:2\n-1\n-1"),
            TestCase("10\n3", ":2\n-1\n-1"),
            TestCase("8\n1", ":2\n:2\n:2"),
            TestCase("15\n7", "-1\n:2"),
            TestCase("100\n5", ":2\n:2\n-1\n:2\n:2\n-1"),
            TestCase("20\n1", ":2\n:2\n-1\n:2\n:2"),
            TestCase("5\n4", "-1"),
            TestCase("16\n1", ":2\n:2\n:2\n:2"),
        ],
    ),
    TaskConfig(
        task_id="47",
        name="Сумма цифр числа",
        filename="Задание 47.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase("564", "15"),
            TestCase("1234", "10"),
            TestCase("1", "1"),
            TestCase("9", "9"),
            TestCase("100", "1"),
            TestCase("999", "27"),
            TestCase("12345", "15"),
        ],
    ),
    TaskConfig(
        task_id="48",
        name="Банковский вклад",
        filename="Задание 48.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase(
                "1000\n1100\n25",
                "1 - 1020.83\n2 - 1042.10\n3 - 1063.81\n4 - 1085.97\n5 - 1108.60",
            ),
            TestCase(
                "1000\n1300\n48",
                "1 - 1040.00\n2 - 1081.60\n3 - 1124.86\n4 - 1169.86"
                "\n5 - 1216.65\n6 - 1265.32\n7 - 1315.93",
            ),
            TestCase(
                "200\n250\n36",
                "1 - 206.00\n2 - 212.18\n3 - 218.55\n4 - 225.10"
                "\n5 - 231.85\n6 - 238.81\n7 - 245.97\n8 - 253.35",
            ),
        ],
    ),
    TaskConfig(
        task_id="49",
        name="Среднее значение последовательности",
        filename="Задание 49.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=_float_validator,
        test_cases=[
            TestCase("1\n7\n9\n0", (1 + 7 + 9) / 3),
            TestCase("1\n2\n3\n0", 2.0),
            TestCase("5\n0", 5.0),
            TestCase("10\n20\n30\n40\n0", 25.0),
            TestCase("1\n1\n1\n0", 1.0),
            TestCase("-3\n5\n0", 1.0),
            TestCase("-5\n0", -5.0),
        ],
    ),
    TaskConfig(
        task_id="410",
        name="Максимум последовательности",
        filename="Задание 410.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase("1\n7\n9\n0", "9"),
            TestCase("1\n2\n3\n0", "3"),
            TestCase("5\n0", "5"),
            TestCase("9\n7\n1\n0", "9"),
            TestCase("3\n3\n3\n0", "3"),
            TestCase("1\n100\n2\n0", "100"),
        ],
    ),
    TaskConfig(
        task_id="411",
        name="Количество максимумов последовательности",
        filename="Задание 411.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase("1\n7\n9\n0", "1"),
            TestCase("1\n3\n3\n1\n0", "2"),
            TestCase("5\n0", "1"),
            TestCase("3\n3\n3\n0", "3"),
            TestCase("1\n2\n3\n3\n2\n3\n0", "3"),
        ],
    ),
    TaskConfig(
        task_id="412",
        name="Второй максимум",
        filename="Задание 412.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase("1\n7\n9\n0", "7"),
            TestCase("1\n2\n3\n0", "2"),
            TestCase("9\n1\n0", "1"),
            TestCase("5\n3\n8\n2\n0", "5"),
            TestCase("1\n10\n100\n0", "10"),
        ],
    ),
    TaskConfig(
        task_id="413",
        name="Номера максимумов",
        filename="Задание 413.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase("1\n7\n9\n0", "3 3"),
            TestCase("1\n2\n3\n2\n3\n1\n0", "3 5"),
            TestCase("5\n0", "1 1"),
            TestCase("3\n1\n2\n0", "1 1"),
            TestCase("1\n3\n3\n1\n0", "2 3"),
        ],
    ),
    TaskConfig(
        task_id="414",
        name="Максимальное число идущих подряд равных элементов",
        filename="Задание 414.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase("1\n7\n7\n9\n0", "2"),
            TestCase("1\n7\n7\n7\n9\n0", "3"),
            TestCase("1\n2\n3\n0", "1"),
            TestCase("5\n0", "1"),
            TestCase("3\n3\n3\n3\n0", "4"),
            TestCase("1\n1\n2\n2\n2\n1\n0", "3"),
            TestCase("1\n2\n2\n1\n2\n2\n2\n1\n2\n2\n2\n2\n0", "4"),
        ],
    ),
    TaskConfig(
        task_id="415",
        name="Максимальная длина монотонного фрагмента",
        filename="Задание 415.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase("1\n7\n9\n0", "3"),
            TestCase("1\n2\n3\n2\n1\n0", "3"),
            TestCase("5\n0", "1"),
            TestCase("3\n2\n1\n0", "3"),
            TestCase("1\n3\n2\n4\n3\n5\n0", "2"),
            TestCase("1\n2\n3\n4\n5\n0", "5"),
            TestCase("1\n2\n2\n3\n4\n0", "3"),
        ],
    ),
]

if __name__ == "__main__":
    result = run_module("Цикл while", TASKS, _BASE_DIR)
    sys.exit(0 if result.solved_tasks == result.total_tasks else 1)
