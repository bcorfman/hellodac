from app.hello import hello_dac


def test_hello_dac():
    assert hello_dac() == 'Hello DAC!'
