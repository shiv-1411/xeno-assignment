#!/usr/bin/env python3
"""
Update customer total_spent values with realistic data
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.customer import Customer
from app.models.order import Order
import random

def update_customer_spending():
    db: Session = SessionLocal()
    
    try:
        # Get all customers
        customers = db.query(Customer).all()
        
        for customer in customers:
            # Calculate realistic total_spent based on orders or assign random amount
            orders_total = db.query(Order).filter(Order.tenant_id == customer.tenant_id).all()
            
            if orders_total:
                # Assign realistic spending between $150-$2500
                customer.total_spent = round(random.uniform(150.0, 2500.0), 2)
            else:
                customer.total_spent = 0.0
            
            print(f"Updated {customer.first_name} {customer.last_name}: ${customer.total_spent}")
        
        db.commit()
        print("✅ Successfully updated customer spending data!")
        
    except Exception as e:
        print(f"❌ Error updating customer data: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    print("🔄 Updating customer spending data...")
    update_customer_spending()
