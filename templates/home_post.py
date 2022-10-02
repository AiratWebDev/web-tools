def home_page_html(title, link):
    html_content = f"""
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
            <script src="/static/script-download.js" type="text/javascript"></script>
            <link rel="stylesheet" href="/static/styles.css">
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
    return html_content
