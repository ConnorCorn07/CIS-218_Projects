import Near

def bavg(atbats, hits):
    return hits / atbats

def test_bavg():
    assert Near.near(.333, bavg(9, 3), 0.001)
    assert Near.near(.300, bavg(10,3), 0.001)
    assert Near.near(.33, bavg(9,3), 0.001) == False
    
    
    
    print('Batting Tests Passed')