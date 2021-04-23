import os

import yaml

_env = None
_api_descriptor = None
_all_testcases = None


# 加载接口配置信息（metadata/api.yml）
def _load_api_dsl(env):
    global _env, _api_descriptor, _all_testcases
    api_dsl = os.path.join('metadata', 'api.yml')
    with open(api_dsl, 'r', encoding='utf-8') as f:
        dsl = yaml.full_load(f)  # dsl是dict类型，存储的是api.yml中所有的接口信息

        _env = dsl['environments'][env]  # 运行环境相对应的登录接口信息
        del dsl['environments']

        _api_descriptor = dict()  # 存储api.yml中接口信息
        testcases = list()  # 存储接口名称（api_name）和描述（description）
        for key, api_dsl in dsl.items():
            if ('skip_test' in api_dsl and api_dsl['skip_test']) or ('depend_on' in api_dsl):
                continue
            desc = api_dsl['description'] if 'description' in api_dsl else ''

            testcases.append((key, desc,), )
            _api_descriptor[key] = api_dsl
        _all_testcases = tuple(testcases)


def _load_api_dsl_depend(env):
    global _env, _api_descriptor_depend, _all_testcases_depend
    api_dsl = os.path.join('metadata', 'api.yml')
    with open(api_dsl, 'r', encoding='utf-8') as f:
        dsl = yaml.full_load(f)  # dsl是dict类型，存储的是api.yml中所有的接口信息

        _env = dsl['environments'][env]  # 运行环境相对应的登录接口信息，参数env可选项包括：sandbox，prod和stage（在tox.ini中配置）
        del dsl['environments']

        _api_descriptor_depend = dict()  # 存储api.yml中接口信息，除了跳过（skip_test）和环境配置（environments）的信息
        testcases = list()  # 存储接口名称（api_name）和描述（description）
        for key, api_dsl in dsl.items():
            if 'depend_on' not in api_dsl:
                continue
            desc = api_dsl['description'] if 'description' in api_dsl else ''

            testcases.append((key, desc,), )
            _api_descriptor_depend[key] = api_dsl
        _all_testcases_depend = tuple(testcases)


# -- coding: utf-8 --

import requests


def call(url, method, params=None, headers=None):
    method = method.lower()
    if method not in ('get', 'post'):
        raise Exception('Invalid request method [%s], should be "get" or "post"' % method)

    if method == 'get':
        return get(url, params, headers)
    elif method == 'post':
        return post(url, params, headers)
    else:
        raise Exception('Should not run into here')


def get(url, params, headers=None):
    resp = requests.get(url, params=params, headers=headers)
    return resp


def post(url, params, headers=None):
    resp = requests.post(url, data=params, headers=headers)
    return resp
