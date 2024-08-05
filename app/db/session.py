from app.core.settings import settings
from app.db.db_connection_manager import AsyncSessionManager

async_db_manager = AsyncSessionManager(settings.SQLALCHEMY_DATABASE_URI)
