def test():
    # Test
    assert(max_min_first_last([70, 79, 88, 31, 24, 95]) == (95, 24, 70, 95)
           ), "اجابة خاطئة: هناك خطأ في صناعة الوظيفه"
    __msg__.good("اجابة صحيحة. احسنت")