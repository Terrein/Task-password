def get_absolute_url(url, *args, **kwargs):
    """ Сборка url-адресса по входящим параметрам. 
    :param ulr: обязательный аргумент.
    :param *args: позиционный(е) аргумент(ы). Возможен ввод любого кол-ва аргументов
    :param **kwargs: именованный(е) аргумент(ы). Возможен ввод любого кол-ва аргументов
    """  
    z = ""
    for el in args:
        z += el.strip() + "/"
    z = z + "?"
    for k, v in kwargs.items():
        z += ((k.strip()) + "=" + str(v).strip() + "&")
    z = z[:-1]
    return(url + "/" + z)

# https://www.da-office.ru/store/zashitnii-kovriki-pod-kreslo/bsl-100-x-120-sm-1-2-mm-matovyy-pesok-polipropilen/?utm_source=YM&utm_medium=cpc&utm_content=bsl-100-x-120-sm-1-2-mm-matovyy-pesok-polipropilen&utm_campaign=zashitnii-kovriki-pod-kreslo&r1=&ymclid=16012405962867952112500007
#Тестовый вывод
print(get_absolute_url('www.da-office.ru', 'store', 'zashitnii-kovriki-pod-kreslo', 'bsl-100-x-120-sm-1-2-mm-matovyy-pesok-polipropilen', utm_source='YM',
                       utm_medium='cpc', utm_content='bsl-100-x-120-sm-1-2-mm-matovyy-pesok-polipropilen', 
                       utm_campaign='zashitnii-kovriki-pod-kreslo', r1='', ymclid=16012405962867952112500007))
#Тестовый вывод
print(get_absolute_url('yandex.ru','news', utm_source='main_stripe_big'))


