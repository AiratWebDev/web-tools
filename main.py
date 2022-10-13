from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse, RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import pytube
import subprocess

from static.speedtest_check import *
from static import speedtest_check
from static.short_link_generator import link_generator
from static.links_dict import links_dict
from static.whois_check import whois_check
from static.translit import *

app = FastAPI()

templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')


def download_video(link):
    youtube = pytube.YouTube(link)
    video = youtube.streams.filter(progressive=True).desc().first()
    result = video.download(r'L:\PythonProjects\youtubeDownloader\downloads')
    title = youtube.title
    return title


@app.get('/favicon.ico')
def favicon(request: Request):
    return FileResponse(f'media/favicon.jpg')


@app.get('/', response_class=HTMLResponse)
def home_get(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})


@app.post('/', response_class=HTMLResponse)
def home_post(request: Request, link: str = Form(...)):
    title = download_video(link)
    return templates.TemplateResponse('home_post.html', {'request': request, 'title': title, 'link': link})


@app.get('/downloads/{title}', response_class=FileResponse)
def success(request: Request, title):
    return FileResponse(f'downloads/{title}.mp4')


@app.get('/s')
def short_url(request: Request):
    return templates.TemplateResponse('short_url.html', {'request': request})


@app.post('/s', response_class=HTMLResponse)
def short_url(request: Request, link: str = Form(...)):
    [link, short_link] = link_generator(link)
    links_dict[short_link] = link
    return templates.TemplateResponse('short_url_post.html',
                                      {'request': request, 'link': link, 'short_link': short_link})


@app.get('/s/{short_link}', response_class=RedirectResponse)
def shorted_url(request: Request, short_link):
    link = links_dict[short_link]
    return RedirectResponse(link)


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
    return templates.TemplateResponse('translit.html', {'request': request, 'result': result, 'area_text': area_text })


@app.get('static/script-download.js')
def js_script(request: Request):
    return FileResponse(f'static/script-download.js')


@app.get('/static/script_home.js')
def script_home(request: Request):
    return FileResponse(f'static/script_home.js')
