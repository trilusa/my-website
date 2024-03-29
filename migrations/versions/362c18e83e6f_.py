"""empty message

Revision ID: 362c18e83e6f
Revises: c127f2fdead1
Create Date: 2021-06-05 19:52:08.112218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '362c18e83e6f'
down_revision = 'c127f2fdead1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('description', sa.String(length=2000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'description')
    # ### end Alembic commands ###
