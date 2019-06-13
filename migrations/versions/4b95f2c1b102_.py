"""empty message

Revision ID: 4b95f2c1b102
Revises: e18903a13bb4
Create Date: 2019-06-13 22:10:09.116739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b95f2c1b102'
down_revision = 'e18903a13bb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'activity', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'activity', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###
