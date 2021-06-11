def test():
    # Test
    assert( best_friends == {'Ahmed', 'Nor', 'Ali', 'Khaled', 'Waleed'}
           ), "اجابة خاطئة: لم تقم بأضافة احمد الى مجموعة افضل الاصدقاء بشكل صحيح"

    assert( school_friends == {'Ali', 'Sara', 'Waleed'}
           ), "اجابة خاطئة: لم تقم بحذف ياسر من مجموعة اصدقاء المدرسة بشكل صحيح"

    assert( int_friends == {'Ali', 'Waleed'}
           ), "اجابة خاطئة: تقاطع المجموعتين غير صحيح"

    assert( un_friends == {'Ahmed', 'Ali', 'Khaled', 'Nor', 'Sara', 'Waleed'}
           ), "اجابة خاطئة: اتحاد المجموعتين غير صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
