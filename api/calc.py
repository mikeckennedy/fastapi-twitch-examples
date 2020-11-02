import asyncio
from typing import Optional

import fastapi
import pydantic

router = fastapi.APIRouter()


class Vector(pydantic.BaseModel):
    x: int
    y: int
    z: Optional[int] = None


class Result(pydantic.BaseModel):
    result: int
    x: int
    y: int
    z: Optional[int]


@router.get('/api/calculate')
async def calculate(x: int, y: int, z: Optional[int] = None):
    # https://github.com/encode/httpx
    # await Calling twitch api
    # await saving to db
    # await asyncio.sleep(.001)
    prod = x * y
    if z:
        prod *= z * 10

    return Result(result=prod, x=x, y=y, z=z)


@router.post('/api/sum')
def sum_it(v: Vector):
    addition = v.x + v.y
    if v.z:
        addition += v.z

    return Result(result=addition, x=v.x, y=v.y, z=v.z)
