from sqlmodel import SQLModel


class BaseSQLModel(SQLModel):
    """
    Base SQLModel to be inherited by all other models.
    It provides the `metadata` attribute for Alembic.
    """

    pass
