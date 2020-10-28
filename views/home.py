import datetime

import fastapi

router = fastapi.APIRouter()


@router.get('/')
def index():
    return dict(msg="Hello world", time=datetime.datetime.now().isoformat())


@router.get('/home')
def home():
    msg = 'This is not the home you\'re looking for'
    return fastapi.Response(msg, status_code=302, headers={'location': '/'})
