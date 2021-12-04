"""add phone number column in users

Revision ID: 3b1ebf57f7fb
Revises: 
Create Date: 2021-12-04 02:13:41.064627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b1ebf57f7fb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
	op.add_column('users',sa.Column('Phone number',sa.String()))
	pass


def downgrade():
	op.drop_column('users','Phone number')
	pass
