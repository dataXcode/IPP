def test():
    # Test
    assert( areas[3] == 13.5
           ), "اجابة خاطئة: لم تقم بتغيير مساحة المطبخ بشكل صحيح"

    assert( areas[4] == "study room"
           ), "اجابة خاطئة: لم تقم بتغيير غرفة المعيشة الى غرفة الدراسة بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
