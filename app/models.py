from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    balance = Column(Float, default=0.0)

    credits = relationship("Credit", back_populates="account")
    debits = relationship("Debit", back_populates="account")

    def recalculate_balance(self):
        self.balance = sum(credit.amount for credit in self.credits) - sum(debit.amount for debit in self.debits)

class Credit(Base):
    __tablename__ = "credits"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    description = Column(String, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))

    account = relationship("Account", back_populates="credits")

class Debit(Base):
    __tablename__ = "debits"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    description = Column(String, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))

    account = relationship("Account", back_populates="debits")
