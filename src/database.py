from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime, timezone
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = "postgresql://shakiba@localhost/llm_debate_system"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Debate(Base):
    __tablename__ = "debates"

    id = Column(Integer, primary_key=True)
    question = Column(Text, nullable=False)
    models = Column(Text, nullable=False)
    personas = Column(Text, nullable=False)
    num_rounds = Column(Integer, nullable=False)
    final_answer = Column(Text, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
def init_db(): #Run this once
    Base.metadata.create_all(engine)
    print("Database tables created successfully!")

def save_debate(question, models, personas, num_rounds, final_answer):
    session = Session()
    debate = Debate(
        question=question,
        models=str(models),
        personas=str(personas),
        num_rounds=num_rounds,
        final_answer=final_answer
    )
    session.add(debate)
    session.commit()
    session.close()
    print("Debate saved to database!")

def get_all_debates():
    session = Session()
    debates = session.query(Debate).all()
    session.close()
    return debates

if __name__ == "__main__":
    init_db()