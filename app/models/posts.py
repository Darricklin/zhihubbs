from datetime import datetime
from app.extensions import db
class Base:
    #添加一条数据
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
    #添加多条数据
    @staticmethod
    def save_all(*args):
        try:
            db.session.add_all(args)
            db.session.commit()
        except:
            db.session.rollback()
    #自定义删除基类
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()

class Posts(Base,db.Model):
    __tablename__='posts'
    id=db.Column(db.Integer,primary_key=True, nullable=False)
    create_time=db.Column(db.DateTime,default=datetime.now)
    title=db.Column(db.String(255))
    content=db.Column(db.Text)
    tag=db.Column(db.String(255))
    author=db.Column(db.String(255))


