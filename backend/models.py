from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum, Boolean, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import enum

class UserType(str, enum.Enum):
    FREELANCER = "freelancer"
    CLIENT = "client"

class ProjectStatus(str, enum.Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    user_type = Column(Enum(UserType))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Profile fields
    title = Column(String, nullable=True)
    bio = Column(Text, nullable=True)
    hourly_rate = Column(Float, nullable=True)
    skills = Column(String, nullable=True)  # Comma-separated list of skills
    
    # Relationships
    projects_owned = relationship("Project", back_populates="client", foreign_keys="Project.client_id")
    projects_working = relationship("Project", back_populates="freelancer", foreign_keys="Project.freelancer_id")
    proposals = relationship("Proposal", back_populates="freelancer")
    reviews_given = relationship("Review", back_populates="reviewer", foreign_keys="Review.reviewer_id")
    reviews_received = relationship("Review", back_populates="reviewee", foreign_keys="Review.reviewee_id")

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    budget_min = Column(Float)
    budget_max = Column(Float)
    status = Column(Enum(ProjectStatus), default=ProjectStatus.OPEN)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Foreign keys
    client_id = Column(Integer, ForeignKey("users.id"))
    freelancer_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    # Relationships
    client = relationship("User", back_populates="projects_owned", foreign_keys=[client_id])
    freelancer = relationship("User", back_populates="projects_working", foreign_keys=[freelancer_id])
    proposals = relationship("Proposal", back_populates="project")
    milestones = relationship("Milestone", back_populates="project")

class Proposal(Base):
    __tablename__ = "proposals"

    id = Column(Integer, primary_key=True, index=True)
    cover_letter = Column(Text)
    proposed_amount = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Foreign keys
    project_id = Column(Integer, ForeignKey("projects.id"))
    freelancer_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationships
    project = relationship("Project", back_populates="proposals")
    freelancer = relationship("User", back_populates="proposals")

class Milestone(Base):
    __tablename__ = "milestones"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    amount = Column(Float)
    due_date = Column(DateTime)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Foreign keys
    project_id = Column(Integer, ForeignKey("projects.id"))
    
    # Relationships
    project = relationship("Project", back_populates="milestones")

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)  # 1-5 stars
    comment = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Foreign keys
    reviewer_id = Column(Integer, ForeignKey("users.id"))
    reviewee_id = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    
    # Relationships
    reviewer = relationship("User", back_populates="reviews_given", foreign_keys=[reviewer_id])
    reviewee = relationship("User", back_populates="reviews_received", foreign_keys=[reviewee_id])

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    read = Column(Boolean, default=False)
    
    # Foreign keys
    sender_id = Column(Integer, ForeignKey("users.id"))
    receiver_id = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id", nullable=True))
