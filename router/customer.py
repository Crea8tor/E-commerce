from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends, status

from schema.customer import Customer, CustomerCreate, customers
from service.customer import customer_service

customer_router = APIRouter()

# Create customer 
# List customer
# edit customer
 

# create customer
@customer_router.post('/', status_code=status.HTTP_201_CREATED)
def create_customer(payload: Annotated[CustomerCreate, Depends(customer_service.is_username_unique)]):
   
    customer_id = len(customers) + 1
    new_customer = Customer(
        id=customer_id,
        username=payload.username,
        address=payload.address
    )

    customers.append(new_customer)
    return {'message': 'Customer created successfully', 'data': new_customer}


@customer_router.get('/', status_code=200)
def list_customers():
    return {'message': 'success', 'data': customers}



@customer_router.put('/{customer_id}', status_code=200)
def edit_customer(customer_id: int, payload: CustomerCreate):
    curr_customer = None
   
    for customer in customers:
        if customer.id == customer_id:
            curr_customer = customer
            break
    if not curr_customer:
        raise HTTPException(status_code=404, detail="customer not found")
    curr_customer.username = payload.username
    curr_customer.address = payload.address
    return {'message': 'customer edited successfully', 'data': curr_customer}


