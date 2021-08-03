def test():
    # Test
    assert('elif area > 10:' in __solution__ or 'elif area> 10:' in __solution__ or 'elif area >10:' in __solution__ or 'elif area>10:' in __solution__
           or 'elif area > 10 :' in __solution__ or 'elif area> 10 :' in __solution__ or 'elif area >10 :' in __solution__ or 'elif area>10 :' in __solution__
           ), "اجابة خاطئة: لم تقم بصناعة الشرط بشكل صحيح"

    assert('print("medium size, nice!")' in __solution__ or "print('medium size, nice!')" in __solution__
           ), "اجابة خاطئة: هناك خطأ في امر الطباعة او الجملة"

    assert("else:" in __solution__ or "else :" in __solution__
           ), "اجابة خاطئة: هناك خطأ في شرط الاخر"   

    assert('print("pretty small.")' in __solution__ or "print('pretty small.')" in __solution__
           ), "اجابة خاطئة: هناك خطأ في امر الطباعة او الجملة"   
    __msg__.good("اجابة صحيحة. احسنت")
