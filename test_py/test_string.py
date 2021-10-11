from .. import minipy as py

s1 = "122333444455555"
s2 = "1111"
s3 = "0"
s4 = ""

class TestString:
    def test_self_string(self):
        assert py.SingleString(s1).string == s1
        assert py.SingleString(s2).string == s2
        assert py.SingleString(s3).string == s3
        assert py.SingleString(s4).string == s4

    def test_maxPower(self):
        assert py.SingleString(s1).maxPower() == 5
        assert py.SingleString(s2).maxPower() == 4
        assert py.SingleString(s3).maxPower() == 1
        assert py.SingleString(s4).maxPower() == 0
