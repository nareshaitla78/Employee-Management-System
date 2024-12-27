# from .app import db

# class Office(db.Model):
#     officeCode=db.Column(db.Integer,primary_key=True)
#     city=db.Column(db.String(100))
#     phone=db.Column(db.String(100))
#     addressLine1=db.Column(db.String(100))
#     addressLine2=db.Column(db.String(100))
#     state=db.Column(db.String(100))
#     country=db.Column(db.String(100))
#     postalCode=db.Column(db.String(100))
#     territory=db.Column(db.String(100))
#     def to_dict(self):
#         return{
#             'officeCode':self.officeCode,
#              'city':self.city,
#             'phone':self.phone,
#             'addressLine1':self.addressLine1,
#             'addressLine2':self.addressLine2,
#             'state':self.state,
#             'country':self.country,
#             'postalCode':self.postalCode,
#             'territory':self.territory
#         }
   