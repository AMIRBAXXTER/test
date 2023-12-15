let states = {
    "Alabama": ["Athens", "Atmore", "Dothan", "Florence", "Opelika"],
    "Alaska": ["Haines", "Kodiak", "Sitka", "Nome"],
    "Arizona": ["Casa Grande", "Douglas","Gila Bend", "Kingman", "Oraibi"],
    "Arkansas": ["Batesville", "Conway"],
    "California": ["Barstow", "Calexico", "Compton", "Corona", "El Monte", "Fresno"],
    "": []
  };

let stateSelect = document.getElementById("state") 
let citySelect = document.getElementById("city")
stateSelect.addEventListener("change", function(){
    let selectedState = stateSelect.value
    let cities = states[selectedState]

    citySelect.innerHTML = '<option value="">select city...</option>'
cities.forEach(function(city){
    let option = document.createElement("option")
    option.value = city
    option.text = city
    citySelect.add(option)
})

})



