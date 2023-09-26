from num2tib.core import convert

def test_convert():
    #test int
    assert convert(3) == 'གསུམ་'
    assert convert(1959) == 'གཅིག་སྟོང་དགུ་བརྒྱ་ལྔ་བཅུ་ང་དགུ་'
    assert convert(6000000) == 'ས་ཡ་དྲུག་'
    assert convert(608430)== 'འབུམ་དྲུག་དང་བརྒྱད་སྟོང་བཞི་བརྒྱ་སུམ་ཅུ་'
    

    #test float
    assert convert(3.14) == 'གསུམ་ཚེག་བཅུ་བཞི་'
    assert convert(3.01) == 'གསུམ་ཚེག་ཀླད་ཀོར་གཅིག་'
  
    #test str
    assert convert('1959') == 'གཅིག་སྟོང་དགུ་བརྒྱ་ལྔ་བཅུ་ང་དགུ་'
    assert convert('3.14') == 'གསུམ་ཚེག་བཅུ་བཞི་'
