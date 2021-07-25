def test():
    # Test
    assert("my_room > 12 and my_room < 25" in __solution__ or "my_room> 12 and my_room < 25" in __solution__ or "my_room >12 and my_room < 25" in __solution__ or "my_room>12 and my_room < 25" in __solution__
           or "my_room > 12 and my_room< 25" in __solution__ or "my_room > 12 and my_room< 25" in __solution__ or "my_room > 12 and my_room <25" in __solution__ or "my_room>12 and my_room<25" in __solution__
           or "my_room> 12 and my_room< 25" in __solution__ or "my_room> 12 and my_room< 25" in __solution__ or "my_room> 12 and my_room <25" in __solution__ or "my_room> 12 and my_room<25" in __solution__
           or "my_room >12 and my_room< 25" in __solution__ or "my_room >12 and my_room< 25" in __solution__ or "my_room > 12 and my_room <25" in __solution__ or "my_room > 12 and my_room<25" in __solution__
           ), "اجابة خاطئة: في النقطة الاولى لم تقم بعملية المقارنة بشكل صحيح"

    assert("my_room * 2 > your_room * 3" in __solution__ or "my_room* 2 > your_room * 3" in __solution__ or "my_room *2 > your_room * 3" in __solution__ or "my_room*2 > your_room * 3" in __solution__
           or "my_room * 2 > your_room* 3" in __solution__ or "my_room * 2 > your_room *3" in __solution__ or "my_room * 2 > your_room*3" in __solution__ or "my_room*2 > your_room*3" in __solution__
           or "my_room* 2 > your_room* 3" in __solution__ or "my_room* 2 > your_room *3" in __solution__ or "my_room* 2 > your_room*3" in __solution__ or "my_room* 2 > your_room*3" in __solution__
           or "my_room *2 > your_room* 3" in __solution__ or "my_room *2 > your_room *3" in __solution__ or "my_room *2 > your_room*3" in __solution__ or "my_room *2 > your_room*3" in __solution__
           ), "اجابة خاطئة: في النقطة الثانية لم تقم بعملية المقارنة بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
