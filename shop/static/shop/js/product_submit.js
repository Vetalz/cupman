let cart_form = document.getElementById('cart-form');
let cart_item_product = document.getElementById('input-product');

document.addEventListener('DOMContentLoaded', check_cart)

cart_form.addEventListener('submit', function(event){
    event.preventDefault();
    let products = JSON.parse(localStorage.getItem('products'));
    console.log(products)
    cart_item_product.value = JSON.stringify(products);
    localStorage.clear();
    cart_form.submit();
    check_cart();
});

function check_cart(){
    let empty_cart = document.getElementsByClassName('empty');
    empty_cart = Array.from(empty_cart);
    let products = JSON.parse(localStorage.getItem('products'));
    if(products === null || products.length < 1) {
        for (let i in empty_cart) {
            empty_cart[i].classList.toggle('hidden')
        }
    }
}