def test():
    # Test
    assert("while counter != 0" in __solution__ or "while counter !=0" in __solution__
           ), "اجابة خاطئة: هناك خطأ في صناعة اللوب"

    assert('print("Great job")' in __solution__ or "print('Great job')" in __solution__ or "print( 'Great job')" in __solution__ or "print('Great job' )" in __solution__ or "print( 'Great job' )" in __solution__
           or 'print( "Great job")' in __solution__ or 'print("Great job" )' in __solution__ or 'print( "Great job" )' in __solution__
           ), "اجابة خاطئة: هناك خطأ في طباعة جملة عمل عظيم"

    assert("if counter > 0" in __solution__ or "if counter >0" in __solution__ or "if counter>0" in __solution__ or "if counter> 0" in __solution__
           ), "اجابة خاطئة: هناك خطأ في صناعة الشرط الاول"

    assert("counter = counter - 1" in __solution__ or "counter = counter -1" in __solution__ or "counter = counter- 1" in __solution__ or "counter =counter - 1" in __solution__ or "counter= counter - 1" in __solution__
           or "counter=counter - 1" in __solution__ or "counter= counter- 1" in __solution__ or "counter= counter -1" in __solution__ or "counter= counter-1" in __solution__ or "counter=counter-1" in __solution__
           or "counter=counter -1" in __solution__ or "counter=counter- 1" in __solution__ or "counter=counter - 1" in __solution__
           ), "اجابة خاطئة: هناك خطأ في عداد الشرط الاول"

    assert("else" in __solution__
           ), "اجابة خاطئة: هناك خطأ في صناعة الشرط الاخر"

    assert("counter = counter + 1" in __solution__ or "counter = counter +1" in __solution__ or "counter = counter+ 1" in __solution__ or "counter =counter + 1" in __solution__ or "counter= counter + 1" in __solution__
           or "counter=counter + 1" in __solution__ or "counter= counter+ 1" in __solution__ or "counter= counter +1" in __solution__ or "counter= counter+1" in __solution__ or "counter=counter+1" in __solution__
           or "counter=counter +1" in __solution__ or "counter=counter+ 1" in __solution__ or "counter=counter + 1" in __solution__
           ), "اجابة خاطئة: هناك خطأ في عداد الشرط الاخر"

    assert("print(counter)" in __solution__ or "print( counter)" in __solution__ or "print(counter )" in __solution__ or "print( counter )" in __solution__
       ), "اجابة خاطئة: هناك خطأ في طباعة العداد"
    __msg__.good("اجابة صحيحة. احسنت")
