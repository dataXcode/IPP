def test():
    # Test
    assert( full == [12.35, 24.5, 31.0, 8.45, 6.4]
           ), "اجابة خاطئة: لم تقم بدمج القائمتين الاولى والثانية بشكل صحيح"

    assert( full_sorted == [31.0, 24.5, 12.35, 8.45, 6.4]
           ), "اجابة خاطئة: لم تقم بعملية الترتيب التنازلي بشكل صحيح"
    
    assert("reverse = True" in __solution__ or "reverse=True" in __solution__ or "reverse =True" in __solution__ or "reverse= True" in __solution__
       ), "اجابة خاطئة: لم تقم بحساب المساحة الكلية للمنزل بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
