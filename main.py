from enum import Enum

from fastapi import FastAPI, \
    Query, \
    Path, \
    Body
from pydantic import BaseModel, \
    Field

app = FastAPI()

#
# @app.get('/')
# async def root():
#     return {"message": "hello world"}
#
#
# @app.post('/')
# async def post():
#     return {"message": "hello from the post route"}
#
#
# @app.put('/')
# async def put():
#     return {"message": "hello from the put route"}
#
#
# @app.get("/users")
# async def list_users():
#     return {"message": "list users route"}
#
#
# @app.get("/users/me")
# async def get_current_user():
#     return {"message": "this is the current user"}
#
#
# @app.get("/users/{user_id}")
# async def get_user(user_id: str):
#     return {"user id": user_id}
#
#
# class FoodEnum(str, Enum):
#     fruits = "fruits"
#     vegetables = "vegetables"
#     dairy = "dairy"
#
#
# @app.get("/foods/{food_name}")
# async def get_food(food_name: FoodEnum):
#     if food_name == FoodEnum.vegetables:
#         return {
#             "food_name": food_name,
#             "message": "you are healthy"
#         }
#
#     if food_name.value == "fruits":
#         return {
#             "food_name": food_name,
#             "message": "you are still healty, but like sweet things"
#         }
#     return {"food_name": food_name, "message": "i like choco milk"}
#
#
# fake_items_db = [{"food_name": "Foo"}, {"food_name": "Bar"}, {"food_name": "Baz"}]
#
#
# # @app.get("/items")
# # async def list_items(skip: int = 0, limit: int = 10):
# #     return fake_items_db[skip: skip + limit]
#
#
# @app.get("/items/{item_id}")
# async def get_item(item_id: str, sample_query_param: str, q: str | None = None, short: bool = False):
#     item = {"items_id": item_id, "sample_query_param": sample_query_param}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu."})
#     return item
#
#
# @app.get("/users/{user_id}/items/{item_id}")
# async def get_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id, "onwer_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eu."})
#     return item
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#
# @app.post("/items")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict
#
#
# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result
#
#
# @app.get("/items")
# async def read_items(
#         q: str | None = Query(None, min_length=3, max_length=10, title="Sample query string",
#                               description="This is a sample query string",
#                               alias="item-query")):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results
#
#
# @app.get('/items_hidden')
# async def hidden_query_route(hidden_query: str | None = Query(None, include_in_schema=False)):
#     if hidden_query:
#         return {"hidden_query": hidden_query}
#     return {"hidden_query": "Not found"}
#
#
# @app.get("/items_validation/{item_id}")
# async def read_items_validation(
#         *,
#         item_id: int = Path(..., title="The ID of the item to get", gt=10, le=100),
#         q: str = 'hello',
#         size: float = Query(..., gt=0, lt=7.75)
# ):
#     results = {"item_id": item_id, "size": size}
#     if q:
#         results.update({"q": q})
#     return results


# Part 7 Body - Multiple Parameters
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#
# class User(BaseModel):
#     username: str
#     full_name: str | None = None
#
#
# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(..., title="The ID of the item to get", ge=0, le=150),
#     q: str | None = None,
#     item: Item = Body(..., embed=True),
#     # user: User,
#     # importance: int = Body(...)
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     # if user:
#     #     results.update({"user": user})
#     # if importance:
#     #     results.update({"importance": importance})
#
#     return results


# Part 8 Body - Fields
# class Item(BaseModel):
#     name: str
#     description: str | None = Field(
#         None, titles="The desc of the item", max_length=300
#     )
#     price: float = Field(..., gt=0, description="The price must be greater than zero")
#     tax: float | None = None
#
#
# @app.put("/items/{item_id")
# async def update_item(item_id: int, item: Item = Body(..., embed=True)):
#     result = {"item_id": item, "item": item}
#     return result


# Part 8 Body - Fields
