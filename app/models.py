from . import db

class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count


class Review:

    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response


class User(db.Model): #Passed in db.Model as an argument that connects our class to the database and allow communication
    __tablename__ = 'users' #__tablename__ variable allows us to give the tables in our database proper names

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255)) #db.String class specifies the data in that column should be a string with a maximum of 255 characters
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self): #__repr__method is not really important. It makes it easier to debug our applications
        return f'User {self.username}'


#Created a Role class that will define all the different roles. We create two columns for the ID and the name.
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'        