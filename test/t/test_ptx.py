import pytest


class Test(object):

    @pytest.mark.complete("ptx ")
    def test_(self, completion):
        assert completion.list