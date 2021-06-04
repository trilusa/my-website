"""empty message

Revision ID: 7978112daf6a
Revises: a166b1ee8f3c
Create Date: 2021-06-02 19:59:27.079707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7978112daf6a'
down_revision = 'a166b1ee8f3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
