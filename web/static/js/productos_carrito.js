
var urlRestListarProductos = 'http://127.0.0.1:8000/rest/traer_productos';


function loopProducto(){
    $.ajax({
        url:urlRestListarProductos,
        dataType:'JSON',
        success:function(data){
            for(var i=0; i<data.length; i++){
                var fila=$('<div class="max-w-sm bg-white w-80 shadow-md rounded-xl transform transition duration-500 hover:scale-105 hover:shadow-2xl" > '+
                '<a href="#"><img class="shadow-lg border-gray-700 object-cover w-full rounded-xl border-b" src="{% static "img/kong-goodie-bone-dog-toy-best-chew-dog-toy.jpg"%}" width="" height="" alt="product image">'+
                '</a><div class="m-3 "><h1 class="text-2xl font-bold text-gray-800 ">'+data[i].nombre_producto +'</h1><h3 class="text-gray-500 uppercase ">'
                +data[i].marca_producto +'</h3><div class="flex  items-center"><span class="text-2xl text-gray-900 ">$'+data[i].precio_producto +
                '</span></div></div><button data-id="'+data[i].id +'" href="#" class="w-full shadow-lg rounded-b-lg text-black bg-pink-500 hover:bg-pink-600  hover:text-white focus:ring-4'+
                'focus:outline-none focus:ring-purlpe-300 font-medium text-sm px-5 py-2.5 text-center  ">Agregar al carrito</button>  </div>');       
                $('#tarjetas').append(fila);
            }
        }
    });
};

document.addEventListener('DOMContentLoaded',() =>{
    loopProducto();

})



