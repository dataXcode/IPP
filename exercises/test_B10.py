def test():
    # Test
    assert( areas_copy == ['hallway', 14.35, 'kitchen', 15.0, 'living room', 19.0, 'bedroom', 12.5, 'bathroom', 10.0]
           ), "اجابة خاطئة: لم تقم بإنشاء نسخة من قائمة المساحات بشكل صحيح او لم تقم بالتعديل المطلوب بشكل صحيح"

    assert( areas == ['hallway', 14.35, 'kitchen', 15.0, 'living room', 19.0, 'bedroom', 12.5, 'bathroom', 8.75]
           ), "اجابة خاطئة: لقد تأثرت قائمة المساحات الاصلية بالتعديل "
    __msg__.good("اجابة صحيحة. احسنت")
