from pydantic import BaseModel,Field,EmailStr,validator,root_validator

data = ['info@mail.ru', 'vasya@info.com']
class User(BaseModel):
    name : str = Field(min_length=4, max_length=10)
    age: int
    email:EmailStr
    text:str
    @validator('email', pre=True)
    def validate_email(cls,value):
        if value in data:
            raise ValueError('email is not uniqe')
        return value

    @root_validator(pre=True)
    def validate_name_in_email(cls, value):
        if value['name'] not in value['email']:
            raise ValueError('имя не содержится в почте')

        value['text']= value['name'] + value['email']
        return value
vasya = User(name='petya',age =45,email="petya@info.com")
print(vasya.dict())
