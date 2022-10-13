window.onload = () => {
    const form = document.querySelector('.form-to-send')
    const inputShort = document.querySelector('.link-input')
    const button = document.querySelector('.send-btn')
    const elem = document.createElement('div')

    elem.style.color = '#e90d0d'
    elem.style.visibility = 'hidden'
    form.prepend(elem)

    inputShort.oninvalid = (event) => {
        event.target.setCustomValidity('Вставьте ссылку в верном формате')
    }

    const regExpUrl = new RegExp("^((http|https|ftp)\://){1}([a-zA-Z0-9\.\-]+\.(\:[a-zA-Z0-9\.&amp;%\$\-]+)*@)*((25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])|([a-zA-Z0-9\-]+\.)*[a-zA-Z0-9\-]+\.(com|edu|gov|int|mil|net|org|biz|arpa|info|name|pro|aero|coop|museum|[a-zA-Z]{2}))(\:[0-9]+)*(/($|[a-zA-Z0-9\.\,\?\'\\\+&amp;%\$#\=~_\-]+))*$");

    button.addEventListener('click', (event) => {
        const value = inputShort.value

        if (regExpUrl.test(value)) {
            console.log("URL/IP Valid")
        } else {
            event.preventDefault()
            elem.innerHTML = 'Укажите верную ссылку'
            elem.style.visibility = 'visible'
        }
    })
}

