from flask import render_template, redirect, url_for
import src.models.recommendation


class Recommendations:
    def __init__(self):
        ""

    def index(self):
        list = src.models.recommendation.Recommendation().get_all()
        return render_template('list.html', title='Recommender system', header='Recommender system', recommendations=list)

    def new(self, request):
        params = []
        if request.method == 'POST':
            recommendation = src.models.recommendation.Recommendation(
                request.form.get('title'),
                request.form.get('description'),
                request.form.get('season_count'),
                request.form.get('still_on'),
                request.form.get('episodes_per_season'),
                request.form.get('episode_length'),
                request.form.get('trailer'),
                request.form.get('person'),
                request.form.get('associated_links')
            )

            if recommendation.valid() and recommendation.save():
                return redirect(url_for('index'))

        # @todo if form is not valid set values from request
        return render_template('new.html', title='Recommender system - add recommendation', header='Recommender system - add recommendation', params=params)
