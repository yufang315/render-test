from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import os
from typing import List

# Import database configuration, models, and schemas
from database import engine, Base, get_db
import models
import schemas

# Automatically create database tables (useful for Render deployment & local SQLite setup)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book CRUD API for Render")

@app.get("/")
def read_root():
    return {"message": "Morning"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/info")
def get_info():
    return {
        "app_name": "Morning Book API",
        "version": "1.0.0",
        "description": "A FastAPI Book CRUD application integrated with Render PostgreSQL",
        "environment": "production" if os.environ.get("RENDER") == "true" else "local"
    }

# --- Book CRUD Endpoints ---

# 1. Create a Book
@app.post("/books/", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(
        title=book.title,
        author=book.author,
        description=book.description,
        published_year=book.published_year
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# 2. Read All Books (with Pagination)
@app.get("/books/", response_model=List[schemas.BookResponse])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = db.query(models.Book).offset(skip).limit(limit).all()
    return books

# 3. Read Single Book
@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

# 4. Update a Book
@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Update fields only if they are provided
    update_data = book.model_dump(exclude_unset=True) if hasattr(book, "model_dump") else book.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)
        
    db.commit()
    db.refresh(db_book)
    return db_book

# 5. Delete a Book
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return None

if __name__ == "__main__":
    import uvicorn
    # Render sets the PORT environment variable
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
