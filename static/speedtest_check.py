import speedtest


def speed_check():
    test = speedtest.Speedtest(secure=1) #secure переключает запрос на https
    download_speed = round(test.download() / (2 ** 20), 2)
    upload_speed = round(test.upload() / (2 ** 20), 2)
    return [download_speed, upload_speed]
