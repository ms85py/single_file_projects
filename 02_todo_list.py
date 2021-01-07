

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    task = Column(String, default="Nothing to do!")
    deadline = Column(Date, default=datetime.today().date())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def missed_tasks():
    print("\nMissed tasks:")
    query = session.query(Table).filter(Table.deadline < datetime.today().date()).order_by(Table.deadline).all()
    if query:
        for count, task in enumerate(query, 1):
            print(f"{count}. {task.task}. {task.deadline.day} {task.deadline.strftime('%b')}")
    else:
        print("Nothing was missed.\n")


def delete_task():
    print("\nEnter ID of the task you want to delete:")  # typo. can't do shit about it, it's from the site.
    query = session.query(Table).order_by(Table.deadline).all()
    if query:
        for count, task in enumerate(query, 1):
            print(f"{count}. {task.task}. {task.deadline.day} {task.deadline.strftime('%b')}")
        delete = int(input()) - 1
        try:
            session.delete(query[delete])
            session.commit()
            print("The task has been deleted.\n")
        except IndexError:
            print("Task not found.")
    else:
        print("No tasks to delete!\n")


def show_tasks():
    query = session.query(Table).filter(Table.deadline == datetime.today().date()).all()
    if not query:
        print(f"Today {datetime.today().day} {datetime.today().strftime('%b')}:")
        print("Nothing to do!\n")
    else:
        print(f"Today {datetime.today().day} {datetime.today().strftime('%b')}:")
        for count, task in enumerate(session.query(Table).filter(Table.deadline == datetime.today().date()).order_by(Table.deadline).all(), 1):
            print(f"{count}. {task.task}")


def show_weekly_tasks():
    today = datetime.today().date()
    for i in range(0, 7):
        query = session.query(Table).filter(Table.deadline == (today + timedelta(days=i))).order_by(Table.deadline).all()
        day = today + timedelta(days=i)
        print(f"\n{day.strftime('%A')} {day.day} {day.strftime('%b')}")
        if query:
            for x, q in enumerate(query, 1):
                print(f"{x}. {query[x - 1]}")
            print()
        else:
            print("Nothing to do!\n")


def show_all_tasks():
    print("\n")
    query = session.query(Table).order_by(Table.deadline).all()
    if query:
        for task in query:
            print(f"{task.task}. {task.deadline.day} {task.deadline.strftime('%b')}:")
    else:
        print("Nothing to do!\n")


def add_task():
    print("\nEnter task")
    new_task = input()
    print("Enter deadline in format Y-M-D")
    date = input()
    new = Table(task=new_task, deadline=datetime.strptime(date, '%Y-%m-%d'))
    session.add(new)
    session.commit()
    print("The task has been added!\n")



class TDL:
    def __init__(self, comm):
        self.comm = comm


    def menu(self):
        while self.comm != 0:
            try:
                self.comm = int(input("""
    1) Today's tasks
    2) Week's tasks
    3) All tasks
    4) Missed tasks
    5) Add task
    6) Delete task
    0) Exit
    """))
                if self.comm == 1:
                    show_tasks()
                elif self.comm == 2:
                    show_weekly_tasks()
                elif self.comm == 3:
                    show_all_tasks()
                elif self.comm == 4:
                    missed_tasks()
                elif self.comm == 5:
                    add_task()
                elif self.comm == 6:
                    delete_task()
            except ValueError:
                print("Invalid input!")


if __name__ == "__main__":
    inst = TDL("_")
    inst.menu()
