from real_python_client.api import ReqresClient


def test_do_something_success():
    assert ReqresClient().do_something() == "done"


def test_do_something_failure():
    assert ReqresClient().do_something() == "not done"