from typing import Optional
from sqlalchemy import create_engine, select, update, delete,or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from settings import DATABASE_URL
from models import Category,Product

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def create_session(func):
    def wrapper(**kwargs):
        with Session() as session:
            return func(**kwargs, session=session)
    return wrapper
class CRUDCategory:

    @staticmethod
    @create_session
    def add(category:Category,session = None)-> Optional[Category]:
        session.add(category)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(category)
            print(category.__dict__)

    @staticmethod
    @create_session
    def get(category_id:int, session=None) -> Optional[Category]:

        category = session.execute(
            select(Category).where(Category.id == category_id)
        )
        category = category.first()
        return category[0] if category else None

    @staticmethod
    @create_session
    def update(category: Category, session=None)-> bool:
        category = category.__dict__
        del category['_sa_instance_state']

        session.execute(
            update(Category).where(Category.id == category.get('id'))
            .values(**category)
        )
        try:
            session.commit()
        except IntegrityError:
            return False
        else:
            return True

    @staticmethod
    @create_session
    def delete(category_id: int, session=None) -> None:

        session.execute(
            delete(Category)
            .where(Category.id == category_id)
        )
        session.commit()



