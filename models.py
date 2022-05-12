from dbhelper import Base
from sqlalchemy import Column, Integer, Float, DateTime, String, Text
from datetime import datetime


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    gender = Column(String(255), nullable=False)
    email_id = Column(String(255), nullable=False, unique=True)
    phone_no = Column(Integer, nullable=False)
    address = Column(String(255), nullable=False)
    school_10th = Column(String(255), nullable=False)
    year_10th = Column(String(255), nullable=False)
    percent_10th = Column(Float, nullable=False)
    college_12th = Column(String(255), nullable=False)
    year_12th = Column(String(255), nullable=False)
    percent_12th = Column(Float, nullable=False)
    diploma_university_name = Column(String(255), nullable=True)
    diploma_cource_name = Column(String(255), nullable=True)
    diploma_year = Column(String(255), nullable=True)
    diploma_percent = Column(Float, nullable=True) 
    graduation_university_name = Column(String(255), nullable=False)
    graduation_cource_name = Column(String(255), nullable=False)
    graduation_year = Column(String(255), nullable=False)
    graduation_percent = Column(Float, nullable=True)
    post_graduation_university_name = Column(String(255), nullable=False)
    post_graduation_cource_name = Column(String(255), nullable=False)
    post_graduation_year = Column(String(255), nullable=False)
    post_graduation_percent = Column(Float, nullable=True)  
    lang_link = Column(String(255), nullable=False)
    technical_skills = Column(String(255), nullable=False)
    project = Column(String(255), nullable=False)
    about = Column(String(255), nullable=False)
    record_workphoto = Column(Text, nullable=False)

    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=True, default=datetime.utcnow())

    @classmethod
    def get_user_by_chatid(cls, session, chat_id):
        return session.query(cls).filter(cls.chat_id == chat_id).first()

    @classmethod
    def get_all_users(cls, session):
        return session.query(cls).all()

    @classmethod
    def get_user_by_username(cls, session, user_name):
        return session.query(cls).filter(cls.name == user_name).first()

    

    def update_name(self, session, name):
        self.name = name
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None

    def update_gender(self, session, gender):
        self.gender = gender
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None

    def update_email(self, session, email):
        self.email_id = email
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None

    def update_phone_no(self, session, phone_no):
        self.phone_no = phone_no
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None

    def update_address(self, session, address):
        self.address = address
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None

        
    def update_school_10th(self, session, school_10th):
        self.school_10th= school_10th
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None

        
    def update_year_10th(self, session, year_10th):
        self.year_10th = year_10th
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None

    def update_percent_10th(self, session, percent_10th):
        self.percent_10th = percent_10th
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None

    def update_college_12th(self, session, college_12th):
        self.college_12th= college_12th
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None

        
    def update_year_12th(self, session, year_12th):
        self.year_12th = year_12th
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None


    def update_percent_12th(self, session, percent_12th):
        self.percent_12th = percent_12th
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None


    
    def update_diploma_university_name(self, session, diploma_university_name):
        self.diploma_university_name= diploma_university_name
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None
   
    def update_diploma_cource_name(self, session, diploma_cource_name):
        self.diploma_cource_name= diploma_cource_name
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None

        
    def update_diploma_year(self, session, diploma_year):
        self.diploma_year = diploma_year
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None


    def update_diploma_percent(self, session, diploma_percent):
        self.diploma_percent = diploma_percent
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None

    
    def update_graduation_university_name(self, session, graduation_university_name):
        self.graduation_university_name= graduation_university_name
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None
   
    def update_graduation_cource_name(self, session, graduation_cource_name):
        self.graduation_cource_name= graduation_cource_name
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None

        
    def update_graduation_year(self, session, graduation_year):
        self.graduation_year = graduation_year
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None


    def update_graduation_percent(self, session, graduation_percent):
        self.graduation_percent = graduation_percent
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None   

    
    def update_post_graduation_university_name(self, session, post_graduation_university_name):
        self.post_graduation_university_name= post_graduation_university_name
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None     

    def update_post_graduation_cource_name(self, session, post_graduation_cource_name):
        self.post_graduation_cource_name= post_graduation_cource_name
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None

        
    def update_post_graduation_year(self, session, post_graduation_year):
        self.post_graduation_year = post_graduation_year
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None


    def update_post_graduation_percent(self, session, post_graduation_percent):
        self.post_graduation_percent = post_graduation_percent
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None  

    def update_lang_link(self, session, lang_link):
        self.lang_link = lang_link
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None

    def update_technical_skills(self, session, technical_skills):
        self.technical_skills = technical_skills
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None

    def update_project(self, session, project):
        self.project = project
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None

    def update_about(self, session, about):
        self.about = about
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None

    def update_record_workphoto(self, session, record_workphoto):
        self.record_workphoto = record_workphoto
        session.add(self)
        try:
            session.commit()
            return self
        except:
            session.rollback()
            return None

    def __repr__(self):
        return f"<User: id - {self.id}, chat_id - {self.chat_id}, name - {self.name},gender - {self.gender}, email_id - {self.email_id}, phone_no - {self.phone_no},address - {self.address},school_10th-{self.school_10th},year_10th - {self.year_10th},percent_10th - {self.percent_10th},college_12th-{self.college_12th},year_12th - {self.year_12th},percent_12th -{self.percent_12th},diploma_university_name- {self.diploma_university_name},diploma_cource_name- {self.diploma_cource_name},diploma_year - {self.diploma_year},diploma_percent - {self.diploma_percent},graduation_university_name- {self.graduation_university_name},graduation_cource_name - {self.graduation_cource_name},graduation_year - {self.graduation_year},graduation_percent - {self.graduation_percent},post_graduation_university_name- {self.post_graduation_university_name},post_graduation_cource_name - {self.post_graduation_cource_name},post_graduation_year - {self.post_graduation_year},post_graduation_percent - {self.post_graduation_percent},lang_link - {self.lang_link},technical_skills - {self.technical_skills}, project - {self.project},about - {self.about}, record_workphoto-{self.record_workphoto},created_at - {self.created_at}, updated_at - {self.updated_at}>"



