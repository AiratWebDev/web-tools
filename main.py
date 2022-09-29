from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import pytube
import subprocess

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
    print(title)
    html_content = f"""
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
        <script src="script.js" type="text/javascript"></script>
    </head>
    <body>
    <h1>Поздравляем, ваше видео</h1>
    <p>Если загрузка не началась автоматически — нажмите на ссылку ниже</p>
    <p>{link}</p>
    <p>{title}</p>
    <a class="dnld-link" href="/downloads/{title}" download="{title}">Скачать</a>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get('/downloads/{title}', response_class=FileResponse)
def success(request: Request, title):
    return FileResponse(f'downloads/{title}.mp4')


@app.get('/script.js')
def js_script(request: Request):
    return FileResponse(f'templates/script.js')
