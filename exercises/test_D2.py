def test():
    # Test
    assert("countries.keys()" in __solution__
           ), "اجابة خاطئة: لم تقم بطباعة اسماء الدول بشكل صحيح"

    assert("countries.values()" in __solution__
           ), "اجابة خاطئة: لم تقم بطباعة اسماء العواصم بشكل صحيح"

    assert("countries['Iraq']" in __solution__ or "countries[ 'Iraq' ]" in __solution__ or 'countries["Iraq"]' in __solution__ or 'countries[ "Iraq" ]' in __solution__
           ), "اجابة خاطئة: لم تقم بطباعة عاصمة العراق بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
