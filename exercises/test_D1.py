def test():
    # Test
    assert( countries == {'Egypt': 'Cairo',
     'Iraq': 'Baghdad',
     'Jordan': 'Amman',
     'Saudi Arabia': 'Riyadh'}
           ), "اجابة خاطئة: لم تقم بأنشاء قاموس الدول بشكل صحيح"

    assert("countries['Egypt']" in __solution__ or "countries[ 'Egypt' ]" in __solution__ or 'countries["Egypt"]' in __solution__ or 'countries[ "Egypt" ]' in __solution__
           ), "اجابة خاطئة: لم تقم بطباعة عاصمة مصر بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
