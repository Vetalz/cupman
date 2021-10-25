function qty_up(id) {
    let input_qty = document.getElementById(id);
    let prev_value = parseInt(input_qty.value);
    let max_value = parseInt(input_qty.max)

    if (max_value > prev_value) {
        input_qty.setAttribute('value', ++prev_value);
    }
}

function qty_down(id) {
    let input_qty = document.getElementById(id);
    let prev_value = parseInt(input_qty.value);
    let min_value = parseInt(input_qty.min)

    if (min_value < prev_value) {
        input_qty.setAttribute('value', --prev_value);
    }
}

function qty_up_cart(input_id) {
    let operation = 'add';
    let input_qty = document.getElementById(input_id);
    let prev_value = parseInt(input_qty.value);
    let max_value = parseInt(input_qty.max);
    let new_value;
    let id = input_id.slice('_')[0];

    if (max_value > prev_value) {
        new_value = ++prev_value
        input_qty.setAttribute('value', new_value);
        change_total_product_price(id, new_value, operation);
    }

    update_product(id, new_value);

}

function qty_down_cart(input_id) {
    let operation = 'take';
    let input_qty = document.getElementById(input_id);
    let prev_value = parseInt(input_qty.value);
    let min_value = parseInt(input_qty.min);
    let new_value;
    let id = input_id.slice('_')[0];

    if (min_value < prev_value) {
        new_value = --prev_value
        input_qty.setAttribute('value', new_value);
        change_total_product_price(id, new_value, operation);
    }
    else{
            new_value = 1
        }

    update_product(id, new_value);
}

function update_product(product_id, qty){
    let all_products = JSON.parse(localStorage.getItem('products'));
    let new_all_products = [];
    for (let item in all_products) {
        if (parseInt(all_products[item].id) === parseInt(product_id)){
            let product = {
                id_product: all_products[item].id_product,
                packing: all_products[item].packing,
                roasting: all_products[item].roasting,
                grind: all_products[item].grind,
                qty: qty,
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
        else{
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
}


function change_total_product_price(product_id, qty, operation){
    let span_price = document.getElementById(`${product_id}_price`)
    let all_products = JSON.parse(localStorage.getItem('products'));
    let price;
    let total_price;
    for (let i in all_products){
        if(all_products[i].id === Number(product_id)) {
            price = Number(all_products[i].price)
        }
    }
    total_price = price * qty;
    span_price.innerText = total_price;
    if(operation === 'add'){
        update_total_price(price);
    }
    else {
        update_total_price(-price)
    }

}
