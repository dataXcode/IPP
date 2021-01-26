def test():
    # Test
    assert("areas.append(17.0)" in __solution__ or "areas.append( 17.0 )" in __solution__
           or "areas.append( 17.0)" in __solution__ or "areas.append(17.0 )" in __solution__
           ), "اجابة خاطئة: لم تقم بأضافة مساحة الكراج الى قائمة المساحات بشكل صحيح"

    assert("areas.remove(19.0)" in __solution__ or "areas.remove( 19.0 )" in __solution__
           or "areas.remove( 19.0)" in __solution__ or "areas.remove(19.0 )" in __solution__
           or "areas.pop(2)" in __solution__ or "areas.pop( 2 )" in __solution__
           or "areas.pop( 2)" in __solution__ or "areas.pop(2 )" in __solution__
           ), "اجابة خاطئة: لم تقم بحذف مساحة غرفة المعيشة من قائمة المساحات بشكل صحيح"

    assert("areas.reverse()" in __solution__
           ), "اجابة خاطئة: لم تقم بعكس ترتيب قائمة المساحات بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
