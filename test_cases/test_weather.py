import pytest
import requests


def test_baidu_result():
    url = "http://www.baidu.com"
    # 部分网站需要代理
    # headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
    # data1 = urllib.request.Request(url, headers=headers)
    # data = urllib.request.urlopen(data1).read()
    res = requests.post(url)
    assert 302 == res.status_code


def test_weather_result():
    url = "http://www.weather.com.cn/data/cityinfo/101190408.html"
    res = requests.get(url)
    res.encoding = 'utf-8'
    # print(res.text)
    city = res.json().get('weatherinfo').get('city')
    assert "太仓" == city


if __name__ == '__main__':
    pytest.main(['-s', 'test_weather.py'])