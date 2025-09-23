from app import db

class DebtData(db.Model):
    """SQLAlchemy model for debt collection data"""
    __tablename__ = 'debt_data'
    
    id = db.Column(db.Integer, primary_key=True)
    total_debt = db.Column(db.Float, nullable=False)
    total_debt_payment_recieved = db.Column(db.Float, nullable=False)
    problem_solving = db.Column(db.String(20), nullable=False)
    transfer_day_diff = db.Column(db.Float, nullable=False)
    debtor_feedback = db.Column(db.String(20), nullable=False)
    total_contact = db.Column(db.Float, nullable=False)
    contact_connected = db.Column(db.Float, nullable=False)
    call_to_ptp = db.Column(db.Float, nullable=False)
    total_case_closed = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'<DebtData {self.id}>'