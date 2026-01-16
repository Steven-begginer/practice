from src.twttr import short

def main():
    test_uppercase()
    test_lowercase()

def test_uppercase():
    assert short("A") == 'Output: '
    assert short("E") == 'Output: '
    assert short("I") == 'Output: '
    assert short("O") == 'Output: '
    assert short("U") == 'Output: '

def test_lowercase():
    assert short("a") == 'Output: '
    assert short("e") == 'Output: '
    assert short("i") == 'Output: '
    assert short("o") == 'Output: '
    assert short("u") == 'Output: '

if __name__ == "__main__":
    main()