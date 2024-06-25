from bson import ObjectId
from app.database import db
from app.schemas import AccountCreate, CreditCreate, DebitCreate


async def create_account(account: AccountCreate):
    result = await db.accounts.insert_one(account.dict())
    new_account = await db.accounts.find_one({"_id": result.inserted_id})
    return {"id": str(new_account["_id"]), **new_account}

async def get_accounts(skip: int = 0, limit: int = 10):
    accounts = await db.accounts.find().skip(skip).limit(limit).to_list(length=limit)
    return [{"id": str(account["_id"]), **account} for account in accounts]

async def get_account(account_id: str):
    account = await db.accounts.find_one({"_id": ObjectId(account_id)})
    if account:
        return {"id": str(account["_id"]), **account}
    return None

async def delete_account(account_id: str):
    result = await db.accounts.delete_one({"_id": ObjectId(account_id)})
    return result.deleted_count > 0

async def update_account_balance(account_id: str, amount: float):
    account = await db.accounts.find_one({"_id": ObjectId(account_id)})
    if account:
        new_balance = account['balance'] + amount
        await db.accounts.update_one({"_id": ObjectId(account_id)}, {"$set": {"balance": new_balance}})
        updated_account = await db.accounts.find_one({"_id": ObjectId(account_id)})
        return {"id": str(updated_account["_id"]), **updated_account}
    return None


async def create_credit(credit: CreditCreate, account_id: str):
    credit_dict = credit.dict()
    credit_dict['account_id'] = account_id
    result = await db.credits.insert_one(credit_dict)
    new_credit = await db.credits.find_one({"_id": result.inserted_id})
    await update_account_balance(account_id, credit.amount)
    return {"id": str(new_credit["_id"]), **new_credit}

async def get_credits(skip: int = 0, limit: int = 10):
    credits = await db.credits.find().skip(skip).limit(limit).to_list(length=limit)
    return [{"id": str(credit["_id"]), **credit} for credit in credits]

async def get_credit(credit_id: str):
    credit = await db.credits.find_one({"_id": ObjectId(credit_id)})
    if credit:
        return {"id": str(credit["_id"]), **credit}
    return None

async def delete_credit(credit_id: str):
    credit = await db.credits.find_one({"_id": ObjectId(credit_id)})
    if credit:
        account_id = credit['account_id']
        amount = credit['amount']
        await db.credits.delete_one({"_id": ObjectId(credit_id)})
        await update_account_balance(account_id, -amount)
        return {"id": str(credit["_id"]), **credit}
    return None


async def create_debit(debit: DebitCreate, account_id: str):
    debit_dict = debit.dict()
    debit_dict['account_id'] = account_id
    result = await db.debits.insert_one(debit_dict)
    new_debit = await db.debits.find_one({"_id": result.inserted_id})
    await update_account_balance(account_id, -debit.amount)
    return {"id": str(new_debit["_id"]), **new_debit}

async def get_debits(skip: int = 0, limit: int = 10):
    debits = await db.debits.find().skip(skip).limit(limit).to_list(length=limit)
    return [{"id": str(debit["_id"]), **debit} for debit in debits]

async def get_debit(debit_id: str):
    debit = await db.debits.find_one({"_id": ObjectId(debit_id)})
    if debit:
        return {"id": str(debit["_id"]), **debit}
    return None

async def delete_debit(debit_id: str):
    debit = await db.debits.find_one({"_id": ObjectId(debit_id)})
    if debit:
        account_id = debit['account_id']
        amount = debit['amount']
        await db.debits.delete_one({"_id": ObjectId(debit_id)})
        await update_account_balance(account_id, amount)
        return {"id": str(debit["_id"]), **debit}
    return None
