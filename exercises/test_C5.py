def test():
    # Test
    assert("import math" in __solution__
           ), "اجابة خاطئة: لم تقم بأستيراد مكتبة الرياضيات بشكل صحيح"

    assert(round(A, 1) == 0.5), "اجابة خاطئة: لم تقم بحساب المساحة بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")