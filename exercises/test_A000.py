def test():
    # Test
    assert("print('مرحباً بك')" in __solution__ or "print('مرحبا بك')" in __solution__ or "print( 'مرحباً بك')" in __solution__ or "print('مرحباً بك' )" in __solution__ or "print( 'مرحباً بك' )" in __solution__
           or 'print("مرحباً بك")' in __solution__ or 'print("مرحبا بك")' in __solution__ or 'print( "مرحباً بك")' in __solution__ or 'print("مرحباً بك" )' in __solution__ or 'print( "مرحباً بك" )' in __solution__
           ), "اجابة خاطئة: لم تقم بطباعة الجملة التي في الاعلى بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
