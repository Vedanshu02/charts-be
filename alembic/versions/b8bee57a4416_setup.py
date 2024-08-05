"""setup

Revision ID: b8bee57a4416
Revises: 
Create Date: 2024-08-04 19:40:27.247174

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8bee57a4416'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('basemodel',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_basemodel_id'), 'basemodel', ['id'], unique=False)
    op.create_table('plots_data',
    sa.Column('fc_name', sa.Text(), nullable=True),
    sa.Column('fc_ns', sa.Text(), nullable=True),
    sa.Column('fc_ts', sa.BigInteger(), nullable=True),
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_plots_data_id'), 'plots_data', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_plots_data_id'), table_name='plots_data')
    op.drop_table('plots_data')
    op.drop_index(op.f('ix_basemodel_id'), table_name='basemodel')
    op.drop_table('basemodel')
    # ### end Alembic commands ###
