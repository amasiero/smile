from flask import Blueprint, render_template, request, redirect, url_for, make_response
from .extensions import db
from .models import Donation
from datetime import datetime

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/donations')
def donations():
    filter = request.args.get('filter')
    if filter == 'on':
        donations = Donation.query.order_by(Donation.date.asc()).all()
    else:
        donations = Donation.query.order_by(
            Donation.date.asc()).filter_by(collected=False)

    return render_template('donation_list.html', donations=donations, with_check=True, filter=filter)


@main.route('/donation', methods=['GET', 'POST'])
def donation():
    if request.method == 'POST':
        id = request.form.get('id')
        donator = request.form.get('donator')
        address = request.form.get('address')
        item = request.form.get('item')
        dismount = False if request.form.get('dismount') == 'False' else True
        date = datetime.strptime(request.form.get('date'), '%Y-%m-%d')

        donation = Donation(donator, item, date, dismount, address)

        if id:
            temp = Donation.query.filter_by(id=id).first()
            db.session.delete(temp)
            db.session.commit()
            donation.id = id

        db.session.add(donation)
        db.session.commit()

        return redirect(url_for('main.donations'))
    return render_template('new.html', donation=None)


@main.route('/donation/<int:_id>')
def get_donation(_id):
    donation = Donation.query.filter_by(id=_id).first_or_404()
    return render_template('new.html', donation=donation)


@main.route('/collect/<int:_id>', methods=['PUT'])
def collect(_id):
    donation = Donation.query.filter_by(id=_id).first()
    donation.collected = not donation.collected
    db.session.commit()

    res = make_response('', 200)
    res.mimeType = 'application/json'
    return res


@main.route('/search', methods=['GET', 'POST'])
def search():
    item = request.form.get('item')
    donations = []
    if item:
        donations = Donation.query.filter(
            Donation.item.contains(item)).order_by(Donation.date.asc()).filter_by(collected=False)
    return render_template('search.html', donations=donations)
