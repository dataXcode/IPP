def test():
    # Test
    assert( type(t) == tuple
           ), "اجابة خاطئة: لم تقم بتحويل القائمة الى صف بشكل صحيح"

    assert('t[3]["Ali"]' in __solution__ or "t[3]['Ali']" in __solution__ or "t[3] ['Ali']" in __solution__ 
           ), "اجابة خاطئة: لم تقم بطباعة درجة علي بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
