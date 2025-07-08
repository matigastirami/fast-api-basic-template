from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True, max_length=50)
    password: str = Field(max_length=512)

    def __repr__(self):
        return f'<User(id={self.id}, name={self.username}, email={self.password})>'
