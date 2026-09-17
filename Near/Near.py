

def near(x, y, diff = .1):
        
        
    return abs(x-y) < diff


def test_near():
    
    assert near (10, 10.09)
    assert near (10.09, 10)
    assert near (10, 10.11) == False
    assert near (-10, -10.99)
    assert near (-10, -10.11) == False
    
    
    print('Tests Passed')