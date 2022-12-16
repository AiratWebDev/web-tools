from fastapi import FastAPI, Form, Request, UploadFile, File, Depends
from fastapi.responses import FileResponse, RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session
import crud
import models
from database import engine, get_db

import pytube
import shutil
from pathlib import Path
from static.compress_image import compressor

from static.speedtest_check import *
from static.short_link_generator import link_generator
from static.whois_check import whois_check
from static.translit import *

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')


def download_video(link):
    youtube = pytube.YouTube(link)
    video = youtube.streams.filter(progressive=True).desc().first()
    _path = Path('downloads')
    video.download(_path)  # r'L:\PythonProjects\youtubeDownloader\downloads'
    title = youtube.title
    return title


@app.get('/favicon.ico')
def favicon():
    return FileResponse(f'media/favicon.jpg')


@app.get('/', response_class=HTMLResponse)
def home_get(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})


@app.get('/youtube', response_class=HTMLResponse)
def youtube_get(request: Request):
    return templates.TemplateResponse('youtube.html', {'request': request})


@app.post('/youtube', response_class=HTMLResponse)
def home_post(request: Request, link: str = Form(...)):
    title = download_video(link)
    return templates.TemplateResponse('youtube_post.html', {'request': request, 'title': title, 'link': link})


@app.get('/downloads/{title}', response_class=FileResponse)
def success(title):
    return FileResponse(f'downloads/{title}.mp4')


@app.get('/compress', response_class=HTMLResponse)
def compress(request: Request):
    return templates.TemplateResponse('compress.html', {'request': request})


@app.post('/compress', response_class=HTMLResponse)
def compress_post(request: Request, file: UploadFile = File(...)):
    _name = file.filename
    _path = Path('downloads', 'unoptimized')
    with open(f'downloads/unoptimized/{_name}', 'wb') as buffer:  # downloads/unoptimized/
        shutil.copyfileobj(file.file, buffer)
    _compressed = compressor(_name)
    return templates.TemplateResponse('compressed.html',
                                      {'request': request, 'compressed_link': _compressed, 'file_name': _name})


@app.get('/downloads/optimized/{name}', response_class=FileResponse)
def success(name):
    return FileResponse(f'downloads/optimized/{name}')


@app.get('/s')
def short_url(request: Request):
    return templates.TemplateResponse('short_url.html', {'request': request})


@app.post('/s', response_class=HTMLResponse)
def short_url(request: Request, db: Session = Depends(get_db), link: str = Form(...)):
    [link, short_link] = link_generator(link)
    crud.create_link(db=db, full_link=link, short_link=short_link)
    return templates.TemplateResponse('short_url_post.html',
                                      {'request': request, 'link': link, 'short_link': short_link})


@app.get('/s/{short_link}', response_class=RedirectResponse)
def shorted_url(short_link, db: Session = Depends(get_db)):
    _link = crud.get_link_by_short_link(db=db, short_link=short_link)
    return _link.full_link


@app.get('/speedtest')
def speedtest(request: Request):
    return templates.TemplateResponse('speedtest.html', {'request': request})


@app.post('/speedtest', response_class=HTMLResponse)
def speedtest(request: Request):
    [d_spd, u_spd] = speed_check()
    return templates.TemplateResponse('speedtest_done.html', {'request': request, 'd_spd': d_spd, 'u_spd': u_spd})


@app.get('/whois')
def whois(request: Request):
    return templates.TemplateResponse('whois.html', {'request': request})


@app.post('/whois')
def whois(request: Request, link: str = Form(...)):
    whois_obj = whois_check(link)
    return templates.TemplateResponse('whois_post.html', {'request': request, 'whois_obj': whois_obj})


@app.get('/text')
def text(request: Request):
    return templates.TemplateResponse('text_quantity.html', {'request': request})


@app.get('/password-generator')
def password_generator(request: Request):
    return templates.TemplateResponse('password_generator.html', {'request': request})


@app.get('/translit')
def translit(request: Request):
    return templates.TemplateResponse('translit.html', {'request': request})


@app.post('/translit')
def translit(request: Request, area_text: str = Form(...)):
    result = text_transliteration(area_text)
    return templates.TemplateResponse('translit.html', {'request': request, 'result': result, 'area_text': area_text})


@app.get('static/script-download.js')
def js_script():
    return FileResponse(f'static/script-download.js')


@app.get('/static/script-youtube.js')
def script_home():
    return FileResponse(f'static/script-youtube.js')
