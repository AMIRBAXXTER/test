function lamp () {
    let button = document.getElementById("button").innerHTML
    if(button == "turn on"){
        document.getElementById("button").innerHTML = "turn off"
        let picture = document.getElementById("picture")
        picture.setAttribute("src", "on.jpg")

    } else {
        document.getElementById("button").innerHTML = "turn on"
        let picture = document.getElementById("picture")
        picture.setAttribute("src", "off.jpg")
    }
}