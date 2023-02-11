import os
import socket
import subprocess
from typing import Optional

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def shell(cmd):
    ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    return ps.communicate()[0].decode("utf-8").strip()

def get_config():
    pid_count = int(shell("cat /sys/fs/cgroup/pids.current"))-1
    memory_usage = float(shell("cat /sys/fs/cgroup/memory.current"))/1024/1024
    return {
        "Hostname": socket.gethostname(),
        "IP": socket.gethostbyname(socket.gethostname()),
        "PID Count": pid_count,
        "Memory Usage": "{:.2f}MB".format(memory_usage),
    }

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "config": get_config().items()})

@app.get("/json")
def hello_json():
    d = get_config()
    d["Hello"] = "World"
    return d

@app.get("/files", response_class=HTMLResponse)
def hello_json():
    files_basepath = os.getenv('FILES_BASEPATH', "/tmp")
    files = "<h1>Hello Files</h1><br>"
    files += shell("find {}".format(files_basepath)).replace("\n","<br>")
    return files