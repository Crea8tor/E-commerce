from fastapi import HTTPException,status


from schema.customer import customers, CustomerCreate, Customer


class CustomerService:

    @staticmethod
    def is_username_unique(payload : CustomerCreate):
       
        for customer in customers:
            if  customer.username == payload.username:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Customer with username {payload.username} already exists")
        return payload
   
            
        
customer_service = CustomerService()
         



            
           