import pytest
from answer_testing_ferst_kt import concat_total


# @pytest.mark.xfail()
@pytest.mark.parametrize('avg, avg_in_grades',concat_total())
def test_avg(avg, avg_in_grades):
    assert avg == avg_in_grades