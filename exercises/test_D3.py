def test():
    # Test
    assert('"Lebanon" in countries' in __solution__ or "'Lebanon' in countries" in __solution__ 
           ), "اجابة خاطئة: لم تقم بالتحقق من وجود دولة لبنان بشكل صحيح"

    assert('countries["Lebanon"] = "Beirut"' in __solution__ or "countries['Lebanon'] = 'Beirut'" in __solution__ 
           or 'countries["Lebanon"]="Beirut"' in __solution__ or "countries['Lebanon']='Beirut'" in __solution__ 
           or 'countries["Lebanon"] ="Beirut"' in __solution__ or "countries['Lebanon'] ='Beirut'" in __solution__ 
           or 'countries["Lebanon"]= "Beirut"' in __solution__ or "countries['Lebanon']= 'Beirut'" in __solution__ 
           ), "اجابة خاطئة: لم تقم بأضافة دولة لبنان وعاصمتها بيروت بشكل صحيح"

    assert('del(countries["Lebanon"])' in __solution__ or "del(countries['Lebanon'])" in __solution__ 
           ), "اجابة خاطئة: لم تقم بحذف دولة لبنان بشكل صحيح"

    assert('countries["Iraq"] = "Basra"' in __solution__ or "countries['Iraq'] = 'Basra'" in __solution__ 
           or 'countries["Iraq"]="Basra"' in __solution__ or "countries['Iraq']='Basra'" in __solution__ 
           or 'countries["Iraq"] ="Basra"' in __solution__ or "countries['Iraq'] ='Basra'" in __solution__ 
           or 'countries["Iraq"]= "Basra"' in __solution__ or "countries['Iraq']= 'Basra'" in __solution__ 
           ), "اجابة خاطئة: لم تقم بتغيير عاصمة العراق من بغداد الى البصرة بشكل صحيح"
    __msg__.good("اجابة صحيحة. احسنت")
