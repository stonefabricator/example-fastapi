"""add foreign-key to posts table

Revision ID: 25bcb61835e8
Revises: 615a889c37ea
Create Date: 2025-04-05 22:35:13.308863

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25bcb61835e8'
down_revision: Union[str, None] = '615a889c37ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id', sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts",referent_table="users",
                          local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk',table_name="posts")
    op.drop_column('posts','owner_id')
    pass
