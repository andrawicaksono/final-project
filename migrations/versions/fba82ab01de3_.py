"""empty message

Revision ID: fba82ab01de3
Revises: cb557b7f612f
Create Date: 2022-11-30 14:21:21.596995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fba82ab01de3'
down_revision = 'cb557b7f612f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('products_title_category_id_condition_key', 'products', type_='unique')
    op.create_unique_constraint(None, 'products', ['title', 'category_id', 'condition', 'brand_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'products', type_='unique')
    op.create_unique_constraint('products_title_category_id_condition_key', 'products', ['title', 'category_id', 'condition'])
    # ### end Alembic commands ###
