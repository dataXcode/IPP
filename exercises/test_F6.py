def test():
    # Test
    assert("for key, value in countries.items()" in __solution__ or "for key, value in countries.items( )" in __solution__
           ), "اجابة خاطئة: هناك خطأ في صناعة اللوب"

    assert("print('the capital of ' + str(key) + ' is ' + str(value))" in __solution__ or "print('the capital of ' + str(key) + ' is ' + str(value) )" in __solution__
           or "print('the capital of ' + str( key) + ' is ' + str(value))" in __solution__ or "print('the capital of ' + str(key ) + ' is ' + str(value))" in __solution__ or "print('the capital of ' + str( key ) + ' is ' + str(value))" in __solution__
           or "print('the capital of ' + str(key) + ' is ' + str( value))" in __solution__ or "print('the capital of ' + str(key) + ' is ' + str(value ))" in __solution__ or "print('the capital of ' + str(key) + ' is ' + str( value ))" in __solution__
           or "print('the capital of ' + str( key) + ' is ' + str( value))" in __solution__ or "print('the capital of ' + str( key) + ' is ' + str(value ))" in __solution__ or "print('the capital of ' + str( key) + ' is ' + str( value ))" in __solution__
           or "print('the capital of ' + str(key ) + ' is ' + str( value))" in __solution__ or "print('the capital of ' + str(key ) + ' is ' + str(value ))" in __solution__ or "print('the capital of ' + str(key ) + ' is ' + str( value ))" in __solution__

           or "print('the capital of ' + str( key) + ' is ' + str(value) )" in __solution__ or "print('the capital of ' + str(key ) + ' is ' + str(value) )" in __solution__ or "print('the capital of ' + str( key ) + ' is ' + str(value) )" in __solution__
           or "print('the capital of ' + str(key) + ' is ' + str( value) )" in __solution__ or "print('the capital of ' + str(key) + ' is ' + str(value ) )" in __solution__ or "print('the capital of ' + str(key) + ' is ' + str( value ) )" in __solution__
           or "print('the capital of ' + str( key) + ' is ' + str( value) )" in __solution__ or "print('the capital of ' + str( key) + ' is ' + str(value ) )" in __solution__ or "print('the capital of ' + str( key) + ' is ' + str( value ) )" in __solution__
           or "print('the capital of ' + str(key ) + ' is ' + str( value) )" in __solution__ or "print('the capital of ' + str(key ) + ' is ' + str(value ) )" in __solution__ or "print('the capital of ' + str(key ) + ' is ' + str( value ) )" in __solution__
           ), "اجابة خاطئة: هناك خطأ في امر الطباعه"
    __msg__.good("اجابة صحيحة. احسنت")
