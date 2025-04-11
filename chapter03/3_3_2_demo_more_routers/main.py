from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI(routes=None)

router_user = APIRouter(prefix="/user", tags=["用户模块"])
router_pay = APIRouter(prefix="/pay", tags=["支付模块"])

@router_user.get("/{user}/login")
def user_login(user: str):
    return {"user": user, "login": f"{user} login success!"}


@router_pay.post("/{user}/pay")
def user_pay(user: str):
    return {"user": user, "pay": f"{user} pay success!"}

app.include_router(router_user)
app.include_router(router_pay)

if __name__ == "__main__":
    import uvicorn
    import os

    app_model_name = os.path.basename(__file__).replace(".py", "")
    print(app_model_name)
    uvicorn.run(f"{app_model_name}:app", host='127.0.0.1', reload=True)