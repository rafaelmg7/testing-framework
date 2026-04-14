from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from test_secao5 import TestCaseTest
from xunit import TestLoader, TestRunner


if __name__ == "__main__":
    loader = TestLoader()
    suite = loader.make_suite(TestCaseTest)

    runner = TestRunner()
    runner.run(suite)
