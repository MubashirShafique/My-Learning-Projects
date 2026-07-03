from fastapi import FastAPI
from pydantic import BaseModel,Field,computed_field
from typing import Literal,Annotated
import pickle
import pandas as pd 
from fastapi.responses import JSONResponse


# import the ml model 
with open("Model.pkl",'rb') as f:
    model=pickle.load(f)



app=FastAPI()

# pdantic model to validate incoming data
class UserInput(BaseModel):

    age:Annotated[int,Field(...,gt=0,lt=120,description="age of the user ")]
    weigth:Annotated[float,Field(...,gt=0,description="weight of the user ")]
    height:Annotated[float,Field(...,gt=0,lt=2.5,description="heigth of the user ")]
    income_lpa:Annotated[float,Field(...,gt=0,description="Anual salary of the User ")]
    smoker:Annotated[bool,Field(...,description="is User a Smoker")]
    occupation:Annotated[Literal['retired', 'freelancer', 'student', 'government_job','business_owner', 'unemployed', 'private_job'],Field(...,description="Occupation of the user ")]

    @computed_field
    @property
    def bmi(self ) ->float:
        return self.weigth/self.height**2
    

    @computed_field
    @property
    def lifestyle_risk(self) ->str:
        if  self.smoker and self.bmi > 30:
            return "heigh"
        elif self.smoker and self.bmi >27:
            return "medium"
        else:
                return "low"


@app.post("/predict")
def predict_permium(data:UserInput):
     input_df=pd.DataFrame([{'bmi':data.bmi,"age":data.age,"lifestyle_risk":data.lifestyle_risk,"income_lpa":data.income_lpa,
                    "occupation":data.occupation}])
     prediction = model.predict(input_df)[0]
     # Label mapping (XGBoost numbers ko wapas categories mein badalne ke liye)
     categories_map = {0: "High", 1: "Low", 2: "Medium"}
     # Numeric output ko wapas category mein convert karna
     prediction_label = categories_map.get(prediction, prediction)
     return JSONResponse(status_code = 200,content = {"prediction_category":prediction_label})
