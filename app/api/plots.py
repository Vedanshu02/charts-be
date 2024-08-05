from fastapi import APIRouter, status, Request
from app.db.operations import PlotsOperations
from app.schemas import PlotsCreateRequestSchema
from starlette.responses import JSONResponse
from app.models import Plots

plot_router = APIRouter()


class PlotRoute:

    def __init__(self):
        self.router = APIRouter(
            prefix="/api/v1",
            tags=["plots"],
            responses={404: {"description": "Not found"}},
        )

    def get_router(self):
        self.router.get("/plots", status_code=status.HTTP_200_OK)(self.list_plots)
        # self.router.post("/plots", status_code=status.HTTP_200_OK)(self.create_plots)
        return self.router          

    async def list_plots(
        self,
        request: Request,
        limit: int = 30,
        offset: int = 0,
    ):

        if limit > 50:
            limit = 50
        
        data = await PlotsOperations.list_plots(limit=limit, offset=offset)
        return JSONResponse(content=data)
    
    # async def create_plots(
    #      self,
    #      request: Request,    
    # ):
    #     data=[
    #         {"fc_name":"John Doe","fc_ns":"123e4567-e89b-12d3-a456-426614174000","fc_ts":1701705600000},
    #         {"fc_name":"Jane Smith","fc_ns":"123e4567-e89b-12d3-a456-426614174001","fc_ts":1701668041000},
    #         {"fc_name":"Alice Johnson","fc_ns":"123e4567-e89b-12d3-a456-426614174002","fc_ts":1701244800000},
    #         {"fc_name":"Bob Brown","fc_ns":"123e4567-e89b-12d3-a456-426614174003","fc_ts":1698883200000},
    #         {"fc_name":"Charlie Davis","fc_ns":"123e4567-e89b-12d3-a456-426614174004","fc_ts":1684204800000},
    #         {"fc_name":"David Evans","fc_ns":"123e4567-e89b-12d3-a456-426614174005","fc_ts":1701705601000},
    #         {"fc_name":"Eve Foster","fc_ns":"123e4567-e89b-12d3-a456-426614174006","fc_ts":1701668042000},
    #         {"fc_name":"Frank Harris","fc_ns":"123e4567-e89b-12d3-a456-426614174007","fc_ts":1701244801000},
    #         {"fc_name":"Grace Kelly","fc_ns":"123e4567-e89b-12d3-a456-426614174008","fc_ts":1698883201000},
    #         {"fc_name":"Hank Lewis","fc_ns":"123e4567-e89b-12d3-a456-426614174009","fc_ts":1684204801000},
    #         {"fc_name":"Ivy Martinez","fc_ns":"123e4567-e89b-12d3-a456-426614174010","fc_ts":1701705602000},
    #         {"fc_name":"Jack Nguyen","fc_ns":"123e4567-e89b-12d3-a456-426614174011","fc_ts":1701668043000},
    #         {"fc_name":"Karen Olson","fc_ns":"123e4567-e89b-12d3-a456-426614174012","fc_ts":1701244802000},
    #         {"fc_name":"Larry Perez","fc_ns":"123e4567-e89b-12d3-a456-426614174013","fc_ts":1698883202000},
    #         {"fc_name":"Mona Roberts","fc_ns":"123e4567-e89b-12d3-a456-426614174014","fc_ts":1684204802000},
    #         {"fc_name":"Nina Scott","fc_ns":"123e4567-e89b-12d3-a456-426614174015","fc_ts":1701705603000},
    #         {"fc_name":"Oscar Thompson","fc_ns":"123e4567-e89b-12d3-a456-426614174016","fc_ts":1701668044000},
    #         {"fc_name":"Pauline Upton","fc_ns":"123e4567-e89b-12d3-a456-426614174017","fc_ts":1701244803000},
    #         {"fc_name":"Quincy Vaughn","fc_ns":"123e4567-e89b-12d3-a456-426614174018","fc_ts":1698883203000},
    #         {"fc_name":"Rachel Wilson","fc_ns":"123e4567-e89b-12d3-a456-426614174019","fc_ts":1684204803000},
    #         {"fc_name":"Sam Young","fc_ns":"123e4567-e89b-12d3-a456-426614174020","fc_ts":1701705604000},
    #         {"fc_name":"Tina Zhang","fc_ns":"123e4567-e89b-12d3-a456-426614174021","fc_ts":1701668045000},
    #         {"fc_name":"Uma Anderson","fc_ns":"123e4567-e89b-12d3-a456-426614174022","fc_ts":1701244804000},
    #         {"fc_name":"Vince Carter","fc_ns":"123e4567-e89b-12d3-a456-426614174023","fc_ts":1698883204000},
    #         {"fc_name":"Wendy Diaz","fc_ns":"123e4567-e89b-12d3-a456-426614174024","fc_ts":1684204804000},
    #         {"fc_name":"Xander Foster","fc_ns":"123e4567-e89b-12d3-a456-426614174025","fc_ts":1701705605000},
    #         {"fc_name":"Yara Glover","fc_ns":"123e4567-e89b-12d3-a456-426614174026","fc_ts":1701668046000},
    #         {"fc_name":"Zane Hill","fc_ns":"123e4567-e89b-12d3-a456-426614174027","fc_ts":1701244805000},
    #         {"fc_name":"Amy Ingram","fc_ns":"123e4567-e89b-12d3-a456-426614174028","fc_ts":1698883205000},
    #         {"fc_name":"Brian Jenkins","fc_ns":"123e4567-e89b-12d3-a456-426614174029","fc_ts":1684204805000}
    #         ]
        
    #     for i in data:
    #         print("data_print",i)
    #         insert_data = Plots(**i)
    #         create_status=await PlotsOperations.create_plots(insert_data)
            
    #         if(create_status==False):
    #             return JSONResponse(content={"message": "Not Created"}, status_code=status.HTTP_400_BAD_REQUEST)
        
    #     return JSONResponse(content={"message":"OK"}, status_code=status.HTTP_201_CREATED)    