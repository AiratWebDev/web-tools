from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import pytube
import subprocess

from templates.home_post import home_page_html

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


@app.get('static/script-download.js')
def js_script(request: Request):
    return FileResponse(f'static/script-download.js')


@app.get('/static/script_home.js')
def script_home(request: Request):
    return FileResponse(f'static/script_home.js')
