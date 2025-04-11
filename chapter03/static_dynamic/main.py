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


router_user = APIRouter(prefix="/user", tags=["用户模块"])

@router_user.get("/{user}/login")
def user_login(user):
    return {"ok": f"用户 {user} login登入成功！"}

@router_user.api_route("/{user}/api/login", methods=['GET', 'POST'])
def user_api_route_login(user):
    return {"ok": f"用户 {user} api登入成功！"}

def add_user_api_route_login():
    return {"ok": "登入成功！"}

router_user.add_api_route("/user/add/api/login", methods=['GET', 'POST'], endpoint=add_user_api_route_login)
app.include_router(router_user)

if __name__ == "__main__":
    import uvicorn
    import os

    app_model_name = os.path.basename(__file__).replace(".py", "")
    print(app_model_name)
    uvicorn.run(f"{app_model_name}:app", host='127.0.0.1', reload=True)
