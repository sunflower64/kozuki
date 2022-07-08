const url='http://127.0.0.1:8000/app/';
const templateTarjeta = document.getElementById('tarjeta-producto').content
const tarjetas = document.getElementById('tarjetas')

const contenedorTarjetaCarrito = document.getElementById('contenedorTarjetaCarrito')
const templateTarjetaCarrito = document.getElementById('templateTarjetaCarrito').content


const realizarCompra = document.getElementById('realizarCompra')

//array carrito
let carrito = {}

const fragment = document.createDocumentFragment()

// se carga documento...
document.addEventListener('DOMContentLoaded', () => {

    traerProductos()

    // local storaje y cargar carrito
    if(localStorage.getItem('carrito')){
        carrito = JSON.parse(localStorage.getItem('carrito'))
        poblarCarrito()
    }
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

        templateTarjeta.querySelector('#img-producto').textContent = producto.foto_producto
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
        foto_producto: objeto.querySelector('#img-producto').textContent,
        cantidad : 1
    }
    if (carrito.hasOwnProperty(producto.id)){
        producto.cantidad = carrito[producto.id].cantidad + 1

    }
    carrito[producto.id] = {...producto}
    poblarCarrito()


}
// POBLAR CARRITO DE COMPRA
const poblarCarrito = () =>{
    //console.log(carrito)
    contenedorTarjetaCarrito.innerHTML=''

    Object.values(carrito).forEach(producto => {
        templateTarjetaCarrito.querySelector('#Nombre').textContent = producto.nombre_producto
        templateTarjetaCarrito.querySelector('#Marca').textContent = producto.marca_producto

        templateTarjetaCarrito.querySelector('#img-carrito').textContent = producto.foto_producto

        templateTarjetaCarrito.querySelector('#Cantidad').textContent = producto.cantidad
        templateTarjetaCarrito.querySelector('#Precio').textContent = '$'+producto.precio_producto
        templateTarjetaCarrito.querySelector('#Total').textContent = '$'+producto.precio_producto * producto.cantidad
        



        const clone = templateTarjetaCarrito.cloneNode(true)
        fragment.appendChild(clone)
    }) 
    contenedorTarjetaCarrito.appendChild(fragment)

    poblarCompra()

    localStorage.setItem('carrito', JSON.stringify(carrito))

}

const poblarCompra = () =>{

    const cantidadTotal = Object.values(carrito).reduce((acumulador, {cantidad})=> acumulador + cantidad , 0)
    const precioTotal = Object.values(carrito).reduce((acumulador, {cantidad , precio_producto})=> acumulador + cantidad *  precio_producto, 0)

    realizarCompra.querySelector('#cantidad-total').textContent = cantidadTotal
    realizarCompra.querySelector('#precio-total').textContent = '$'+precioTotal

    const btnVaciar1 = document.querySelector('.btn-vaciar1')
    btnVaciar1.addEventListener('click' ,() => {
        carrito={}
        poblarCarrito()

    })
    const btnVaciar2 = document.querySelector('.btn-vaciar2')
    btnVaciar2.addEventListener('click' ,() => {
        carrito={}
        poblarCarrito()

    })

}

