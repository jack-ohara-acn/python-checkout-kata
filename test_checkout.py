from checkout import scan, checkout

def empty_scan_test():
    assert checkout() == 0

def test():
    scan('A')
    scan('A')
    scan('A')
    scan('A')
    scan('A')
    scan('A')
    result = checkout()
    assert result == 50