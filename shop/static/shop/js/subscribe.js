let subscribe_roasting = document.getElementById('roasting');
let grinds = document.getElementsByClassName('grind');
grinds = Array.from(grinds);
let kind = document.getElementById('kind');
let feature = document.getElementById('feature');

let subscribe_form = document.getElementById('subscribe-form');
let subscribe_item_product = document.getElementById('input-product');
let subscribe_item_roasting = document.getElementById('input-roasting');
let subscribe_item_grind = document.getElementById('input-grind');

document.addEventListener('DOMContentLoaded', is_feature);
kind.addEventListener('change', is_feature);

document.addEventListener('DOMContentLoaded', initial_subscribe_grind);
subscribe_roasting.addEventListener('change', choice_subscribe_grind);

function choice_subscribe_grind(){
    let option = this.value;
    get_subscribe_grind(option);
}

function get_subscribe_grind(option){
        for(let i in grinds){
            if(grinds[i].name === option){
                grinds[i].classList.remove('hidden');
            } else {
                grinds[i].classList.add('hidden');
            }
        }
}

function initial_subscribe_grind(){
        let option = subscribe_roasting.value;
        get_subscribe_grind(option);
}

function is_feature(){
    let option = kind.value.split('_')[1];
    if(option){
        feature.classList.remove('hidden');
    } else {
        feature.classList.add('hidden');
    }
}

subscribe_form.addEventListener('submit', function(event){
    event.preventDefault();
    subscribe_item_product.value = kind.value.split('_')[0];
    if(!feature.classList.contains('hidden')){
        subscribe_item_roasting.value = subscribe_roasting.value;
        for(let i in grinds){
            if(!grinds[i].classList.contains('hidden')){
                subscribe_item_grind.value = grinds[i].value;
            }
        }
    }
    subscribe_form.submit();
});