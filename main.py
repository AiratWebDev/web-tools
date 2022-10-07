from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import pytube
import subprocess

from templates.home_post import home_page_html
from static.speedtest_check import *
from static import speedtest_check

app = FastAPI()

templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')


def download_video(link):
    youtube = pytube.YouTube(link)
    video = youtube.streams.filter(progressive=True).desc().first()
    result = video.download(r'L:\PythonProjects\youtubeDownloader\downloads')
    title = youtube.title
    return title


@app.get('/', response_class=HTMLResponse)
def home_get(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})


@app.post('/', response_class=HTMLResponse)
def home_post(request: Request, link: str = Form(...)):
    title = download_video(link)
    html_content = home_page_html(title, link)
    return HTMLResponse(content=html_content)


@app.get('/downloads/{title}', response_class=FileResponse)
def success(request: Request, title):
    return FileResponse(f'downloads/{title}.mp4')


@app.get('/speedtest')
def speedtest(request: Request):
    return templates.TemplateResponse('speedtest.html', {'request': request})


@app.post('/speedtest', response_class=HTMLResponse)
async def speedtest(request: Request):
    [d_spd, u_spd] = speed_check()
    return templates.TemplateResponse('speedtest_done.html', {'request': request, 'd_spd': d_spd, 'u_spd': u_spd})


@app.get('static/script-download.js')
def js_script(request: Request):
    return FileResponse(f'static/script-download.js')


@app.get('/static/script_home.js')
def script_home(request: Request):
    return FileResponse(f'static/script_home.js')


@app.get('/favicon.ico')
def favicon(request: Request):
    return FileResponse(f'downloads/favicon.jpg')
