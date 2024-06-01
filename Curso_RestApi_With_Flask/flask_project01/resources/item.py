import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import items
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", "items", description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema) # aquí va el status code y el itemSchema a la derecha recibe el valor devuelto en el return.
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found.")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message="Item not found.")

    @blp.arguments(ItemUpdateSchema) # al usar el blp.arguments, el parametro va en frente del resto de los otros argumentos.
    @blp.response(200, ItemSchema) # el orden importa, el response debe ir dentro del arguments, más abajo.
    def put(self, item_data, item_id):
        try:
            item = items[item_id]

            # https://blog.teclado.com/python-dictionary-merge-update-operators/
            item |= item_data

            return item
        except KeyError:
            abort(404, message="Item not found.")


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True)) # el many=True se usa cuando se devuelve multiples itemSchemas.
    def get(self):
        return items.values() # ahora simplemente devolvemos el items.values()

    @blp.arguments(ItemSchema) # aquí usamos el schema para validar 
    @blp.response(201, ItemSchema)
    def post(self, item_data): # ahora no hay que hacer el request ya que el item schema lo recibe y valida (luego devolviendo como argumento ese diccionario validado.).
        for item in items.values():
            if (
                item_data["name"] == item["name"]
                and item_data["store_id"] == item["store_id"]
            ):
                abort(400, message=f"Item already exists.")

        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item

        return item
