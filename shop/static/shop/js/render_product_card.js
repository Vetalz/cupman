let roasting = document.getElementsByClassName('roasting')
let packing = document.getElementsByClassName('packing')

let array_roasting = Array.from(roasting)
let array_packing = Array.from(packing)

document.addEventListener('DOMContentLoaded', initial_grind);
document.addEventListener('DOMContentLoaded', initial_price);

for(let i in array_roasting) {
    array_roasting[i].addEventListener('change', choice_grind);
}

for(let i in array_packing) {
    array_packing[i].addEventListener('change', choice_price);
}


function get_grind(option, id){
    let grind_id = id + '_grind'
        let grind = document.getElementsByClassName(grind_id)
        grind = Array.from(grind)
        for(let n in grind){
            if(grind[n].name === option){
                grind[n].classList.remove('hidden')
            } else {
                grind[n].classList.add('hidden')
            }
        }
}

function choice_grind(){
    let option = this.value
    let id = this.id.slice('_')[0]
    get_grind(option, id)
}

function initial_grind(){
    for(let i in array_roasting) {
        let option = array_roasting[i].value
        let id = array_roasting[i].id.slice('_')[0]
        get_grind(option, id)
    }
}


function get_price(option, id){
    let price_id = id + '_price'
        let price = document.getElementsByClassName(price_id)
        price = Array.from(price)
        for(let n in price){
            if(price[n].id === option){
                price[n].classList.remove('hidden')
            } else {
                price[n].classList.add('hidden')
            }
        }
}

function choice_price(){
    let option = this.value
    let id = this.id.slice('_')[0]
    get_price(option, id)
}

function initial_price(){
    for(let i in array_packing) {
        let option = array_packing[i].value
        let id = array_packing[i].id.slice('_')[0]
        get_price(option, id)
    }
}



