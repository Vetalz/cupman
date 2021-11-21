let subscribe_roasting = document.getElementById('roasting')
let kind = document.getElementById('kind')
let feature = document.getElementById('feature')

document.addEventListener('DOMContentLoaded', is_feature);
kind.addEventListener('change', is_feature);

document.addEventListener('DOMContentLoaded', initial_subscribe_grind);
subscribe_roasting.addEventListener('change', choice_subscribe_grind);

function choice_subscribe_grind(){
    let option = this.value
    get_subscribe_grind(option)
}

function get_subscribe_grind(option){
    let grinds = document.getElementsByClassName('grind')
        grinds = Array.from(grinds)
        for(let i in grinds){
            if(grinds[i].name === option){
                grinds[i].classList.remove('hidden')
            } else {
                grinds[i].classList.add('hidden')
            }
        }
}

function initial_subscribe_grind(){
        let option = subscribe_roasting.value
        get_subscribe_grind(option)
}

function is_feature(){
    let option = kind.value.split('_')[1]
    if(option){
        feature.classList.remove('hidden')
    } else {
        feature.classList.add('hidden')
    }
}