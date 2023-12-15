var hour = +prompt('Enter The Hour: ')
var minute = +prompt('Enter The Minute: ')
var second = +prompt('Enter The Second: ')

var timer = setInterval(function () {

    if (second === -1) {
        minute--
        second = 59
    }
    if (minute === -1) {
        hour--
        minute = 59
    }

    if (hour === 0 && minute === 0 && second === 0) {
        clearInterval(timer)
    }

    console.log('Timer: ' + hour + ' : ' + minute + ' : ' + second)
    second--
}, 1000)