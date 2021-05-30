"""empty message

Revision ID: d6316580a7d5
Revises: 
Create Date: 2020-06-15 16:04:46.460574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6316580a7d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('time_stamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_post_time_stamp'), 'post', ['time_stamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_time_stamp'), table_name='post')
    op.drop_column('post', 'time_stamp')
    # ### end Alembic commands ###
