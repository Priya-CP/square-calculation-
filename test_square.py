from square import square
def test_postive_number():
    assert square(5) == 25
    def test_neagtive_number():
        assert square(-4) == 16
        def test_zero():
            assert square(0)==0
            def test_another_number():
                assert square(3)==9