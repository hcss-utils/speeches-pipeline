"""Initial Migraton from hidden connection string

Revision ID: 1515436d6989
Revises: 
Create Date: 2021-12-13 19:45:16.529227

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '1515436d6989'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('speeches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('text', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('URL', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('category', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_speeches_URL'), 'speeches', ['URL'], unique=False)
    op.create_index(op.f('ix_speeches_category'), 'speeches', ['category'], unique=False)
    op.create_index(op.f('ix_speeches_created_at'), 'speeches', ['created_at'], unique=False)
    op.create_index(op.f('ix_speeches_date'), 'speeches', ['date'], unique=False)
    op.create_index(op.f('ix_speeches_id'), 'speeches', ['id'], unique=False)
    op.create_index(op.f('ix_speeches_text'), 'speeches', ['text'], unique=False)
    op.create_index(op.f('ix_speeches_title'), 'speeches', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_speeches_title'), table_name='speeches')
    op.drop_index(op.f('ix_speeches_text'), table_name='speeches')
    op.drop_index(op.f('ix_speeches_id'), table_name='speeches')
    op.drop_index(op.f('ix_speeches_date'), table_name='speeches')
    op.drop_index(op.f('ix_speeches_created_at'), table_name='speeches')
    op.drop_index(op.f('ix_speeches_category'), table_name='speeches')
    op.drop_index(op.f('ix_speeches_URL'), table_name='speeches')
    op.drop_table('speeches')
    # ### end Alembic commands ###