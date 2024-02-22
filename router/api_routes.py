from fastapi import APIRouter
from starlette.responses import JSONResponse

from modules.add_expense import addExpense
from modules.create_room import createRoom
from modules.login import doLogin
from modules.register_user import register_user
from modules.room_Transaction_Views import show_transactions_under_room
from modules.search_room import getAllRooms
from modules.settle_transactions import settle_room_transactions
from schemas.schemas import RegisterUser, createRoom_ipParams, add_expense
from utils.constants import database_name, room_collection_name
from utils.dbOperations import find_single_data

router = APIRouter(prefix='', tags=[], responses={404: {"description": "Not found"}})


@router.get("/")
async def health_check():
    return JSONResponse({'message': "health Check"})


@router.post("/register")
async def register(registerUser: RegisterUser):
    user_id = registerUser.user_id
    full_name = registerUser.full_name
    password = registerUser.password
    email = registerUser.email
    response_user_id = register_user(user_id, full_name, password, email)
    return JSONResponse({'user_id': response_user_id})


@router.post("/login")
async def register(registerUser: RegisterUser):
    user_id = registerUser.user_id
    password = registerUser.password
    return doLogin(user_id,password)

@router.post("/createRoom")
async def create_room(create_room_object: createRoom_ipParams):
    user_id = create_room_object.user_id
    room_name = create_room_object.room_name
    currency = create_room_object.currency
    members = create_room_object.members
    # call create room function
    return createRoom(user_id, room_name, currency, members)


@router.post("/searchRooms")
async def create_room(create_room_object: createRoom_ipParams):
    user_id = create_room_object.user_id
    return getAllRooms(user_id)


@router.post("/addTransactions")
async def add_Expenses(addTransaction: add_expense):
    room_id = addTransaction.room_id
    paid_user_id = addTransaction.paid_user_id
    amount = addTransaction.amount
    expense_name = addTransaction.expense_name
    fairsplit_members = addTransaction.fairsplit_members
    print(room_id, paid_user_id, amount, expense_name, fairsplit_members)
    addExpense(room_id, paid_user_id, amount, expense_name, fairsplit_members)
    return {"message":"Expense added successfully"}


@router.post("/show_transactions_under_room")
async def show_room_transactions(addTransaction: add_expense):
    room_id = addTransaction.room_id
    found_room_details=show_transactions_under_room(room_id)
    return {"room_transaction_details": found_room_details}

@router.post("/settleUp")
async def settle_room_transaction(addTransaction: add_expense):
    room_id = addTransaction.room_id
    settle_statements=settle_room_transactions(room_id)
    return {"settle_statements":settle_statements}
