"""added about_me and last seen

Revision ID: 06027b61f207
Revises: d6316580a7d5
Create Date: 2020-06-15 16:36:29.531555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06027b61f207'
down_revision = 'd6316580a7d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=50), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_last_seen'), 'user', ['last_seen'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_last_seen'), table_name='user')
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
