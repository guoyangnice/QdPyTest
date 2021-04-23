import pytest
import requests


class TestRequestsDemo:
    # 初始化
    url = "http://baidu.com"
    session = requests.session()

    # 测试获得所有用户信息接口
    def test_get_posts(self):
        r = self.session.post(self.url)
        # 断言状态码
        assert r.status_code == 200
        # 断言响应头信息
        assert r.headers['Content-Type'] == "text/html"


if __name__ == '__main__':
    pytest.main(['-s', 'testBaiDu.py'])
