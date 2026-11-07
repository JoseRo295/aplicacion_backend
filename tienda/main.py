from fastapi import FastAPI
from db.database import crear_tablas
from controller.auth_controller import router as auth_router
from controller.producto_controller import router as producto_router

app = FastAPI(lifespan=crear_tablas)

app.include_router(auth_router)
app.include_router(producto_router)
