import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
sys.stdout.reconfigure(encoding="utf-8")

from tester import TaskConfig, TestCase, exact_match, multi_value, run_module

_BASE_DIR = os.path.dirname(__file__)


def _hms_validator(output: str, expected):
    exp_h, exp_m, exp_s = expected
    expected_str = f"{exp_h}:{exp_m}:{exp_s}"
    if output == expected_str:
        return True, ""
    return False, f"Неверный формат или значение: ожидалось «{expected_str}»"


TASKS = [
    TaskConfig(
        task_id="201",
        name="Секунды",
        filename="Задание 201.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=_hms_validator,
        test_cases=[
            TestCase("3661", (1,  1,  1)),
            TestCase("365", (0,  6,  5)),
            TestCase("3660", (1,  1,  0)),
            TestCase("7000", (1,  56, 40)),
            TestCase("1", (0,  0,  1)),
            TestCase("60", (0,  1,  0)),
            TestCase("3600", (1,  0,  0)),
            TestCase("86399", (23, 59, 59)),
            TestCase("86400", (24, 0,  0)),
            TestCase("100", (0,  1,  40)),
            TestCase("7384", (2,  3,  4)),
            TestCase("59", (0,  0,  59)),
            TestCase("3599", (0,  59, 59)),
            TestCase("36000", (10, 0,  0)),
        ],
    ),
    TaskConfig(
        task_id="202",
        name="Конец уроков",
        filename="Задание 202.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=multi_value((int, None), (int, None)),
        test_cases=[
            TestCase("1", (9,  45)),
            TestCase("2", (10, 35)),
            TestCase("3", (11, 35)),
            TestCase("4", (12, 25)),
            TestCase("5", (13, 25)),
            TestCase("6", (14, 15)),
            TestCase("7", (15, 15)),
            TestCase("8", (16, 5)),
            TestCase("9", (17, 5)),
            TestCase("10", (17, 55)),
        ],
    ),
]

if __name__ == "__main__":
    result = run_module("Операции деления", TASKS, _BASE_DIR)
    sys.exit(0 if result.solved_tasks == result.total_tasks else 1)
