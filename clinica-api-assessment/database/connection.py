from sqlmodel import SQLModel, Session, create_engine

database_file = "clinica.db"
sqlite_url = f"sqlite:///{database_file}"

connect_args = {"check_same_thread": False}
engine_url = create_engine(sqlite_url, connect_args=connect_args)

def conn():
    SQLModel.metadata.create_all(engine_url)

def get_session():
    with Session(engine_url) as session:
        yield session
