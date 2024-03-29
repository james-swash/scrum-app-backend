"""empty message

Revision ID: e18903a13bb4
Revises: b9e0014ec9f3
Create Date: 2019-06-13 20:39:47.483492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e18903a13bb4'
down_revision = 'b9e0014ec9f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('activity', sa.String(length=140), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_activity_created'), 'activity', ['created'], unique=False)
    op.create_index(op.f('ix_user_created'), 'user', ['created'], unique=False)
    op.create_index(op.f('ix_user_updated'), 'user', ['updated'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_updated'), table_name='user')
    op.drop_index(op.f('ix_user_created'), table_name='user')
    op.drop_index(op.f('ix_activity_created'), table_name='activity')
    op.drop_table('activity')
    # ### end Alembic commands ###
