def test():
    # Test
    assert("for room, area in zip(rooms, areas)" in __solution__ or "for room, area in zip(rooms, areas)" in __solution__ or "for room, area in zip( rooms, areas )" in __solution__ 
           or "for room, area in zip(rooms , areas)" in __solution__ or "for room, area in zip( rooms , areas )" in __solution__ or "for room, area in zip(rooms,areas)" in __solution__
           or "for room, area in zip( rooms, areas)" in __solution__ or "for room, area in zip(rooms, areas )" in __solution__ or "for room, area in zip( rooms , areas)" in __solution__
           or "for room, area in zip(rooms , areas )" in __solution__ or "for room, area in zip( rooms,areas )" in __solution__
           ), "اجابة خاطئة: هناك خطأ في صناعة اللوب"

    assert("print(str(room) + ' area is ' + str(area) + 'm')" in __solution__ or "print( str(room) + ' area is ' + str(area) + 'm')" in __solution__
           or "print(str( room) + ' area is ' + str(area) + 'm')" in __solution__ or "print(str(room ) + ' area is ' + str(area) + 'm')" in __solution__ or "print(str( room ) + ' area is ' + str(area) + 'm')" in __solution__
           or "print( str( room) + ' area is ' + str(area) + 'm')" in __solution__ or "print( str(room ) + ' area is ' + str(area) + 'm')" in __solution__ or "print( str( room ) + ' area is ' + str(area) + 'm')" in __solution__
           or "print(str(room) + ' area is ' + str( area) + 'm')" in __solution__ or "print(str(room) + ' area is ' + str(area ) + 'm')" in __solution__ or "print(str(room) + ' area is ' + str( area ) + 'm')" in __solution__
           or "print( str(room) + ' area is ' + str( area) + 'm')" in __solution__ or "print( str(room) + ' area is ' + str(area ) + 'm')" in __solution__ or "print( str(room) + ' area is ' + str( area ) + 'm')" in __solution__
           or "print(str( room) + ' area is ' + str( area) + 'm')" in __solution__ or "print(str( room) + ' area is ' + str(area ) + 'm')" in __solution__ or "print(str( room) + ' area is ' + str( area ) + 'm')" in __solution__
           or "print(str( room ) + ' area is ' + str( area ) + 'm')" in __solution__ or "print( str( room ) + ' area is ' + str( area ) + 'm')" in __solution__
           ), "اجابة خاطئة: هناك خطأ في امر الطباعه"
    __msg__.good("اجابة صحيحة. احسنت")
