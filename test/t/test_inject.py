import pytest


@pytest.mark.pre_commands(
    'PATH=$PATH:/usr/lib/mailman/bin',
)
class Test(object):

    @pytest.mark.complete("inject ")
    def test_(self, completion):
        assert completion.list