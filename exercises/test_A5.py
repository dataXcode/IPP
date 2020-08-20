def test():
    # Test
    assert( savings == 100 ), "اجابة خاطئة: لم تقم بإنشاء المتغير الاول بشكل صحيح"
    assert( factor == 1.1 ), "اجابة خاطئة: لم تقم بإنشاء المتغير الثاني بشكل صحيح"
    assert( round(result) == 236 ), "اجابة خاطئة: لم تقم بإنشاء المتغير الثالث بشكل صحيح"
    assert("print(result)" in __solution__ or "print( result )" in __solution__ or "print( result)" in __solution__ or "print(result )" in __solution__
           ), "اجابة خاطئة: لم تقم بطباعة الناتج بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
