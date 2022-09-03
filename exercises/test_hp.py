def test():
    # Test
    assert( area == 15 ), "اجابة خاطئة: لم تقم بحساب مساحة المستطيل بشكل صحيح"
    assert("print(area)" in __solution__ or "print (area)" in __solution__ or "print( area)" in __solution__ or "print(area )" in __solution__
           or "print( area )" in __solution__ or "print ( area)" in __solution__ or "print (area )" in __solution__ or "print ( area )" in __solution__ 
           ), "اجابة خاطئة: لم تقم بطباعة مساحة المستطيل بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
