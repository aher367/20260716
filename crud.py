from sqlalchemy.orm import Session
import models

def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()

def create_book(db: Session, book: models.BookCreate):
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

def update_book(db: Session, book_id: int, book: models.BookUpdate):
    db_book = get_book(db, book_id)
    if not db_book:
        return None
    
    # Support both Pydantic v1 and v2
    update_data = book.model_dump(exclude_unset=True) if hasattr(book, "model_dump") else book.dict(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(db_book, key, value)
        
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    if not db_book:
        return None
    
    db.delete(db_book)
    db.commit()
    return db_book
