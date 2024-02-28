from fastapi import APIRouter, Header
from starlette.responses import JSONResponse

# Importing functions and schemas from modules
from modules.add_expense import addExpense
from modules.check_user_spendings import check_User_spendings
from modules.create_room import createRoom
from modules.login import do_login
from modules.register_user import register_user
from modules.room_Transaction_Views import show_transactions_under_room
from modules.search_room import getAllRooms
from modules.settle_transactions import settle_room_transactions
from schemas.schemas import RegisterUser, createRoom_ipParams, add_expense, LoginUser
from utils.dbOperations import mongoDB_connection

# Creating an APIRouter instance
router = APIRouter(prefix='', tags=[], responses={404: {"description": "Not found"}})


# Endpoint for health check
@router.get("/api_healthCheck")
async def health_check():
    if mongoDB_connection():
        return JSONResponse({'message': "health Check complete, DB connection up"})
    else:
        return {"message": "mongoDB Connection is down"}


# Endpoint for user registration
@router.post("/register")
async def register(registerUser: RegisterUser):
    user_name = registerUser.user_name
    first_name = registerUser.first_name
    last_name = registerUser.last_name
    password = registerUser.password
    email = registerUser.email
    return register_user(user_name, first_name, last_name, password, email)


# Endpoint for user login
@router.post("/login")
async def login(loginuser: LoginUser):
    user_id = loginuser.user_id
    password = loginuser.password
    return do_login(user_id, password)


# Endpoint for creating a room
@router.post("/createRoom")
async def create_room(create_room_object: createRoom_ipParams, Authorization: str = Header(None)):
    # access_token=create_room_object.access_token
    room_name = create_room_object.room_name
    currency = create_room_object.currency
    members = create_room_object.members
    # Calling create room function
    return createRoom(Authorization, room_name, currency, members)


# Endpoint for searching rooms
@router.get("/getRoomsForUser")
async def search_rooms(Authorization: str = Header(None)):
    return getAllRooms(Authorization)


@router.get("/getUserTransactions")
async def check_User_spending(Authorization: str = Header(None)):
    return check_User_spendings(Authorization)


# Endpoint for adding transactions
@router.post("/addTransactions")
async def add_transactions(addTransaction: add_expense, Authorization: str = Header(None)):
    room_id = addTransaction.room_id
    amount = addTransaction.amount
    expense_name = addTransaction.expense_name
    fairsplit_members = addTransaction.fairsplit_members
    return addExpense(room_id, Authorization, amount, expense_name, fairsplit_members)


# Endpoint for showing transactions under a room
@router.post("/showTransactionsUnderRoom")
async def show_transactions_under_room_endpoint(addTransaction: add_expense, Authorization: str = Header(None)):
    room_id = addTransaction.room_id
    found_room_details = show_transactions_under_room(room_id, Authorization)
    return {"room_transaction_details": found_room_details}


# Endpoint for settling room transactions
@router.post("/settleUp")
async def settle_room_transaction_endpoint(addTransaction: add_expense, Authorization: str = Header(None)):
    room_id = addTransaction.room_id
    settle_statements = settle_room_transactions(room_id, Authorization)
    return {"settle_statements": settle_statements}
