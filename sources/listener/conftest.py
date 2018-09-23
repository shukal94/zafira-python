import pytest


@pytest.hookimpl
def pytest_runtestloop(session):
    print('session started', session)


@pytest.hookimpl
def pytest_runtest_call(item):
    print('test started', item)


@pytest.hookimpl
def pytest_runtest_teardown(item):
    print('\ntest finished', item)

@pytest.hookimpl
def pytest_sessionfinish(session, exitstatus):
    print('session finished', session, exitstatus)


