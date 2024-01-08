"""profilecontact

Revision ID: fc7af4cfa7de
Revises: 88092daca90b
Create Date: 2023-12-28 12:09:09.978898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc7af4cfa7de'
down_revision: Union[str, None] = '88092daca90b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "contact",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(50), nullable=False),
        sa.Column("user_name", sa.String(100), nullable=False),
        sa.Column("password", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("contact")
