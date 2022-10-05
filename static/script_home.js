window.onload = () => {
    const form = document.querySelector('.form-to-send')
    const input = document.querySelector('.link-input')
    const elem = document.createElement('div')

    elem.style.color = '#e90d0d'
    elem.style.visibility = 'hidden'
    form.prepend(elem)

    form.addEventListener('submit', (event) => {
        const value = document.querySelector('.link-input').value.trim().toLowerCase()

        if (!value.includes('youtu')) {
            event.preventDefault()
            elem.innerHTML = 'Укажите верную ссылку на видео с YouTube'
            elem.style.visibility = 'visible'
        }
    })
}


