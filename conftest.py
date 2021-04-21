import os

import settings

from api import _load_api_dsl, _load_api_dsl_depend


def pytest_sessionstart(session):
    settings.setup()


def setup():
    global _all_testcases, _api_descriptor
    if _all_testcases:
        return

    env = os.getenv('ENV', None)
    if not env or env not in ('stage', 'sandbox', 'prod',):
        raise Exception('Environment is not configured. Sould be stage, sandbox, or prod.')
    _load_api_dsl(env)  # 加载接口配置信息（metadata/api.yml）
    _load_api_dsl_depend(env)
