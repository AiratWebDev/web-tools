window.onload = () => {
    const label = document.querySelector('.file-label'),
        fileInput = document.querySelector('.file-input')

    fileInput.addEventListener('change', (event) => {
        let fileName = ''
        fileName = event.target.files[0].name
        label.textContent = fileName
    })
}
