def test():
    # Test
    assert("10+25" in __solution__ or "10 + 25" in __solution__ or "10 +25" in __solution__ or "10+ 25" in __solution__
           or "25+10" in __solution__ or "25 + 10" in __solution__ or "25 +10" in __solution__ or "25+ 10" in __solution__ 
           ), "اجابة خاطئة: لم تقم بعملية جمع الرقم 10 مع الرقم 25 بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
