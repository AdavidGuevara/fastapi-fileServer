from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse, JSONResponse
from os import getcwd, remove
from shutil import rmtree

home = APIRouter()


@home.get("/")
def index():
    return "Hello world"


# Subir un archivo:
@home.post("/upload")
async def upload(file: UploadFile = File(...)):
    with open(getcwd() + "/data/" + file.filename, "wb") as myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()
    return "Success"


# Obtener (visualizar) el archivo:
@home.get("/file/{name_file}")
def get_file(name_file: str):
    return FileResponse(getcwd() + "/data/" + name_file)


# Descargar el archivo:
@home.get("/download/{name_file}")
def download_file(name_file: str):
    return FileResponse(
        getcwd() + "/data/" + name_file,
        media_type="application/octet-stream",
        filename=name_file,
    )


# Borrar un archivo:
@home.delete("/delete/{name_file}")
def delete_file(name_file: str):
    try:
        remove(getcwd() + "/data/" + name_file)
        return JSONResponse(
            content={
                "removed": True,
            },
            status_code=200,
        )
    except FileNotFoundError:
        return JSONResponse(
            content={"removed": False, "mesage": "File not found"}, status_code=404
        )


# Borrar una carpeta:
@home.delete("/folder")
def delete_folder(name_folder: str = Form(...)):
    rmtree(getcwd() + "/data/" + name_folder)
    return JSONResponse(
        content={
            "removed": True,
        },
        status_code=404,
    )
