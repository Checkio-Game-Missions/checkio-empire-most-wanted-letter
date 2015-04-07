from checkio_referee import RefereeRank
from checkio_referee import covercodes, representations, validators


import settings_env
from tests import TESTS


class LetterInValidator(validators.BaseValidator):
    def validate(self, outer_result):
        in_data = self._test["input"]
        if len(in_data) != 2 or not in_data[1]:
            return validators.ValidatorResult(
                isinstance(outer_result, str) and
                len(outer_result) == 1 and
                outer_result in self._test["answer"])
        else:
            return validators.ValidatorResult(
                outer_result == self._test["answer"])


cover = """def cover(f, data):
    return f(*[str(x) if not isinstance(x, bool) else x for x in data])
"""


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    VALIDATOR = LetterInValidator
    DEFAULT_FUNCTION_NAME = "most_letter"
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": cover,
        "javascript": None
    }
    CALLED_REPRESENTATIONS = {
        "python_2": representations.unwrap_arg_representation,
        "python_3": representations.unwrap_arg_representation,
        "javascript": representations.unwrap_arg_representation,
    }
