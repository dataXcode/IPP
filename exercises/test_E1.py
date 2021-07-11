def test():
    # Test
    assert("True == False" in __solution__ or "True==False" in __solution__ or "True ==False" in __solution__ or "True== False" in __solution__
           ), "اجابة خاطئة: في النقطة الاولى لم تقم بعملية المقارنة بشكل صحيح"

    assert("-2*10 != 20" in __solution__ or "-2*10!=20" in __solution__ or "-2*10!= 20" in __solution__ or "-2*10 !=20" in __solution__
           or "-2 * 10 != 20" in __solution__ or "-2 *10 != 20" in __solution__ or "-2* 10 != 20" in __solution__
           or "-2 * 10 !=20" in __solution__ or "-2 *10 !=20" in __solution__ or "-2* 10 !=20" in __solution__
           or "-2 * 10!= 20" in __solution__ or "-2 *10!= 20" in __solution__ or "-2* 10!= 20" in __solution__
           ), "اجابة خاطئة: في النقطة الثانية لم تقم بعملية المقارنة بشكل صحيح"

    assert('"python" == "Python"' in __solution__ or '"python"=="Python"' in __solution__ or '"python" =="Python"' in __solution__ or '"python"== "Python"' in __solution__
           or "'python' == 'Python'" in __solution__ or "'python'=='Python'" in __solution__ or "'python' =='Python'" in __solution__ or "'python'== 'Python'" in __solution__
           ), "اجابة خاطئة: في النقطة الثالثة لم تقم بعملية المقارنة بشكل صحيح"

    assert("True == 1" in __solution__ or "True==1" in __solution__ or "True ==1" in __solution__ or "True== 1" in __solution__
           ), "اجابة خاطئة: في النقطة الرابعة لم تقم بعملية المقارنة بشكل صحيح"

    assert("x >= -20" in __solution__ or "x>=-20" in __solution__ or "x >=-20" in __solution__ or "x>= -20" in __solution__
           ), "اجابة خاطئة: في النقطة الخامسة لم تقم بعملية المقارنة بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
