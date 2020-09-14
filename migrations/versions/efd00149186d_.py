"""empty message

Revision ID: efd00149186d
Revises: 5d75fada6953
Create Date: 2020-09-15 01:22:10.105929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efd00149186d'
down_revision = '5d75fada6953'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'avatar_hash')
    # ### end Alembic commands ###
