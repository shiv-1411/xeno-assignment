from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import user as user_model, customer as customer_model, order as order_model
from app.api.v1.deps import get_current_user
from app.db.session import SessionLocal
from datetime import datetime, timedelta

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_dashboard_data(
    db: Session = Depends(get_db),
    current_user: user_model.User = Depends(get_current_user),
    date_from: str = None,
    date_to: str = None
):
    tenant_id = current_user.tenant_id

    total_customers = db.query(customer_model.Customer).filter(customer_model.Customer.tenant_id == tenant_id).count()
    total_orders = db.query(order_model.Order).filter(order_model.Order.tenant_id == tenant_id).count()
    total_revenue = db.query(order_model.Order).filter(order_model.Order.tenant_id == tenant_id).with_entities(order_model.Order.total_price).all()
    total_revenue = sum(price for price, in total_revenue)

    orders_query = db.query(order_model.Order).filter(order_model.Order.tenant_id == tenant_id)
    if date_from:
        orders_query = orders_query.filter(order_model.Order.created_at >= datetime.fromisoformat(date_from))
    if date_to:
        orders_query = orders_query.filter(order_model.Order.created_at <= datetime.fromisoformat(date_to))
    
    orders_over_time = orders_query.group_by(order_model.Order.created_at).with_entities(order_model.Order.created_at, func.count(order_model.Order.id)).all()
    orders_over_time_labels = [str(o[0].date()) for o in orders_over_time]
    orders_over_time_values = [o[1] for o in orders_over_time]

    top_customers = db.query(customer_model.Customer).filter(customer_model.Customer.tenant_id == tenant_id).order_by(customer_model.Customer.total_spent.desc()).limit(5).all()

    return {
        "total_customers": total_customers,
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "orders_over_time": {
            "labels": orders_over_time_labels,
            "values": orders_over_time_values
        },
        "top_customers": [
            {"first_name": c.first_name, "last_name": c.last_name, "total_spent": c.total_spent}
            for c in top_customers
        ]
    }
