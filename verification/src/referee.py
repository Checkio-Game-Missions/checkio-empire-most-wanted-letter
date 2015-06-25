from checkio_referee import RefereeRank
from checkio_referee import covercodes, representations, validators, ENV_NAME


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


py_cover = """def cover(f, data):
    return f(*[str(x) if not isinstance(x, bool) else x for x in data])
"""

js_cover = """var cover = function(f, data){
    if (data.length === 1) {
        return f(data[0]);
    else {
        return f(data[0], data[1]);
    }
}"""



class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    VALIDATOR = LetterInValidator
    DEFAULT_FUNCTION_NAME = "most_letter"
    FUNCTION_NAMES = {
        ENV_NAME.JS_NODE: "mostLetter"
    }
    ENV_COVERCODE = {
        ENV_NAME.PYTHON: py_cover,
        ENV_NAME.JS_NODE: js_cover
    }
    CALLED_REPRESENTATIONS = {
        ENV_NAME.PYTHON: representations.unwrap_arg_representation,
        ENV_NAME.JS_NODE: representations.unwrap_arg_representation,
    }
