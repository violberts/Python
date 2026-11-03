import os
import sys
from typing import Tuple

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.stdout.reconfigure(encoding="utf-8")

from tester import TaskConfig, TestCase, exact_match, run_module

_BASE_DIR = os.path.dirname(__file__)


def _pythagorean_validator(output: str, expected: int) -> Tuple[bool, str]:
    n = expected
    lines = output.strip().split("\n")
    if len(lines) != n:
        return False, f"Ожидалось {n} строк, получено {len(lines)}"
    for i, line in enumerate(lines, 1):
        nums = line.split()
        if len(nums) != n:
            return False, f"Строка {i}: ожидалось {n} чисел, получено {len(nums)}"
        for j, num in enumerate(nums, 1):
            try:
                actual_val = int(num)
            except ValueError:
                return False, f"Строка {i}, колонка {j}: не число: {num!r}"
            if actual_val != i * j:
                return False, f"Строка {i}, колонка {j}: ожидалось {i * j}, получено {actual_val}"
    return True, ""


TASKS = [
    TaskConfig(
        task_id="41",
        name="Факториал",
        filename="Задание 41.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase("1", "1"),
            TestCase("2", "2"),
            TestCase("3", "6"),
            TestCase("4", "24"),
            TestCase("5", "120"),
            TestCase("6", "720"),
            TestCase("7", "5040"),
            TestCase("10", "3628800"),
            TestCase("12", "479001600"),
        ],
    ),
    TaskConfig(
        task_id="42",
        name="Таблица умножения",
        filename="Задание 42.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase("5", "5 * 1 = 5\n5 * 2 = 10\n5 * 3 = 15\n5 * 4 = 20\n5 * 5 = 25\n"
                         "5 * 6 = 30\n5 * 7 = 35\n5 * 8 = 40\n5 * 9 = 45\n5 * 10 = 50"),
            TestCase("1", "1 * 1 = 1\n1 * 2 = 2\n1 * 3 = 3\n1 * 4 = 4\n1 * 5 = 5\n"
                         "1 * 6 = 6\n1 * 7 = 7\n1 * 8 = 8\n1 * 9 = 9\n1 * 10 = 10"),
            TestCase("3", "3 * 1 = 3\n3 * 2 = 6\n3 * 3 = 9\n3 * 4 = 12\n3 * 5 = 15\n"
                         "3 * 6 = 18\n3 * 7 = 21\n3 * 8 = 24\n3 * 9 = 27\n3 * 10 = 30"),
            TestCase("7", "7 * 1 = 7\n7 * 2 = 14\n7 * 3 = 21\n7 * 4 = 28\n7 * 5 = 35\n"
                         "7 * 6 = 42\n7 * 7 = 49\n7 * 8 = 56\n7 * 9 = 63\n7 * 10 = 70"),
            TestCase("9", "9 * 1 = 9\n9 * 2 = 18\n9 * 3 = 27\n9 * 4 = 36\n9 * 5 = 45\n"
                         "9 * 6 = 54\n9 * 7 = 63\n9 * 8 = 72\n9 * 9 = 81\n9 * 10 = 90"),
            TestCase("10", "10 * 1 = 10\n10 * 2 = 20\n10 * 3 = 30\n10 * 4 = 40\n10 * 5 = 50\n"
                          "10 * 6 = 60\n10 * 7 = 70\n10 * 8 = 80\n10 * 9 = 90\n10 * 10 = 100"),
        ],
    ),
    TaskConfig(
        task_id="43",
        name="Лесенка",
        filename="Задание 43.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase("1", "1"),
            TestCase("2", "1\n12"),
            TestCase("3", "1\n12\n123"),
            TestCase("4", "1\n12\n123\n1234"),
            TestCase("5", "1\n12\n123\n1234\n12345"),
            TestCase("9", "1\n12\n123\n1234\n12345\n123456\n1234567\n12345678\n123456789"),
        ],
    ),
    TaskConfig(
        task_id="44",
        name="Лесенка 2",
        filename="Задание 44.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase("1", "1"),
            TestCase("2", "21\n2"),
            TestCase("3", "321\n32\n3"),
            TestCase("4", "4321\n432\n43\n4"),
            TestCase("5", "54321\n5432\n543\n54\n5"),
            TestCase("9", "987654321\n98765432\n9876543\n987654\n98765\n9876\n987\n98\n9"),
        ],
    ),
    TaskConfig(
        task_id="45",
        name="Таблица Пифагора",
        filename="Задание 45.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=_pythagorean_validator,
        test_cases=[
            TestCase("1", 1),
            TestCase("2", 2),
            TestCase("3", 3),
            TestCase("4", 4),
            TestCase("5", 5),
            TestCase("10", 10),
        ],
    ),
    TaskConfig(
        task_id="416",
        name="Треугольная последовательность",
        filename="Задание 416.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase("1", "1"),
            TestCase("2", "1 2"),
            TestCase("3", "1 2 2"),
            TestCase("5", "1 2 2 3 3"),
            TestCase("6", "1 2 2 3 3 3"),
            TestCase("7", "1 2 2 3 3 3 4"),
            TestCase("10", "1 2 2 3 3 3 4 4 4 4"),
            TestCase("15", "1 2 2 3 3 3 4 4 4 4 5 5 5 5 5"),
        ],
    ),
    TaskConfig(
        task_id="418",
        name="Числа Фибоначчи",
        filename="Задание 418.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase("1", "1"),
            TestCase("2", "1 1"),
            TestCase("5", "1 1 2 3 5"),
            TestCase("7", "1 1 2 3 5 8 13"),
            TestCase("10", "1 1 2 3 5 8 13 21 34 55"),
            TestCase("15", "1 1 2 3 5 8 13 21 34 55 89 144 233 377 610"),
        ],
    ),
    TaskConfig(
        task_id="417",
        name="Анализ последовательности",
        filename="Задание 417.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=exact_match,
        test_cases=[
            TestCase(
                "5\n3\n-1\n0\n5\n-2",
                "Нулей: 1\nОтрицательных: 2\nСреднее положительных: 4.00",
            ),
            TestCase(
                "6\n1\n2\n3\n-1\n-2\n0",
                "Нулей: 1\nОтрицательных: 2\nСреднее положительных: 2.00",
            ),
            TestCase(
                "3\n10\n20\n30",
                "Нулей: 0\nОтрицательных: 0\nСреднее положительных: 20.00",
            ),
            TestCase(
                "4\n0\n0\n-3\n6",
                "Нулей: 2\nОтрицательных: 1\nСреднее положительных: 6.00",
            ),
            TestCase(
                "5\n-5\n-10\n0\n0\n7",
                "Нулей: 2\nОтрицательных: 2\nСреднее положительных: 7.00",
            ),
            TestCase(
                "4\n1\n2\n3\n4",
                "Нулей: 0\nОтрицательных: 0\nСреднее положительных: 2.50",
            ),
        ],
    ),
]

if __name__ == "__main__":
    result = run_module("Цикл for", TASKS, _BASE_DIR)
    sys.exit(0 if result.solved_tasks == result.total_tasks else 1)
