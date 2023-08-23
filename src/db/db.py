import asyncio

from src.core.config import app_settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import OperationalError
from src.models.base import Base
from src.models.links import Links
from src.models.transitions import Transitions
from src.core.config import db_echo_mode

engine = create_async_engine(app_settings.database_dsn, echo=db_echo_mode, future=True)
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def create_model():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def ping():
    async with async_session() as session:
        try:
            await session.get(Links, 1)
            return True
        except OperationalError:
            return False


async def add_link(full_link: str, creator: str):
    async with async_session() as session:
        link = Links(full_link=full_link, creator=creator)
        session.add(link)
        await session.commit()
        session.refresh(link)
        return link


async def del_link(link_id: int):
    async with async_session() as session:
        query = select(Links).where(Links.id == link_id)
        link = await session.scalar(query)
        if link is None:
            return False
        link.remove = True
        session.add(link)
        await session.commit()
        return True

async def find_short_link(full_link: str) -> Links:
    async with async_session() as session:
        query = select(Links).where(Links.full_link == full_link)
        link = await session.scalar(query)
        return link


async def find_full_link(short_link: int) -> Links:
    async with async_session() as session:
        query = select(Links).where(Links.id == short_link)
        link = await session.scalar(query)
        return link


async def add_transition(link: Links, user: str):
    async with async_session() as session:
        transitions = Transitions(link=link, user=user)
        session.add(transitions)
        await session.commit()


async def get_transitions(short_link: int) -> str:
    async with async_session() as session:
        query = select(Transitions).join(Transitions.link).where(Links.id == short_link)
        transitions = (await session.scalars(query)).all()
        return transitions


if __name__ == "__main__":
    asyncio.run(create_model())