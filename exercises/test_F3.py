def test():
    # Test
    assert("for index, area in enumerate(areas)" in __solution__ or "for index, area in enumerate( areas)" in __solution__ or "for index, area in enumerate(areas )" in __solution__ or "for index, area in enumerate( areas )" in __solution__
           ), "اجابة خاطئة: هناك خطأ في صناعة اللوب"

    assert("'Room ' + str(index + 1) + ': ' + str(area)" in __solution__ or "'Room ' + str(index+1) + ': ' + str(area)" in __solution__ or "'Room ' + str( index + 1) + ': ' + str(area)" in __solution__ or "'Room ' + str( index + 1 ) + ': ' + str(area)" in __solution__
           or "'Room ' + str(index+ 1) + ': ' + str(area)" in __solution__ or "'Room ' + str(index +1) + ': ' + str(area)" in __solution__ or "'Room ' + str( index+1 ) + ': ' + str(area)" in __solution__ or "'Room ' + str( index+ 1) + ': ' + str(area)" in __solution__
           or "'Room ' + str( index +1) + ': ' + str(area)" in __solution__ or "'Room ' + str( index+1) + ': ' + str(area)" in __solution__ or "'Room ' + str(index+1 ) + ': ' + str(area)" in __solution__

           or "'Room ' + str(index + 1) + ': ' + str( area)" in __solution__ or "'Room ' + str(index+1) + ': ' + str( area)" in __solution__ or "'Room ' + str( index + 1) + ': ' + str( area)" in __solution__ or "'Room ' + str( index + 1 ) + ': ' + str( area)" in __solution__
           or "'Room ' + str(index+ 1) + ': ' + str( area)" in __solution__ or "'Room ' + str(index +1) + ': ' + str( area)" in __solution__ or "'Room ' + str( index+1 ) + ': ' + str( area)" in __solution__ or "'Room ' + str( index+ 1) + ': ' + str( area)" in __solution__
           or "'Room ' + str( index +1) + ': ' + str( area)" in __solution__ or "'Room ' + str( index+1) + ': ' + str( area)" in __solution__ or "'Room ' + str(index+1 ) + ': ' + str( area)" in __solution__

           or "'Room ' + str(index + 1) + ': ' + str(area )" in __solution__ or "'Room ' + str(index+1) + ': ' + str(area )" in __solution__ or "'Room ' + str( index + 1) + ': ' + str(area )" in __solution__ or "'Room ' + str( index + 1 ) + ': ' + str(area )" in __solution__
           or "'Room ' + str(index+ 1) + ': ' + str(area )" in __solution__ or "'Room ' + str(index +1) + ': ' + str(area )" in __solution__ or "'Room ' + str( index+1 ) + ': ' + str(area )" in __solution__ or "'Room ' + str( index+ 1) + ': ' + str(area )" in __solution__
           or "'Room ' + str( index +1) + ': ' + str(area )" in __solution__ or "'Room ' + str( index+1) + ': ' + str(area )" in __solution__ or "'Room ' + str(index+1 ) + ': ' + str(area )" in __solution__
           ), "اجابة خاطئة: هناك خطأ في امر الطباعه"
    __msg__.good("اجابة صحيحة. احسنت")
