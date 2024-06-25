from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app import crud, schemas

router = APIRouter(
    prefix="/credits",
    tags=["credits"],
    responses={404: {"description": "Not found"}},
)

templates = Jinja2Templates(directory="app/templates")

@router.post("/", response_model=schemas.Credit)
async def create_credit(credit: schemas.CreditCreate, account_id: str):
    return await crud.create_credit(credit, account_id)

@router.get("/", response_class=HTMLResponse)
async def read_credits(request: Request, skip: int = 0, limit: int = 10):
    credits = await crud.get_credits(skip=skip, limit=limit)
    return templates.TemplateResponse("list_credits.html", {"request": request, "credits": credits})

@router.get("/{credit_id}", response_model=schemas.Credit)
async def read_credit(credit_id: str):
    db_credit = await crud.get_credit(credit_id=credit_id)
    if db_credit is None:
        raise HTTPException(status_code=404, detail="Credit not found")
    return db_credit

@router.delete("/{credit_id}")
async def delete_credit(credit_id: str):
    result = await crud.delete_credit(credit_id=credit_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Credit not found")
    return {"detail": "Credit deleted"}
