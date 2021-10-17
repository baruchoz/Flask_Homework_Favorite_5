"""empty message

Revision ID: ffca55380c2b
Revises: bcc3095e44aa
Create Date: 2021-10-13 21:17:10.713722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffca55380c2b'
down_revision = 'bcc3095e44aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('phonebook', sa.Column('pb_username', sa.String(length=150), nullable=False))
    op.create_unique_constraint(None, 'phonebook', ['pb_username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'phonebook', type_='unique')
    op.drop_column('phonebook', 'pb_username')
    # ### end Alembic commands ###