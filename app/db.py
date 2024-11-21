from sqlmodel import create_engine, Session, SQLModel

engine = create_engine(f'sqlite:///dnd_db.db', echo=False)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

