"""create update event database task table

Revision ID: 958548ca6d07
Revises: ad009ed08b4f
Create Date: 2019-05-26 13:04:37.762104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "958548ca6d07"
down_revision = "ad009ed08b4f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "fetch_new_events_task",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("data", sa.JSON(), nullable=True),
        sa.ForeignKeyConstraint(["id"], ["task.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("fetch_new_events_task")
    # ### end Alembic commands ###