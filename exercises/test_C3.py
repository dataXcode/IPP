def test():
    # Test
    assert("areas.index(12.5)" in __solution__ or "areas.index( 12.5 )" in __solution__
           or "areas.index( 12.5)" in __solution__ or "areas.index(12.5 )" in __solution__
           ), "اجابة خاطئة: لم تقم بطباعة اندكس الرقم 12.5 بشكل صحيح"

    assert("areas.count(23.5)" in __solution__ or "areas.count( 23.5 )" in __solution__
           or "areas.count( 23.5)" in __solution__ or "areas.count(23.5 )" in __solution__
           ), "اجابة خاطئة: لم تقم بطباعة عدد مرات ظهور الرقم 23.5 بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
