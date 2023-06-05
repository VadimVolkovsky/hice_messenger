"""insert_data

Revision ID: 6073e1ef2bd6
Revises: 64aefe27d1ae
Create Date: 2023-06-03 22:30:11.401863

"""
from sqlalchemy import Integer, String
from sqlalchemy.sql import column, table

from alembic import op

# revision identifiers, used by Alembic.
revision = '6073e1ef2bd6'
down_revision = '64aefe27d1ae'
branch_labels = None
depends_on = None


user_table = table(
    'user',
    column('id', Integer),
    column('username', String),
    column('message_counter', Integer),
)


def upgrade():
    op.bulk_insert(
        user_table,
        [
            {'username': 'Vadim Volkovsky', 'message_counter': 0},
            {'username': 'Minubaev Malik', 'message_counter': 0},
            {'username': 'Erik Matiz', 'message_counter': 0},
            {'username': 'Mark Lutz', 'message_counter': 0},
            {'username': 'Andrey Pronin', 'message_counter': 0},
            {'username': 'Kate', 'message_counter': 0},
            {'username': 'Khristina', 'message_counter': 0},
            {'username': 'Napoleon', 'message_counter': 0},
            {'username': 'Egor', 'message_counter': 0},
            {'username': 'Dmitry', 'message_counter': 0},
        ]
    )


def downgrade():
    pass
