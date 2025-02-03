"""
Project models.

Revision ID: b1106cac9c5a
Revises:
Create Date: 2025-02-01 09:59:45.515970

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "b1106cac9c5a"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "core__project",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column(
            "status",
            sa.Enum("ACTIVE", "PAUSED", "STOPED", "ON_TECHNICAL_MAINTENANCE", name="projectstatus"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("core__project")
