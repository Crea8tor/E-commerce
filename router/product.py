from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends,status

from schema.product import Product, ProductCreate, products


product_router = APIRouter()

# create product
# list all products

@product_router.post('/', status_code=201)
def create_product(payload: ProductCreate):
    # get the product id
    product_id = len(products) + 1
    new_product = Product(
        id=product_id,
        name=payload.name,
        price=payload.price,
        quantity_available=payload.quantity_available
    )
    products[product_id] = new_product
    return {'message': 'Product created successfully', 'data': new_product}

@product_router.get('/', status_code=200)
def list_products():
    return {'message': 'success', 'data': products}


# Add an endpoint to edit product information
@product_router.put("/",status_code=200)
async def product_edit(payload : Product):
    #get the product
    items = []
    for _, item in products.items():
        items.append(item)
    ids = [item.id for item in items]
    print(ids)
    for id in ids:
        if payload.id not in ids:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="product not found")
        product_edit= Product(
            id=payload.id,
            name=payload.name,
            price=payload.price,
            quantity_available=payload.quantity_available
        )
        products[payload.id] = product_edit

    return {
        "message": "product edited successfully",
        "data": product_edit
    }
    









   
     
               
              
   
          
            



       



       
           
               

    

