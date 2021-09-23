def test():
    # Test
    assert("for x in house:" in __solution__ or "for x in house :" in __solution__
           ), "اجابة خاطئة: هناك خطأ في صناعة اللوب"

    assert("print(str(x[0]) + ' area is ' + str(x[1]) + 'm')" in __solution__ or "print( str(x[0]) + ' area is ' + str(x[1]) + 'm')" in __solution__
           or "print(str( x[0]) + ' area is ' + str(x[1]) + 'm')" in __solution__ or "print(str(x[0] ) + ' area is ' + str(x[1]) + 'm')" in __solution__ or "print(str( x[0] ) + ' area is ' + str(x[1]) + 'm')" in __solution__
           or "print( str( x[0]) + ' area is ' + str(x[1]) + 'm')" in __solution__ or "print( str(x[0] ) + ' area is ' + str(x[1]) + 'm')" in __solution__ or "print( str( x[0] ) + ' area is ' + str(x[1]) + 'm')" in __solution__
           or "print(str(x[0]) + ' area is ' + str( x[1]) + 'm')" in __solution__ or "print(str(x[0]) + ' area is ' + str(x[1] ) + 'm')" in __solution__ or "print(str(x[0]) + ' area is ' + str( x[1] ) + 'm')" in __solution__
           or "print( str(x[0]) + ' area is ' + str( x[1]) + 'm')" in __solution__ or "print( str(x[0]) + ' area is ' + str(x[1] ) + 'm')" in __solution__ or "print( str(x[0]) + ' area is ' + str( x[1] ) + 'm')" in __solution__
           or "print(str( x[0]) + ' area is ' + str( x[1]) + 'm')" in __solution__ or "print(str( x[0]) + ' area is ' + str(x[1] ) + 'm')" in __solution__ or "print(str( x[0]) + ' area is ' + str( x[1] ) + 'm')" in __solution__
           or "print(str( x[0] ) + ' area is ' + str( x[1] ) + 'm')" in __solution__ or "print( str( x[0] ) + ' area is ' + str( x[1] ) + 'm')" in __solution__
           ), "اجابة خاطئة: هناك خطأ في امر الطباعه"
    __msg__.good("اجابة صحيحة. احسنت")
