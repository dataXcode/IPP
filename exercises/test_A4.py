def test():
    # Test
    assert( a == 2 ), "اجابة خاطئة: لم تقم بإنشاء المتغير الاول بشكل صحيح"
    assert( b == 5 ), "اجابة خاطئة: لم تقم بإنشاء المتغير الثاني بشكل صحيح"

    assert("print(a+b)" in __solution__ or "print( a+b )" in __solution__ or "print( a + b )" in __solution__ or "print(a + b)" in __solution__
           or "print( a+b)" in __solution__ or "print(a+b )" in __solution__ or "print(a +b)" in __solution__ or "print(a+ b)" in __solution__
           or "print( a +b )" in __solution__ or "print( a+ b)" in __solution__ or "print(a +b )" in __solution__ or "print(a+ b )" in __solution__
           ), "اجابة خاطئة: لم تقم بطباعة ناتج جمع المتغيرين بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
