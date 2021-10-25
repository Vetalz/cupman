let methodNewPost = document.getElementById('method_delivery_1');
let methodSelfPickup = document.getElementById('method_delivery_2');

let region = document.getElementById('input-region');
let city = document.getElementById('input-city');
let new_post_office = document.getElementById('input-new_post');
let address = document.getElementById('input-address');

methodNewPost.addEventListener("click", onclick1);
methodSelfPickup.addEventListener("click", onclick1);

function onclick1(e){
    region.classList.toggle('hidden');
    city.classList.toggle('hidden');
    new_post_office.classList.toggle('hidden');
    address.classList.toggle('hidden');
}
