import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
sys.stdout.reconfigure(encoding="utf-8")

from tester import TaskConfig, TestCase, float_close, multi_value, run_module

_BASE_DIR = os.path.dirname(__file__)

TASKS = [
    TaskConfig(
        task_id="101",
        name="Расстояние между точками",
        filename="Задание 101.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=float_close(tolerance=1e-2),
        test_cases=[
            TestCase("0\n0\n3\n4", 5.0),
            TestCase("-1\n1\n2\n5", 5.0),
            TestCase("1\n1\n1\n4", 3.0),
            TestCase("0\n0\n0\n0", 0.0),
            TestCase("-1\n-2\n1\n2", 4.4721),
            TestCase("1.5\n2.3\n4.8\n6.7", 5.5),
        ],
    ),
    TaskConfig(
        task_id="102",
        name="Площадь треугольника",
        filename="Задание 102.py",
        time_limit=5.0,
        memory_limit_bytes=64 * 1024 * 1024,
        forbidden_constructs=[],
        check_pep8=True,
        validator=multi_value((float, 0.1), (float, 0.1)),
        test_cases=[
            TestCase("0\n0\n3\n0\n0\n4", (12.0,  6.0)),
            TestCase("1\n1\n2\n5\n5\n3", (12.2,  7.0)),
            TestCase("0\n0\n10\n0\n5\n5", (24.14, 25.0)),
        ],
    ),
]

if __name__ == "__main__":
    result = run_module("Введение", TASKS, _BASE_DIR)
    sys.exit(0 if result.solved_tasks == result.total_tasks else 1)
