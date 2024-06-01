from marshmallow import Schema, fields

# Schema básico para representar un artículo
class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)  # El campo 'id' solo se enviará al cliente (no se recibirá del cliente)
    name = fields.Str(required=True) # El campo 'name' es obligatorio recibirlo del cliente
    price = fields.Float(required=True) # El campo 'price' también es obligatorio recibirlo del cliente

# Schema básico para representar una tienda
class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)  # El campo 'id' solo se enviará al cliente (no se recibirá del cliente)
    name = fields.Str(dump_only=True) # El campo 'name' solo se enviará al cliente (no se recibirá del cliente)

# Schema para actualizar un artículo
class ItemUpdateSchema(Schema):
    name = fields.Str()  # Campo opcional para actualizar el nombre del artículo
    price = fields.Float() # Campo opcional para actualizar el precio del artículo

# Schema para representar un artículo con información adicional
class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)  # Campo 'store_id' es obligatorio recibirlo del cliente, pero no se envía al cliente
    store = fields.Nested(PlainStoreSchema(), dump_only=True) # Campo 'store' incluye la tienda anidada y solo se enviará al cliente

# Schema para representar una tienda con una lista de artículos
class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True) # Campo 'items' es una lista de artículos y solo se enviará al cliente
