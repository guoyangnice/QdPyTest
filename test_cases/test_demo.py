# -- coding: utf-8 --

import logging

import pytest

import api
import settings


@pytest.mark.parametrize('api_name, description', [case for case in settings.list_testcases()])
def test_all(api_name, description):
    api_dsl = settings.lookup(api_name)
    requests = settings.resolve(api_name, api_dsl)

    for req in requests:
        resp = api.call(req['url'], req['method'], req['params'], req['headers'])
        result = resp.json()
        # logging.debug(resp.text)
        assert resp.status_code == 200
        if not result['success']:
            assert isinstance(resp.text, object)
            logging.debug(resp.text)
        assert result['success']

