def test():
    # Test
    assert( downstairs == ['hallway', 14.35, 'kitchen', 15.0, 'living room', 19.0]
           ), "اجابة خاطئة: لم تقم بأنشاء متغير الطابق السفلي بشكل صحيح"
    assert( upstairs == ['bedroom', 12.5, 'bathroom', 8.75]
           ), "اجابة خاطئة: لم تقم بأنشاء متغير الطابق العلوي بشكل صحيح"

    assert("areas[:6]" in __solution__ or "areas[0:6]" in __solution__ 
           ), "اجابة خاطئة: لم تقم بأنشاء متغير الطابق السفلي بشكل صحيح"
    assert("areas[-4:]" in __solution__
           ), "اجابة خاطئة: لم تقم بأنشاء متغير الطابق العلوي بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
