"""empty message

Revision ID: bcc3095e44aa
Revises: 4d9211543b1b
Create Date: 2021-10-13 00:48:16.217442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcc3095e44aa'
down_revision = '4d9211543b1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('phonebook',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.Column('phone_number', sa.String(length=150), nullable=True),
    sa.Column('address', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('register_phonebook')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('register_phonebook',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=150), nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=150), nullable=True),
    sa.Column('phone_number', sa.VARCHAR(length=150), nullable=True),
    sa.Column('address', sa.VARCHAR(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('phonebook')
    # ### end Alembic commands ###