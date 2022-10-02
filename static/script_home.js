window.onload = () => {
    const form = document.querySelector('.form-to-send')
    const input = document.querySelector('.link-input')

    form.addEventListener('submit', (event) => {
        const value = document.querySelector('.link-input').value.trim().toLowerCase()
        if (!value.includes('youtu')) {
            event.preventDefault()
            const elem = document.createElement('div')
            elem.style.color = '#e90d0d'
            elem.innerHTML = 'Укажите верную ссылку на видео с YouTube'
            form.prepend(elem)
        }
    })
}


