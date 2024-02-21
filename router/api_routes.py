

from fastapi import APIRouter
from starlette.responses import JSONResponse



router = APIRouter(prefix='', tags=[], responses={404: {"description": "Not found"}})


@router.get("/")
async def health_check():
    return JSONResponse({'message': "health Check"})

