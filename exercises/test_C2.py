def test():
    # Test
    assert("name.capitalize()" in __solution__
           ), "اجابة خاطئة: لم تقم بعملية تكبير الحرف الاول من الاسم بشكل صحيح"

    assert("name.count('e')" in __solution__ or 'name.count("e")' in __solution__ or "name.count( 'e' )" in __solution__ or 'name.count( "e" )' in __solution__
           or "name.count( 'e')" in __solution__ or 'name.count( "e")' in __solution__ or "name.count('e' )" in __solution__ or 'name.count("e" )' in __solution__
           ), "اجابة خاطئة: لم تقم بعملية حساب عدد مرات ظهور حرف اي بشكل صحيح"

    assert('name.replace("e", "i")' in __solution__ or "name.replace('e', 'i')" in __solution__ 
           or 'name.replace("e","i")' in __solution__ or "name.replace('e','i')" in __solution__ 
           or 'name.replace( "e" , "i" )' in __solution__ or "name.replace( 'e' , 'i' )" in __solution__
           or 'name.replace( "e","i" )' in __solution__ or "name.replace( 'e','i' )" in __solution__
           or 'name.replace( "e", "i" )' in __solution__ or "name.replace( 'e', 'i' )" in __solution__
           ), "اجابة خاطئة: لم تقم بعملية استبدال الحروف بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
