from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from xunit import TestCase, TestResult


class MyTest(TestCase):
    def test_a(self):
        assert True

    def test_b(self):
        assert True

    def test_c(self):
        assert True


if __name__ == "__main__":
    result = TestResult()

    test = MyTest("test_a")
    test.run(result)

    test = MyTest("test_b")
    test.run(result)

    test = MyTest("test_c")
    test.run(result)

    print(result.summary())
