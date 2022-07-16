from ge import endpoints


def test_mapping():
    assert endpoints.mapping().status_code == 200


def test_format_data():
    test_data = {"data": {"5": 55}}
    goal = {"5": 55}
    second_test_data = {"data": {"5": 55}, "timestamp": 5555}
    second_goal = {"data": {"5": 55,}, "timestamp": 5555}
    assert endpoints.format_data(test_data) == goal
    assert endpoints.format_data(second_test_data) == second_goal
