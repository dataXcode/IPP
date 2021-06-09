def test():
    # Test
    assert( students == {'Ahmed': 87, 'Waleed': 69, 'Hesham': 92, 'Khaled': {'Math': 86, 'English': 74}}
           ), "اجابة خاطئة: لم تقم باضافة الطالب خالد ودرجاته الى قاموس الطلاب بشكل صحيح"

    assert('students["Khaled"]["English"]' in __solution__ or "students['Khaled']['English']" in __solution__ 
           or 'students["Khaled"] ["English"]' in __solution__ or "students['Khaled'] ['English']" in __solution__ 
           ), "اجابة خاطئة: لم تقم بطباعة درجة خالد في اللغة الانجليزية بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
