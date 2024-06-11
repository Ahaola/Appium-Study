import logging
import pytest
logger = logging.getLogger(__name__)


# def test_case():
#     logger.info("这是日志打印————————")
#     assert 1 == 1

def test_b():
    print("---test_b")
    assert 1 == 1

@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_a():
    print("---test_a")
    assert 1 == 2