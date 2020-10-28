from typing import Optional

import fastapi
import pydantic

router = fastapi.APIRouter()


class Vector:
    x: int
    y: int
    z: Optional[int] = None


class Result(pydantic.BaseModel):
    product: int
    x: int
    y: int
    z: Optional[int]


@router.get('/api/calculate')
def calculate(x: int, y: int, z: Optional[int] = None):
    prod = x * y
    if z:
        prod *= z

    return Result(product=prod, x=x, y=y, z=z)


@router.post('/api/sum')
def sum_it(v: Vector):
    addition = v.x + v.y
    if v.z:
        addition += v.z

    p = Result(product=addition, x=v.x, y=v.y, z=v.z)

    return p
