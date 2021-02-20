def test():
    # Test
    assert("'hello world'" in __solution__ or "'Hello World'" in __solution__ or "'Hello world'" in __solution__ or "'HELLO WORLD'" in __solution__
           or '"hello world"' in __solution__ or '"Hello World"' in __solution__ or '"Hello world"' in __solution__ or '"HELLO WORLD"' in __solution__
           ), "اجابة خاطئة: لم تقم بطباعة الجملة المطلوبة بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
