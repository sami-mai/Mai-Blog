"""update user table and add profile photo table

Revision ID: 7d0eeb9031f2
Revises: bf1f3a7cf743
Create Date: 2018-04-22 10:22:26.885610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d0eeb9031f2'
down_revision = 'bf1f3a7cf743'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile_photos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pic_path', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    op.drop_table('profile_photos')
    # ### end Alembic commands ###