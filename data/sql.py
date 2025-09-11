from sqlmodel import Field, SQLModel, select, Session, delete
from sqlalchemy import create_engine, Enum as SAEnum, MetaData
from typing import Optional, Callable, Any
import pandas as pd
import enum 
from dataclasses import dataclass



'''

Transform csv file to desired table

Products
- ProductID
- Name
- Description

(CRUD)

Autherization

Creds -> 

Customer Access
- Read -> Product Info (Basic Info + Impression)
    - Interface
        - Filters




'''

from enum import Flag, auto





class ACCESS(Flag):
   CREATE = auto()
   READ = auto()
   UPDATE = auto()
   DELETE = auto()


@dataclass
class RIGHT:
   RESOURCE_ID: str = ""
   allowed: ACCESS = ACCESS.READ


class Operation:
   def __init__(self, *, resource_id : str, operation_id : str, access_required : ACCESS, worker : Callable):
      self.id = operation_id
      self.access_required = access_required
      self.worker = worker

class Resource:
    def __init__(self, resource_id: str, resource: Any):
        self.id = resource_id
        self.resource = resource
        self.operations_defined = {}
    
    def addOperation(self, operation: Operation):
       if operation.id in self.operations_defined:
          raise Exception(f"[ERROR]: Operation, {operation.id} already defined in Resource {self.id}")
       self.operations_defined[operation.id] = operation



   
@dataclass 
class GlobalResourceManager:
   def __init__(self):
        self.__registry__ = {} 
   def defineResource(self, resource : Resource):
      if resource.id in self.__registry__:
         raise Exception("Operation Alread Defined")
      else:
         self.__registry__[resource.id] = resource


resources = GlobalResourceManager()
resources.defineResource(res := Resource("hello", [1, 2, 3]))
res.addOperation(Operation(resource_id=res.id, access_required=ACCESS.READ, operation_id="getElement", worker=lambda index: res.resource[index]))

'''

User interact with resources
    - Resource have Access To

''' 


user_db = {}

class User:
    def __init__(self, username):
        self.id = username
        self.type = None
        self.rights = {}
        if self.id not in user_db:
            user_db[self.id] = self
            print("[INFO]: User Created Sucessfully")
        else:
            raise Exception(f"[ERROR]: User, {self.id} Already Exists")

    def callAPI(self, resource_id: str, operation_id: str, context: Any):
        if resource_id not in self.rights:
           raise Exception(f"[ERROR]: Resource, {resource_id}")
        access_granted = self.rights[resource_id]
        resource = resources[resource_id]
        if op := resource.operation_define.get(operation_id, None) == None:
           raise Exception(f"[ERROR]: Operation, {operation_id} doesnt exist!!")
        if op.access_required & access_granted == 0:
            raise Exception(f"[ERROR]: Forbidden Access Not Allowed")
        return op.worker(context)
           
       
    


      
user = User("mister")










exit()

df = pd.read_csv("products.csv")

def transform(df):
    df.set_index("id", inplace=True)
    df["desc"] = df["name"].apply(lambda x: " ".join(x.split()[3:]))
    df["name"] = df["name"].apply(lambda x: " ".join(x.split()[:3]))
    df["currency"] = df["price"].apply(lambda x: "$" if x[0] == "$" else None)
    df["price"] = df["price"].apply(lambda x: float(x[1:]))

transform(df)




class BaseModel(SQLModel):
   __abstract__ = True
   metadata = MetaData(schema="Products")

engine = create_engine("postgresql+psycopg2://mind:mind@localhost/walmart", echo=True)

class Product(BaseModel, table=True):
   id: int | None = Field(default=None, primary_key=True)
   name: str 
   desc: str
   price: int 
   status: str = Field(nullable=False)
   currency : str = Field(default="$")


try:
   BaseModel.metadata.create_all(engine)
except Exception as e:
   print("[ERROR]: Problem while creating table", e)


