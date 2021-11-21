function add_cart(id_product, id_category) {
    let id = id_product.slice('_')[0]
    let id_name = id + '_name';
    let id_url = id + '_url';
    let id_image = id + '_image';
    let id_packing = id + '_packing';
    let id_roasting = id + '_roasting';
    let id_grind = id + '_grind';
    let id_qty = id + '_qty';
    let id_price = id + '_price';
    let n = 0


    let name = document.getElementById(id_name).textContent;
    let url = document.getElementById(id_url).href;
    let image = document.getElementById(id_image).src;
    let packing = document.getElementById(id_packing).value;
    let roasting = null;
    if (document.getElementById(id_roasting)) {
         roasting = document.getElementById(id_roasting).value;
    }
    let qty = document.getElementById(id_qty).value;

    let grind_item = null;
    if (document.getElementsByClassName(id_grind)) {
        let grind = document.getElementsByClassName(id_grind);
        grind = Array.from(grind)

        for (let item in grind) {
            if (!(grind[item].classList.contains('hidden'))) {
                grind_item = grind[item].value
            }
        }
    }

    let price = document.getElementsByClassName(id_price);
    let price_item
    price = Array.from(price)

    for(let item in price){
        if(!(price[item].classList.contains('hidden'))){
            price_item = price[item].textContent
        }
    }

    let all_products = [];
    if (localStorage.getItem('products')) {
        all_products = JSON.parse(localStorage.getItem('products'));
        n = all_products.length + n;
    }

    let product = {
        id_product: id,
        packing: packing,
        roasting: roasting,
        grind: grind_item,
        qty: qty,
        category: id_category,
        name: name,
        url: url,
        image: image,
        price: price_item,
        available: 1,
        id: n
    };

    if(all_products.length !== 0) {
        let flag = true
        for (let i in all_products) {
            if (isEqual(all_products[i], product)) {
                all_products[i].qty = Number(all_products[i].qty) + Number(product.qty)
                flag = false
                break
            }
        }
        if(flag){
            all_products.push(product);
        }
    }
    else{
        all_products.push(product);
    }

    localStorage.setItem('products', JSON.stringify(all_products));

    let cart_qty = String(all_products.length)
    let span_cart = document.getElementById('cart')
    span_cart.innerHTML = cart_qty
    span_cart.classList.remove('hidden')

    let cart_msg = document.getElementsByClassName('cart-msg')[0]
    cart_msg.classList.toggle('cart-msg-hidden')
    setTimeout(hidden_msg, 1000, cart_msg);

}

document.addEventListener("DOMContentLoaded", (event)=>{
    let all_products = JSON.parse(localStorage.getItem('products'));
    if (all_products){
        let cart_qty = all_products.length
        let span_cart = document.getElementById('cart')
        span_cart.innerHTML = cart_qty
        span_cart.classList.remove('hidden')
    }

});


function isEqual(object1, object2){
    const props1 = Object.getOwnPropertyNames(object1)
    const props2 = Object.getOwnPropertyNames(object2)

    if (props1.length !== props2.length) {
        return false;
    }

    // 8 - это поля которые не надо сравнивать
    for (let i = 0; i < (props1.length - 8); i += 1) {
        const prop = props1[i];

        if (object1[prop] !== object2[prop]) {
            return false;
        }
    }
    return true;
}


function hidden_msg(el){
    el.classList.toggle('cart-msg-hidden');
}