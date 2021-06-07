"""empty message

Revision ID: 4d9e38c58362
Revises: 362c18e83e6f
Create Date: 2021-06-07 07:32:25.825440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d9e38c58362'
down_revision = '362c18e83e6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('featured', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'featured')
    # ### end Alembic commands ###
