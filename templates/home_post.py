def home_page_html(title, link):
    html_content = f"""
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ваше видео готово</title>
    <script src="/static/script-download.js" type="text/javascript"></script>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
<div class="content">
    <div class="info">
        <h1>Поздравляем, ваше видео готово</h1>
        <p>Название — «{title}»</p>
        <p>Ваша ссылка — {link}</p>
        <p>Если загрузка не началась автоматически — нажмите на ссылку ниже</p>
        <a class="dnld-link" href="/downloads/{title}" download="{title}">Скачать</a>
    </div>
</div>
</body>
</html>
        """
    return html_content
