from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, String, Integer, Column, text, Select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from pydantic import BaseModel, EmailStr
from typing import Optional
import os

DATABASE_URL = "postgresql://postgres.ayblbybspmwvppczyigo:fJ7EwNdpqTkIEJLT@aws-1-ap-southeast-2.pooler.supabase.com:5432/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass
class User(Base):
    __tablename__ = "test_table"
    id = Column(Integer, primary_key=True, index=True)

db = SessionLocal()

result = db.query(Select(User).where(User.id == 1).subquery()).all()

print(result)