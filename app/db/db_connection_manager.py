from contextlib import asynccontextmanager
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


class AsyncSessionManager:
    def __init__(self, database_uri, echo=True, future=True, pool_pre_ping=True):
        self.engine = create_async_engine(
            database_uri,
            echo=echo,
            future=future,
            pool_pre_ping=pool_pre_ping,
            pool_size=100,
            max_overflow=20,
        )
        self.Session = sessionmaker(  # type: ignore
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autocommit=False,
            autoflush=False,
        )
        self._session = None

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.Session() as session:
            async with session.begin():
                yield session
