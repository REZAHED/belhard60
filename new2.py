from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from settings import DATABASE_ASYNC_URL
from models import Category

engine = create_async_engine(DATABASE_ASYNC_URL)

def create_async_session(func):
    async def wrapper(**kwargs):
        async with AsyncSession(bind=engine) as session:
            return await func(**kwargs,session=session)
    return wrapper

class CRUdCategory(object):

    @staticmethod
    @create_async_session
    async def add(category: Category, session:AsyncSession = None):
        session.add(category)
        try:
            await session.commit()
        except IntegrityError:
            return None
        else:
            await  session.refresh(category)
            return category

    @staticmethod
    @create_async_session
    async def get(category_id: int, session:AsyncSession = None):
        category = await session.execute(
            select(Category).where(Category.id == category_id)

        )
        category = category.first()
        if category:
            return category[0]