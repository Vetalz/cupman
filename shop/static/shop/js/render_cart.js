let all_products = JSON.parse(localStorage.getItem('products'));
let cart = document.getElementById('all_products');
let cart_available = document.getElementById('cart_available');

for (let product in all_products) {
    cart_available.classList.add('hidden');
    render(all_products[product]);
}

function render(product) {
    let product_item = '';
    let total_price_product = product.qty * product.price
    product_item = `<div class="row cart-item" id="${product.id}">
                        <div class="col-md-2 d-flex align-items-center justify-content-center mt-1 mb-1">
                            <div class="img-cart">
                                <img src="${product.image}" alt="${product.name}">
                            </div>
                       </div>
                       <div class="col-md-3 d-flex align-items-center justify-content-center">
                           <h3><a href="${product.url}">${product.name}</a></h3>
                       </div>
                       <div class="col-md-2 d-flex flex-column justify-content-end">
                           <p class="text-center">Вес: ${product.packing} г</p>
                           <p class="text-center">Обжарка: ${product.roasting}</p>
                           <p class="text-center">Помол: ${product.grind}</p>
                       </div>
                       <div class="col-md-2 d-flex align-items-center justify-content-center mt-1 mb-1">
                           <div class="amount-item d-flex">
                               <button class="btn btn-primary" value="-" onClick="qty_down_cart('${product.id}_qty')">-</button>
                               <input type="number" class="form-control ms-3" min="1" max="99" value="${+product.qty}" id="${product.id}_qty">
                               <button class="btn btn-primary" value="+" onClick="qty_up_cart('${product.id}_qty')">+</button>
                           </div>
                       </div>
                       <div class="col-md-2 d-flex align-items-center justify-content-center mt-1 mb-1">
                           <p class="price"><span id="${product.id}_price">${total_price_product}</span><span> грн</span></p>
                       </div>
                       <div class="col-md-1 d-flex align-items-center justify-content-center mt-1 mb-1">
                            <button type="button" class="btn-close" aria-label="Delete" onClick="del_product(${product.id})"></button>
                       </div>
                   </div>`
    cart.innerHTML += product_item;
    update_total_price(total_price_product)
}

function del_product(product_id) {
    let span_product_price = document.getElementById(`${product_id}_price`);
    let product_price = Number(span_product_price.innerText);
    update_total_price(-product_price);

    document.getElementById(product_id).remove();
    all_products = JSON.parse(localStorage.getItem('products'));
    let new_all_products = [];
    for (let item in all_products) {
        if (parseInt(all_products[item].id) !== product_id){
            let product = {
                id_product: all_products[item].id_product,
                packing: all_products[item].packing,
                roasting: all_products[item].roasting,
                grind: all_products[item].grind,
                qty: all_products[item].qty,
                category: all_products[item].category,
                name: all_products[item].name,
                url: all_products[item].url,
                image: all_products[item].image,
                price: all_products[item].price,
                available: all_products[item].available,
                id: all_products[item].id
            };
            new_all_products.push(product);
        }
    }

    check_items(new_all_products);
    localStorage.setItem('products', JSON.stringify(new_all_products));

    all_products = JSON.parse(localStorage.getItem('products'));
    let cart_qty = String(all_products.length)
    let span_cart = document.getElementById('cart')
    span_cart.innerHTML = cart_qty
}

function check_items(products) {
    if(products.length === 0) {
        cart_available.classList.remove('hidden');
    }
}

function update_total_price(price){
    let span_total = document.getElementById('total');
    let total = Number(span_total.innerText);
    span_total.innerText = total + price;
}
