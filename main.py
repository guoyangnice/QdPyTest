import requests


def test_user_reg():
    url = "http://www.baidu.com"
    # 部分网站需要代理
    # headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
    # data1 = urllib.request.Request(url, headers=headers)
    # data = urllib.request.urlopen(data1).read()
    res = requests.post(url)
    assert 302 == res.status_code


if __name__ == '__main__':
    test_user_reg()
