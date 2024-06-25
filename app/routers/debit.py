from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app import crud, schemas

router = APIRouter(
    prefix="/debits",
    tags=["debits"],
    responses={404: {"description": "Not found"}},
)

templates = Jinja2Templates(directory="app/templates")

@router.post("/", response_model=schemas.Debit)
async def create_debit(debit: schemas.DebitCreate, account_id: str):
    return await crud.create_debit(debit, account_id)

@router.get("/", response_class=HTMLResponse)
async def read_debits(request: Request, skip: int = 0, limit: int = 10):
    debits = await crud.get_debits(skip=skip, limit=limit)
    return templates.TemplateResponse("list_debits.html", {"request": request, "debits": debits})

@router.get("/{debit_id}", response_model=schemas.Debit)
async def read_debit(debit_id: str):
    db_debit = await crud.get_debit(debit_id=debit_id)
    if db_debit is None:
        raise HTTPException(status_code=404, detail="Debit not found")
    return db_debit

@router.delete("/{debit_id}")
async def delete_debit(debit_id: str):
    result = await crud.delete_debit(debit_id=debit_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Debit not found")
    return {"detail": "Debit deleted"}
