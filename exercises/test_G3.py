def test():
    # Test
    assert(car1.description() == "Car name: BMW Color: Red Price: 40000"
           ), "اجابة خاطئة: هناك خطأ في صناعة الاوبجكت"

    assert(car2.description() == "Car name: Mercedes Color: White Price: 50000"
           ), "اجابة خاطئة: هناك خطأ في صناعة الاوبجكت"

    assert("print(car1.description())" in __solution__ or "print( car1.description())" in __solution__ or "print(car1.description() )" in __solution__ or "print( car1.description() )" in __solution__
           or "print(car1.description( ))" in __solution__ or "print( car1.description( ))" in __solution__ or "print(car1.description( ) )" in __solution__ or "print( car1.description( ) )" in __solution__
           ), "اجابة خاطئة: هناك خطأ في امر الطباعه"

    assert("print(car2.description())" in __solution__ or "print( car2.description())" in __solution__ or "print(car2.description() )" in __solution__ or "print( car2.description() )" in __solution__
           or "print(car2.description( ))" in __solution__ or "print( car2.description( ))" in __solution__ or "print(car2.description( ) )" in __solution__ or "print( car2.description( ) )" in __solution__
           ), "اجابة خاطئة: هناك خطأ في امر الطباعه"
    __msg__.good("اجابة صحيحة. احسنت")
