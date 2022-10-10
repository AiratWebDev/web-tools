window.onload = () => {
    const textarea = document.querySelector('.textarea-user-text')
    const allSymbols = document.querySelector('.all-symbols')
    const withoutSpace = document.querySelector('.without-space')
    const words = document.querySelector('.words')

    textarea.addEventListener('input', (event) => {
        let value = event.target.value

        allSymbols.innerHTML = value.length
        withoutSpace.innerHTML = value.split(' ').join('').length
        words.innerHTML = value.trim().replace(/ +/g," ").split(' ').length
    })
}