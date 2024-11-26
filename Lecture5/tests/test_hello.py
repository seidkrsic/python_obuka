

from hello import hello  


def test_with_args(): 
    assert hello("Seid") == "hello Seid" 

def test_default(): 
    assert hello() == "hello world" 

