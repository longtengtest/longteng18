import os
import pytest

from utils.api import Api
from utils.data import Data
from utils.db import LongTengServer


@pytest.fixture(scope='session')
def api(base_url):
    api = Api(base_url)
    return api


@pytest.fixture(scope='session')
def db():
    db = LongTengServer()
    yield db
    db.close()


@pytest.fixture(scope='session')
def data(request):
    root_dir = request.config.rootdir
    file_path = os.path.join(root_dir, 'data', 'data.yaml')
    d = Data(file_path)
    return d.data
