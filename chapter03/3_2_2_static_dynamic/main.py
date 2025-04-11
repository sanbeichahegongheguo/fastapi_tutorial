#!/usr/bin/evn python
# -*- coding: utf-8 -*-

from fastapi import FastAPI
from fastapi import APIRouter
from starlette.responses import JSONResponse

app = FastAPI(routes=None)


# ============一个URL配置多个HTTP请求方法==========
# =========================================
@app.api_route(path="/index", methods=["GET", "POST"])
async def index():
    return {"index": "index"}


async def index2():
    return JSONResponse({"index": "index2"})


app.add_api_route(path="/index2", endpoint=index2, methods=["GET", "POST"])


if __name__ == "__main__":
    import uvicorn
    import os

    app_model_name = os.path.basename(__file__).replace(".py", "")
    print(app_model_name)
    uvicorn.run(f"{app_model_name}:app", host="127.0.0.1", reload=True)
