from fastapi                    import FastAPI
from db.database                import engine, create_all_tables
from fastapi.middleware.cors    import CORSMiddleware
from app.main.routers           import duenoMascota, paseador, paseo, servicio, estilizado, mascota, enfermeria  

app     = FastAPI()
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins       =origins,
    allow_credentials   =True,
    allow_methods       =["*"],
    allow_headers       =["*"]
)

create_all_tables(engine)

app.include_router(duenoMascota.router, prefix="/duenoMascota", tags=["duenoMascota"])
app.include_router(paseador.router,     prefix="/paseador",     tags=["paseador"])
app.include_router(paseo.router,        prefix="/paseo",        tags=["paseo"])
app.include_router(servicio.router,     prefix="/servicio",     tags=["servicio"])
app.include_router(estilizado.router,   prefix="/estilizado",   tags=["estilizado"])
app.include_router(mascota.router,      prefix="/mascota",      tags=["mascota"])
app.include_router(enfermeria.router,   prefix="/enfermeria",   tags=["enfermeria"])
