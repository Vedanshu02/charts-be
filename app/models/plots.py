from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text,BigInteger 
from pydantic import ConfigDict
from app.models.base import BaseModel


class Plots(BaseModel):
    __tablename__ = "plots_data"
    
    
    fc_name: Mapped[Text] = mapped_column(Text, nullable=True)
    fc_ns: Mapped[Text] = mapped_column(Text, nullable=True)
    fc_ts: Mapped[BigInteger] = mapped_column(
        BigInteger,nullable=True
    )

    model_config = ConfigDict(from_attributes=True)
