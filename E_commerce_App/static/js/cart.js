function addCart(productId,productPrice,pageType){
    //Add Cart Button Hide
    //Plus,Qty,Minus Button Visible
    console.log(pageType)
    productId = parseInt(productId)
    productPrice = parseInt(productPrice)
    // console.log(productId)
    if (".mainbtn"+productId) {
        $(".mainbtn"+productId).text(1);
        $(".plusbtn"+productId).css("display", "inline");
        $(".mainusbtn"+productId).css("display", "inline");
        console.log("test ::::::::::",productId)
        data = JSON.stringify({
            'qty': 1,
            'productId': productId,
            'productPrice':productPrice,
            'type':'Add'
        })
        console.log(data)
        const xhr = new XMLHttpRequest();
        xhr.responseType = 'json'
        xhr.open('POST', 'http://127.0.0.1:8000/catogary/cartjs/', true);
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest')
        xhr.send(data);
        console.log(pageType)
        console.log(xhr)
    } 
    console.log("add product:"+productId)
}

function positive(productId,productPrice){
    //Add Cart Button Hide
    //Plus,Qty,Minus Button Visible
    productId = parseInt(productId)
    productPrice = parseInt(productPrice)
    // console.log(productId)
    pr = "mainbtn"+productId
    // console.log(pr)
    btn = document.getElementById(pr).innerText;
    btn = +(btn) + +1;
    document.getElementById(pr).innerText = btn
    console.log("increase quantity:",btn+" on product:",productId)
    
    data = JSON.stringify({
        'qty': btn,
        'productId': productId,
        'productPrice':productPrice,
        'type':'Update'
    })
    const xhr = new XMLHttpRequest();
    xhr.responseType = 'json'
    xhr.open('POST', 'http://127.0.0.1:8000/catogary/cartjs/', true);
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest')
    xhr.send(data);
    // console.log("Positive Click "+productId)
}

function negative(productId,productPrice){
    //Add Cart Button Hide
    //Plus,Qty,Minus Button Visible
    productId = parseInt(productId)
    productPrice = parseInt(productPrice)
    // console.log(productId)
    pr = "mainbtn"+productId
    // console.log(pr)
    btn = document.getElementById(pr).innerText;
    // console.log(btn)
    // mbtn = document.getElementById("mainusbtn")
    btn = btn - 1;
    if (btn < 1) {
        console.log("Negative Count Remove "+btn)
        document.getElementById(pr).innerText = 'ADD TO CART';
        $(".plusbtn"+productId).css("display", "none");
        $(".mainusbtn"+productId).css("display", "none");
        data = JSON.stringify({
            'qty': btn,
            'productId': productId,
            'productPrice': productPrice,
            'type':'Remove'
        })
        const xhr = new XMLHttpRequest();
        xhr.responseType = 'json'
        xhr.open('POST', 'http://127.0.0.1:8000/catogary/cartjs/', true);
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest')
        xhr.send(data);
    } else {
        console.log("Negative Count Update "+btn)
        document.getElementById(pr).innerText = btn
        console.log("decrease quantity:",btn+" on product:",productId)
        
        data = JSON.stringify({
            'qty': btn,
            'productId': productId,
            'productPrice': productPrice,
            'type':'Update'
        })
        const xhr = new XMLHttpRequest();
        xhr.responseType = 'json'
        xhr.open('POST', 'http://127.0.0.1:8000/catogary/cartjs/', true);
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest')
        xhr.send(data);
    }
}

function addCartn(productId,productPrice){
    //Add Cart Button Hide
    //Plus,Qty,Minus Button Visible
    productId = parseInt(productId)
    productPrice = parseInt(productPrice)
    console.log("Add Cart N : "+productId+"_"+productPrice)
    if (".mainbtnn"+productId) {
        $(".mainbtnn"+productId).text(1);
        $(".plusbtnn"+productId).css("display", "inline");
        $(".mainusbtnn"+productId).css("display", "inline");
        
        data = JSON.stringify({
            'qty': 1,
            'productId': productId,
            'productPrice':productPrice,
            'type': 'Add'
        })
        const xhr = new XMLHttpRequest();
        xhr.responseType = 'json'
        xhr.open('POST', 'http://127.0.0.1:8000/catogary/cartjs/', true);
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest')
        xhr.send(data);
    }
    console.log("add product:"+productId)
}


function positiven(productId,productPrice){
    //Add Cart Button Hide
    //Plus,Qty,Minus Button Visible
    productId = parseInt(productId)
    productPrice = parseInt(productPrice)
    console.log(productId)
    pr = "mainbtnn"+productId
    console.log(pr)
    btn = document.getElementById(pr).innerText;
    btn = +(btn) + +1;
    document.getElementById(pr).innerText = btn
    console.log("increase quantity:",btn+" on product:",productId)
    
    data = JSON.stringify({
        'qty': btn,
        'productId': productId,
        'productPrice':productPrice,
        'type': 'Update'
    })
    const xhr = new XMLHttpRequest();
    xhr.responseType = 'json'
    xhr.open('POST', 'http://127.0.0.1:8000/catogary/cartjs/', true);
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest')
    xhr.send(data);
    // console.log("Positive Click "+productId)
}

function negativen(productId,productPrice){
    //Add Cart Button Hide
    //Plus,Qty,Minus Button Visible
    productId = parseInt(productId)
    productPrice = parseInt(productPrice)
    // console.log(productId)
    pr = "mainbtnn"+productId
    // console.log(pr)
    btn = document.getElementById(pr).innerText;
    // console.log(btn)
    // mbtn = document.getElementById("mainusbtn")
    btn = btn - 1;
    if (btn < 1) {
        console.log("Negative Count Remove "+btn)
        document.getElementById(pr).innerText = 'ADD TO CART';
        $(".plusbtnn"+productId).css("display", "none");
        $(".mainusbtnn"+productId).css("display", "none");
        data = JSON.stringify({
            'qty': btn,
            'productId': productId,
            'productPrice': productPrice,
            'type': 'Remove'
        })
        const xhr = new XMLHttpRequest();
        xhr.responseType = 'json'
        xhr.open('POST', 'http://127.0.0.1:8000/catogary/cartjs/', true);
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest')
        xhr.send(data);
    } else {
        console.log("Negative Count Update "+btn)
        document.getElementById(pr).innerText = btn
        console.log("decrease quantity:",btn+" on product:",productId)
        
        data = JSON.stringify({
            'qty': btn,
            'productId': productId,
            'productPrice': productPrice,
            'type': 'Update'
        })
        const xhr = new XMLHttpRequest();
        xhr.responseType = 'json'
        xhr.open('POST', 'http://127.0.0.1:8000/catogary/cartjs/', true);
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest')
        xhr.send(data);
    }
}
console.log("Cart JS Call")