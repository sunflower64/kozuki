const url='http://127.0.0.1:8000/app/';
const templateTarjeta = document.getElementById('tarjeta-producto').content
const tarjetas = document.getElementById('tarjetas')

let carrito = {}


const fragment = document.createDocumentFragment()

document.addEventListener('DOMContentLoaded', () => {

    traerProductos()
})

tarjetas.addEventListener('click', prod => {
    alCarrito(prod)
        
})
const traerProductos = async() =>{
    try {
        const restUrl = await fetch(url)
        const data = await restUrl.json()
        
        instanciarProductos(data)
    }catch (error){
        console.log(error)
    }
}

const instanciarProductos = data =>{
    data.forEach(producto => {
        console.log(producto)

       //para imagen templateTarjeta.querySelector('#img-producto').setAtribute("imgDefault" , value)

        templateTarjeta.querySelector('#nombre-producto').textContent = producto.nombre_producto
        templateTarjeta.querySelector('#marca-producto').textContent = producto.marca_producto
        templateTarjeta.querySelector('#precio-producto').textContent = producto.precio_producto
        templateTarjeta.querySelector('#btn-tarjeta').dataset.id = producto.id

        const clone = templateTarjeta.cloneNode(true)
        fragment.appendChild(clone)

    });
    tarjetas.appendChild(fragment)
}

//al cliquear boton...
const alCarrito = prod =>{
    //console.log(prod.target)
    //console.log(prod.target.classList.contains('btn-tarjeta') )
    if (prod.target.classList.contains('btn-tarjeta')){

        setCarrito(prod.target.parentElement)
    }
    prod.stopPropagation()
}

// elementos de la tarjeta se iran a setCarrito
const setCarrito = objeto => {
    
    const producto = {
        id: objeto.querySelector('.btn-tarjeta').dataset.id,
        nombre_producto: objeto.querySelector('#nombre-producto').textContent,
        marca_producto:  objeto.querySelector('#marca-producto').textContent,
        precio_producto: objeto.querySelector('#precio-producto').textContent,
        cantidad : 1
    }
    if (carrito.hasOwnProperty(producto.id)){
        producto.cantidad = carrito[producto.id].cantidad + 1

    }
    carrito[producto.id] = {...producto}

    console.log(carrito)
}