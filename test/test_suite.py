import pytest
from sqlalchemy.testing.suite import *

# Errors
@pytest.mark.skip(reason="The tests of this class use self-reference "
                  "foreign keys which are NOT supported by MonetDB")
class CTETest(CTETest):
    pass

class JSONTest:
    @pytest.mark.skip(reason="MonetDB normalizes json input "
                        "by removing whitespace. "
                        "This is unexpected in this test.")
    def test_round_trip_custom_json(self):
        pass


class LikeFunctionsTest:
    @pytest.mark.skip(reason="monetdb container does not have PCRE")
    def test_regexp_replace(self):
        pass

# FAILED test/test_suite.py::LikeFunctionsTest_monetdb+pymonetdb_11_55_2::test_regexp_replace - sqlalchemy.exc.OperationalError: (pymonetdb.exceptions.OperationalError) Database was compiled without PCRE support.
# │  -# Failures
# │  -class FetchLimitOffsetTest(FetchLimitOffsetTest):
# │  -    @pytest.mark.skip(reason="This test does some LIMIT statements in "
# │  -                      "the middle of the query, this is not supported.")
# │  -    def test_limit_render_multiple_times(*args, **kwargs):
# │  -        """
# │  -        This test does some LIMIT statements in the middle of the query,
# │  -        this is not supported.
# │  -        """
# │  -        pass
# │  -
# │  -