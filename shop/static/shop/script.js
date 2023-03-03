// console.log("mande");


if (localStorage.getItem('cart') === null) {
    var cart = {

    }
}

else {
    cart = JSON.parse(localStorage.getItem('cart'))
}


$(document).on('click', '.atc', function () {
    var item_id = this.id.toString()

    // console.log(item_id);

    if (cart[item_id] != undefined) {
        quantity = cart[item_id][0] + 1
        // cart[item_id] += 1
        cart[item_id][0] = quantity
        cart[item_id][2] = cart[item_id][2] + (document.getElementById('price'+item_id)).innerHTML

    }

    else {
        quantity = 1
        _name = document.getElementById("nm" + item_id).innerHTML;
        _price = (document.getElementById("price" + item_id).innerHTML);
        cart[item_id] = [quantity, _name, _price]
    }

    console.log(cart);


    localStorage.setItem('cart', JSON.stringify(cart))
    document.getElementById("cart").innerHTML = "Mes achats("+Object.keys(cart).length+")"



})


displayCart(cart)

function displayCart(cart) {
    var cartString = ""
    cartString += "<h5>Votre panier</h5>"
    var cartIndex = 1
    for (var x in cart) {
        cartString += cartIndex
        cartString += document.getElementById("nm" + x).innerHTML + "Quantité : " + cart[x][0] + "</br>"
        cartIndex += 1
    }

    console.log(cart);

    cartString += "<a id='checkout' href='checkout/' class='btn btn-warning'>Vérifier</a>"

    document.getElementById("cart").setAttribute('data-content', cartString)

    $('[data-toggle="popover"]').popover();

}