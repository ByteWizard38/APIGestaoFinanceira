from pydantic import BaseModel, Field

class AccountBase(BaseModel):
    name: str
    balance: float

class AccountCreate(AccountBase):
    pass

class Account(AccountBase):
    id: str

    class Config:
        orm_mode = True

class CreditBase(BaseModel):
    amount: float
    description: str

class CreditCreate(CreditBase):
    pass

class Credit(CreditBase):
    id: str
    account_id: str

    class Config:
        orm_mode = True

class DebitBase(BaseModel):
    amount: float
    description: str

class DebitCreate(DebitBase):
    pass

class Debit(DebitBase):
    id: str
    account_id: str

    class Config:
        orm_mode = True
