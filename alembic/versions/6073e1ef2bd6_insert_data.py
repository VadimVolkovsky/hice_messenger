"""insert_data

Revision ID: 6073e1ef2bd6
Revises: 64aefe27d1ae
Create Date: 2023-06-03 22:30:11.401863

"""
from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date


# revision identifiers, used by Alembic.
revision = '6073e1ef2bd6'
down_revision = '64aefe27d1ae'
branch_labels = None
depends_on = None


accounts_table = table(
    'user',
    column('id', Integer),
    column('username', String),
    column('message_counter', Integer),
)


def upgrade():
    op.bulk_insert(
        accounts_table,
        [
            {'id': 1, 'username': 'Vadim Volkovsky', 'message_counter': 0},
            {'id': 2, 'username': 'Minubaev Malik', 'message_counter': 0},
            {'id': 3, 'username': 'Erik Matiz', 'message_counter': 0},
            {'id': 4, 'username': 'Mark Lutz', 'message_counter': 0},
            {'id': 5, 'username': 'Andrey Pronin', 'message_counter': 0},
            {'id': 6, 'username': 'Kate', 'message_counter': 0},
            {'id': 7, 'username': 'Khristina', 'message_counter': 0},
            {'id': 8, 'username': 'Napoleon', 'message_counter': 0},
            {'id': 9, 'username': 'Egor', 'message_counter': 0},
            {'id': 10, 'username': 'Dmitry', 'message_counter': 0},
        ]
    )


def downgrade():
    pass
