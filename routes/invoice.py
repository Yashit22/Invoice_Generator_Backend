from fastapi import APIRouter
from database.config import client
from database.rules import Rules
from schemas.schema import AddBill
from utils.utils import convert_to_json
from bson import ObjectId

router = APIRouter()

@router.post('/add')
async def add_bill(bill: AddBill):
    bills = Rules.get_all({}, client, 'INVOICE', 'BILLS')
    bill_number = len(list(bills)) + 1
    data = {
        '_id': ObjectId(),
        'bill_number': bill_number,
        'item_names': bill.item_names,
        'item_quantities': bill.item_quantities,
        'item_prices': bill.item_prices,
        'total': sum([i * j for i, j in zip(bill.item_quantities, bill.item_prices)])
    }
    operation = Rules.add(data, client, 'INVOICE', 'BILLS')
    return {'message': 'Bill added successfully', 'operation_id': str(operation.inserted_id)}

@router.get('/get/{bill_number}')
async def get_bills(bill_number: int):
    query = {'bill_number': bill_number}
    bill = Rules.get(query, client, 'INVOICE', 'BILLS')
    return {'message': 'Bills fetched successfully', 'bill': convert_to_json(bill)}