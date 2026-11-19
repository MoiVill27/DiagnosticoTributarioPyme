import os

from fastapi import FastAPI

app = FastAPI(title="Diagnóstico Tributario Pyme")


@app.get("/")
def inicio():
    return {"estado": "ok", "mensaje": "Diagnóstico tributario: funcionando"}


@app.get("/salud")
def salud():
    return {"estado": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
