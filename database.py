from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from config import USER, DBNAME, PORT, PASSWORD
from sqlalchemy import create_engine
from models import Workload, Base

engine = create_engine(f"postgresql://{USER}:{PASSWORD}@localhost:{PORT}/{DBNAME}",
                             isolation_level="SERIALIZABLE", )

class DataBase:

    engine = create_engine(f"postgresql://{USER}:{PASSWORD}@localhost:{PORT}/{DBNAME}",
                                 isolation_level="SERIALIZABLE", )

    def workload_writer(self,time , cpu, total_memory, used_memory, total_virtual_memory, used_virtual_memory):
        try:
            with Session(self.engine) as session:
                workload = Workload(time = str(time), cpu = str(cpu),
                                    total_memory = str(total_memory),
                                    used_memory = str(used_memory),
                                    total_virtual_memory = str(total_virtual_memory),
                                    used_virtual_memory = str(used_virtual_memory))
                with session.begin():
                    session.add_all([workload])
        except Exception as ex:
            print(ex)

def main():
    db = DataBase()
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    main()


