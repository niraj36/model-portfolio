"""Initial schema

Revision ID: d170ea4d3223
Revises: 
Create Date: 2017-11-19 02:12:17.574522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd170ea4d3223'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Investment',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Ticker', sa.String(), nullable=False),
    sa.Column('Description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('MarketDataType',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('MarketData',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('InvestmentId', sa.Integer(), nullable=False),
    sa.Column('MarketDataTypeId', sa.Integer(), nullable=False),
    sa.Column('Value', sa.Float(), nullable=False),
    sa.Column('Source', sa.String(), nullable=False),
    sa.Column('CreateDate', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['InvestmentId'], ['Investment.Id'], ),
    sa.ForeignKeyConstraint(['MarketDataTypeId'], ['MarketDataType.Id'], ),
    sa.PrimaryKeyConstraint('Id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('MarketData')
    op.drop_table('MarketDataType')
    op.drop_table('Investment')
    # ### end Alembic commands ###
