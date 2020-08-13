def test():
    # Test
    assert("print(33-33)" in __solution__ or "print( 33-33 )" in __solution__ or "print( 33 - 33 )" in __solution__ or "print(33 - 33)" in __solution__
           or "print( 33-33)" in __solution__ or "print(33-33 )" in __solution__ or "print(33 -33)" in __solution__ or "print(33- 33)" in __solution__
           or "print( 33 -33 )" in __solution__ or "print( 33- 33)" in __solution__ or "print(33 -33 )" in __solution__ or "print(33- 33 )" in __solution__
           ), "اجابة خاطئة: لم تقم بعملية الطرح بشكل صحيح"

    assert("print(3*10)" in __solution__ or "print( 3*10 )" in __solution__ or "print( 3 * 10 )" in __solution__ or "print(3 * 10)" in __solution__
           or "print( 3*10)" in __solution__ or "print(3*10 )" in __solution__ or "print(3 *10)" in __solution__ or "print(3* 10)" in __solution__
           or "print( 3 *10 )" in __solution__ or "print( 3* 10)" in __solution__ or "print(3 *10 )" in __solution__ or "print(3* 10 )" in __solution__
           ), "اجابة خاطئة: لم تقم بعملية الضرب بشكل صحيح"

    assert("print(4**2)" in __solution__ or "print( 4**2 )" in __solution__ or "print( 4**2)" in __solution__ or "print(4**2 )" in __solution__
           ), "اجابة خاطئة: لم تقم بعملية التربيع بشكل صحيح"

    assert("print(60/2)" in __solution__ or "print( 60/2 )" in __solution__ or "print( 60 / 2 )" in __solution__ or "print(60 / 2)" in __solution__
           or "print( 60/2)" in __solution__ or "print(60/2 )" in __solution__ or "print(60 /2)" in __solution__ or "print(60/ 2)" in __solution__
           or "print( 60 /2 )" in __solution__ or "print( 60/ 2)" in __solution__ or "print(60 /2 )" in __solution__ or "print(60/ 2 )" in __solution__
           ), "اجابة خاطئة: لم تقم بعملية القسمة بشكل صحيح"

    assert("print(9//2)" in __solution__ or "print( 9//2 )" in __solution__ or "print( 9 // 2 )" in __solution__ or "print(9 // 2)" in __solution__
           or "print( 9//2)" in __solution__ or "print(9//2 )" in __solution__ or "print(9 //2)" in __solution__ or "print(9// 2)" in __solution__
           or "print( 9 //2 )" in __solution__ or "print( 9// 2)" in __solution__ or "print(9 //2 )" in __solution__ or "print(9// 2 )" in __solution__
           ), "اجابة خاطئة: عملية القسمة بدون كسر غير صحيحة"

    assert("print(9%2)" in __solution__ or "print( 9%2 )" in __solution__ or "print( 9 % 2 )" in __solution__ or "print(9 % 2)" in __solution__
           or "print( 9%2)" in __solution__ or "print(9%2 )" in __solution__ or "print(9 %2)" in __solution__ or "print(9% 2)" in __solution__
           or "print( 9 %2 )" in __solution__ or "print( 9% 2)" in __solution__ or "print(9 %2 )" in __solution__ or "print(9% 2 )" in __solution__
           ), "اجابة خاطئة: لم تقم بحساب باقي القسمة بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
