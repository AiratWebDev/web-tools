window.onload = () => {
    const button = document.querySelector('.send-btn')
    const loading = document.querySelector('.loader')
    const previous = document.querySelector('.background-wrap')
    const text = document.createElement('div')

    loading.style.visibility = 'hidden'
    text.style.visibility = 'hidden'
    loading.after(text)

    button.addEventListener('click', () => {
        previous.style.display = 'none'
        loading.style.visibility = 'visible'
        text.innerHTML = 'Замеряем скорость'
        text.style.visibility = 'visible'
        text.style.fontSize = '18px'
    })
}



