def test():
    # Test
    assert("print(100*1.1**9)" in __solution__ or "print(100 * 1.1**9)" in __solution__ or "print(100 * 1.1 **9)" in __solution__
           or "print( 100*1.1**9 )" in __solution__ or "print( 100 * 1.1**9 )" in __solution__ or "print( 100 * 1.1 **9 )" in __solution__ 
           or "print( 100 * 1.1 **9)" in __solution__ or "print( 100 * 1.1**9)" in __solution__ or "print( 100 * 1.1 **9)" in __solution__
           or "print(100 * 1.1 **9 )" in __solution__ or "print(100 * 1.1**9 )" in __solution__ or "print(100 * 1.1 **9 )" in __solution__
           ), "اجابة خاطئة: العملية الحسابية غير صحيحة"
    __msg__.good("اجابة صحيحة. احسنت")
