"""profile

Revision ID: 88092daca90b
Revises: 65ff0548e066
Create Date: 2023-12-28 12:05:34.660860

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88092daca90b'
down_revision: Union[str, None] = '65ff0548e066'
# down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "profile",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(50), nullable=False),
        sa.Column("user_name", sa.String(100), nullable=False),
        sa.Column("password", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("profile")
