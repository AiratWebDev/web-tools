from sqlalchemy.orm import Session
from models import Links
from schemas import LinksSchema


def get_link_by_id(db: Session, link_id: int):
    return db.query(Links).filter(Links.id == link_id).first()


def get_link_by_short_link(db: Session, short_link: str):
    return db.query(Links).filter(Links.short_link == short_link).first()


def get_links(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Links).offset(skip).limit(limit).all()


def create_link(db: Session, full_link: str, short_link: str):
    _link = Links(full_link=full_link, short_link=short_link)
    db.add(_link)
    db.commit()
    db.refresh(_link)


def remove_link_by_id(db: Session, link_id: int):
    _link = get_link_by_id(db=db, link_id=link_id)
    db.delete(_link)
    db.commit()


def update_link(db: Session, link_id: int, full_link: str, short_link: str):
    _link = get_link_by_id(db=db, link_id=link_id)
    _link.full_link = full_link
    _link.short_link = short_link
    db.commit()
    db.refresh(_link)
    return _link

