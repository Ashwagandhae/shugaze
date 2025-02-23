from pydantic import BaseModel


class Shoe(BaseModel):
    name: str
    price: float
    size: float
    id: str


class ShoeWithPoints(BaseModel):
    shoe: Shoe
    points: list[list[float]]


class AnalyzeRequest(BaseModel):
    id: str


class AnalyzeResponse(BaseModel):
    original: ShoeWithPoints
    similar: list[ShoeWithPoints]
    today: float


class SearchRequest(BaseModel):
    search: str
