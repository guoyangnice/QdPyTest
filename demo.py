# filename: test_reg.py
import requests
import urllib

def test_user_reg():  # 可以不用写类
    url = "http://www.baidu.com"
    # headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
    # data1 = urllib.request.Request(url, headers=headers)
    # data = urllib.request.urlopen(data1).read()
    res = requests.post(url)
    assert 302 == res.status_code  # 断言使用Python原生assert
if __name__ == '__main__':
    test_user_reg()