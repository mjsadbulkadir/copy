"""user

Revision ID: 65ff0548e066
Revises: 
Create Date: 2023-12-28 12:01:38.751315

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers,
# used by Alembic.
revision: str = '65ff0548e066'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(50), nullable=False),
        sa.Column("user_name", sa.String(100), nullable=False),
        sa.Column("password", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("user")
