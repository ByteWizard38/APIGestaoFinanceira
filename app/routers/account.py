from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app import crud, schemas

router = APIRouter(
    prefix="/accounts",
    tags=["accounts"],
    responses={404: {"description": "Not found"}},
)

templates = Jinja2Templates(directory="app/templates")

@router.post("/", response_model=schemas.Account)
async def create_account(account: schemas.AccountCreate):
    return await crud.create_account(account)

@router.get("/", response_class=HTMLResponse)
async def read_accounts(request: Request, skip: int = 0, limit: int = 10):
    accounts = await crud.get_accounts(skip=skip, limit=limit)
    return templates.TemplateResponse("list_accounts.html", {"request": request, "accounts": accounts})

@router.get("/{account_id}", response_model=schemas.Account)
async def read_account(account_id: str):
    db_account = await crud.get_account(account_id=account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

@router.delete("/{account_id}")
async def delete_account(account_id: str):
    db_account = await crud.delete_account(account_id=account_id)
    if not db_account:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"detail": "Account deleted"}
