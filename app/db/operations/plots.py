from sqlalchemy import select
from app.db.session import async_db_manager
from app.models import Plots


class PlotsOperations:
    @staticmethod
    async def list_plots(limit: int, offset: int) -> list:
        data = []
        
        async with async_db_manager.get_session() as session:
            try:
                query = (
                    select(Plots)
                    .order_by(Plots.id)
                    .limit(limit=limit)
                    .offset(offset=offset)
                )
                result = await session.execute(query)
                query_data = result.scalars().all()
                await session.commit()
                if query_data:
                    for single_row in query_data:
                        data_dict = {}
                        for column in Plots.__table__.columns:
                            data_dict[column.name] = getattr(single_row, column.name)
                        print("data_dict",data_dict)
                        data.append(data_dict)
            except Exception as e:
                print(e)
        print("data_list",data)
        return data
    
    @staticmethod
    async def create_plots(data: Plots) ->bool:
        async with async_db_manager.get_session() as session:
            try:
                session.add(data)
                await session.flush()
                if data.id is None:
                    await session.refresh()
                await session.commit()
                if data.id is None:
                    await session.refresh()
            except Exception as e:
                print(e)
                return False

            return True

             