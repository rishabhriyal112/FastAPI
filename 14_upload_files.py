from fastapi import FastAPI, UploadFile, HTTPException, File
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

#STep1 : Ensure Uploads folder exist

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

#STep2: STatic File Setup
#URL : HTTP://127.0.0.1:8080/FILES/<Filename>
app.mount("/files",StaticFiles(directory=UPLOAD_DIR),name="files")

#Step3 : Upload file api
@app.post("/upload")
def upload_file(file:UploadFile = File(...)):
    filename= file.filename
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not filename:
        raise HTTPException(status_code=400,detail="File not selected")
    
    with open(file_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
        return{
            "message" : "File Uploaded successfully",
            "filename" : filename,
            "file_url" : f"http://127.0.0.1:8000/files/{filename}"
        }

#Step 4 : Get file url api
@app.get("/files/{filename}")
def get_file(filename:str):
    file_path = os.path.join(UPLOAD_DIR,filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=400,detail="File not Found")
    
    return{
        "file_url" : f"http://127.0.0.1:8000/files/{filename}"
    }

@app.get("/")
def home():
    return {
        "message" : "File Uploaded api Running"
    }
