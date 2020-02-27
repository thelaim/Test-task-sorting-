source = [                  #подопотный
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]

expected = {}   # создаем словарь

for key, val in reversed(source):       # итерируем список
    if key not in expected:  
        if key == None:
            continue
        else:
            expected[key] = {}
    if val not in expected:                                                          
        expected[key][val] = {} 
    else:                                              
        expected[key][val] = expected[val].copy()                                               
        del expected[val]  

x = sorted(expected.items()) # переворачиваем словарь

print(x)