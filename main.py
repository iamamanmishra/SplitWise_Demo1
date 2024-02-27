import os
import time
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router import api_routes

SERVER_PORT = int(os.getenv("SERVER_PORT", 5090))


def create_app() -> FastAPI:
    current_app = FastAPI(title="FairSplit Application",
                          description="test FairSplit  application ",
                          version="1.0.0", )

    current_app.include_router(api_routes.router)
    return current_app


app = create_app()

origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"], )


@app.middleware("http")
async def add_process_time_header(request, call_next):
    print('inside middleware!')
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(f'{process_time:0.4f} sec')
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=SERVER_PORT, reload=True)
