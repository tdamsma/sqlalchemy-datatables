"""Flask tutorial views."""
from flask import render_template, request, jsonify

from datatables import ColumnDT, DataTables

import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('../app.cfg')
db = SQLAlchemy(app)


class User(db.Model):

    """Define a User."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    address = db.relationship(
        'Address', uselist=False, backref=db.backref('user'))

    def __unicode__(self):
        """Give a readable representation of an instance."""
        return '%s' % self.name

    def __repr__(self):
        """Give a unambiguous representation of an instance."""
        return '<%s#%s>' % (self.__class__.__name__, self.id)


class Address(db.Model):

    """Define an Address."""

    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Unicode, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __unicode__(self):
        """Give a readable representation of an instance."""
        return '%s' % (self.id)

    def __repr__(self):
        """Give a unambiguous representation of an instance."""
        return '<%s#%s>' % (self.__class__.__name__, self.id)


@app.route("/")
def home():
    """Try to connect to database, and list available examples."""
    return render_template('home.html', project='flask_tut')


@app.route("/dt_110x")
def dt_110x():
    """List users with DataTables <= 1.10.x."""
    return render_template('dt_110x.html', project='dt_110x')


@app.route('/data')
def data():
    """Return server side data."""
    # defining columns
    columns = [
        ColumnDT(User.id),
        ColumnDT(User.name),
        ColumnDT(Address.description),
        ColumnDT(User.created_at)
    ]

    # defining the initial query depending on your purpose
    query = db.session.query().\
        select_from(User).\
        join(Address).\
        filter(Address.id > 14)

    # GET parameters
    params = request.args.to_dict()

    # instantiating a DataTable for the query and table needed
    rowTable = DataTables(params, query, columns)

    # returns what is needed by DataTable
    return jsonify(rowTable.output_result())


if __name__ == "__main__":
    app.run('0.0.0.0', port=5678, debug=True)
