def test():
    # Test
    assert('elif room == "bed":' in __solution__ or "elif room == 'bed':" in __solution__ or 'elif room== "bed":' in __solution__ or 'elif room =="bed":' in __solution__ or 'elif room=="bed":' in __solution__
           or "elif room== 'bed':" in __solution__ or "elif room =='bed':" in __solution__ or "elif room=='bed':" in __solution__
           or 'elif room == "bed" :' in __solution__ or "elif room == 'bed' :" in __solution__ or 'elif room== "bed" :' in __solution__ or 'elif room =="bed" :' in __solution__ or 'elif room=="bed" :' in __solution__
           or "elif room== 'bed' :" in __solution__ or "elif room =='bed' :" in __solution__ or "elif room=='bed' :" in __solution__
           ), "اجابة خاطئة: لم تقم بصناعة الشرط بشكل صحيح"

    assert('print("looking around in the bedroom.")' in __solution__ or "print('looking around in the bedroom.')" in __solution__
           ), "اجابة خاطئة: هناك خطأ في امر الطباعة او الجملة"

    assert("else:" in __solution__ or "else :" in __solution__
           ), "اجابة خاطئة: هناك خطأ في شرط الاخر"

    assert('print("looking around elsewhere.")' in __solution__ or "print('looking around elsewhere.')" in __solution__
           ), "اجابة خاطئة: هناك خطأ في امر الطباعة او الجملة"
    __msg__.good("اجابة صحيحة. احسنت")
