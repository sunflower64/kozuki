class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
            self.carro = self.session["carro"]
        else:
            self.carro = carro

    def anadir(self, producto):
        if str(producto.id) not in self.cart.keys():
            self.cart[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.name,
                "cant": 1,
                "acumulado": str(producto.precio),
                "imagen": producto.imagen.url,
            }
        else:
            self.carro[id]["cantidad"] += 1
            self.carro[id]["acumulado"] += 1
        self.guardar_carro
        
    
    def guardar_carrito(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.carro:
            del self.carro[producto.id]
            self.save()

    def reducir(self, producto):
        producto_id = str(producto.id)     
        if producto_id in self.carro.keys():
            self.carro[id]["cantidad"] -= 1
            self.carro[id]["acumulado"] -= producto.precio
            if self.carro[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito

    def limpiar(self):
        self.session["carro"] = {}
        self.sessopm.modified = True