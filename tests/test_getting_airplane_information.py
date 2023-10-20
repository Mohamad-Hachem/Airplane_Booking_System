from datetime import time
from utils.getting_airplane_information import getting_payload
from unittest.mock import patch


def test_getting_payload():
    # creating our needed inputs
    mock_inputs = [1, "AirFrance", "14:05:20", "16:20:30"]

    # generator that will give me the mock_inputs
    def mock_input_generator():
        for input_value in mock_inputs:
            yield input_value

    mock_input_side_effect = mock_input_generator()

    with patch('builtins.input', side_effect=mock_input_side_effect):
        payload = getting_payload()

    assert payload == {
        "id": 1,
        "company_name": "AirFrance",
        "departure_time": time(14, 5, 20),
        "arrival_time": time(16, 20, 30)
    }
