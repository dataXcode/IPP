def test():
    # Test
    assert( isinstance(savings, int) ), "اجابة خاطئة: لم تقم بتحويل المتغير الاول بشكل صحيح"
    assert( isinstance(factor, float) ), "اجابة خاطئة: لم تقم بتحويل المتغير الثاني بشكل صحيح"
    assert( isinstance(years, int) ), "اجابة خاطئة: لم تقم بتحويل المتغير الثالث بشكل صحيح"
    assert( savings == 100 ), "اجابة خاطئة: لم تقم بتحويل المتغير الاول بشكل صحيح"
    assert( factor == 1.1 ), "اجابة خاطئة: لم تقم بتحويل المتغير الثاني بشكل صحيح"
    assert( years == 9 ), "اجابة خاطئة: لم تقم بتحويل المتغير الثالث بشكل صحيح"
    assert( result == 235.7947691000002 ), "اجابة خاطئة: لم تقم بإنشاء المتغير الثالث بشكل صحيح"

    assert('print("I started with $" + str(savings) + " and now after " + str(years) + " years I have $" + str(result))' in __solution__ 
           or 'print("I started with $" + str( savings ) + " and now after " + str( years ) + " years I have $" + str( result ))' in __solution__
           or 'print("I started with $" + str( savings) + " and now after " + str( years) + " years I have $" + str( result))' in __solution__
           or 'print("I started with $" + str(savings ) + " and now after " + str(years ) + " years I have $" + str(result ))' in __solution__
           ), "اجابة خاطئة: لم تقم بطباعة الناتج بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
