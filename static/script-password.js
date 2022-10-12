window.onload = () => {
    const range = document.querySelector('.range-inpt')
    const number = document.querySelector('.number-inpt')

    const button = document.querySelector('.send-btn')
    const result = document.querySelector('.pass-result-inpt')

    const capital = document.querySelector('.capital-letters-chk')
    const lower = document.querySelector('.lower-letters-chk')
    const numbers = document.querySelector('.numbers-chk')
    const special = document.querySelector('.special-symbols-chk')

    range.addEventListener('input', () => number.value = range.value)
    number.addEventListener('input', () => range.value = number.value)

    function createPass(range, capital, lower, numbers, special) {
        const cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        const low = 'abcdefghijklmnopqrstuvwxyz'
        const num = '1234567890'
        const spec = '%*)?@#$~'
        let passString = ''
        let createdPass = ''

        if (capital) passString = passString.concat(cap)
        if (lower) passString = passString.concat(low)
        if (numbers) passString = passString.concat(num)
        if (special) passString = passString.concat(spec)

        for (let i = 0; i < range; i++) {
            createdPass += passString.charAt(Math.floor(Math.random() * passString.length))
        }

        return createdPass
    }

    button.addEventListener('click', (event) => {
        event.preventDefault()

        const rangeValue = range.value
        const capitalChk = capital.checked
        const lowerChk = lower.checked
        const numbersChk = numbers.checked
        const specialChk = special.checked

        result.value = createPass(rangeValue, capitalChk, lowerChk, numbersChk, specialChk)
    })
}