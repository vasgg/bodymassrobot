from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from core.config import settings


class Database:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
        )


db = Database(settings.DB_URL, settings.DB_ECHO)
