"""add content column to post table

Revision ID: b0be247b2c2f
Revises: 5199ec85931b
Create Date: 2025-04-04 08:33:26.094297

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b0be247b2c2f'
down_revision: Union[str, None] = '5199ec85931b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content',sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
