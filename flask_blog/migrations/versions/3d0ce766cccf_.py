"""empty message

Revision ID: 3d0ce766cccf
Revises: 
Create Date: 2021-01-12 15:18:14.988005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d0ce766cccf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'is_edited')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('is_edited', sa.BOOLEAN(), nullable=True))
    # ### end Alembic commands ###
