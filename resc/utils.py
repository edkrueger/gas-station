"""
functions used by Simulator class for parameter validation

yields: None

"""


def validate_params(params):
    """Checks parameters passed to Simulator object for completeness and type"""

    key_type_dict = {
        "expected_wait": (float, int),  # in minutes,
        "gas_required_mean": (float, int),  # in gallons
        "gas_required_std": (float, int),  # in gallons
        "pump_rate": (float, int),  # in gallons per minute
        "expected_lay_time": (float, int),  # in minutes
        "sim_time": (float, int),  # in minutes
        "num_pumps": int,
    }

    if not set(key_type_dict) == set(params):
        missing_keys = ", ".join(list(set(key_type_dict) - set(params)))
        raise ValueError(
            "params is missing key-value pairs for: {}".format(missing_keys)
        )

    for key in key_type_dict:
        if not isinstance(params[key], key_type_dict[key]):
            raise ValueError(
                "Value for {} must be of type {}.".format(key, key_type_dict[key])
            )
