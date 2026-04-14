from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from test_secao5 import TestCaseTest, TestSuiteTest
from test_secao6 import TestLoaderTest
from xunit import TestLoader, TestRunner, TestSuite


if __name__ == "__main__":
    loader = TestLoader()
    test_case_suite = loader.make_suite(TestCaseTest)
    test_suite_suite = loader.make_suite(TestSuiteTest)
    test_loader_suite = loader.make_suite(TestLoaderTest)

    suite = TestSuite()
    suite.add_test(test_case_suite)
    suite.add_test(test_suite_suite)
    suite.add_test(test_loader_suite)

    runner = TestRunner()
    runner.run(suite)
