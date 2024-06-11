import pytest
import os
from datetime import datetime

@pytest.fixture(autouse=False, scope="function")
def login():
    print("---登录前(全局)")
    yield
    print("---登录后(全局)")

# 动态生成log文件的名称，哪怕配置文件中配置了log_file = ./log/test.log也不会生效
def pytest_configure(config):
    time_now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    config.option.log_file = os.path.join(config.rootdir, 'log', f'{time_now}.log')