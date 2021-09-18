def test():
    # Test
    assert("for area in areas" in __solution__
           ), "اجابة خاطئة: هناك خطأ في صناعة اللوب"

    assert("print(area)" in __solution__ or "print( area)" in __solution__ or "print(area )" in __solution__ or "print( area )" in __solution__
           ), "اجابة خاطئة: هناك خطأ في امر الطباعه"
    __msg__.good("اجابة صحيحة. احسنت")
