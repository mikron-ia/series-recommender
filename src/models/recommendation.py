from src import data_provider


class Recommendation:
    def __init__(self, title=None, description='', season_count=1, still_on=False, episodes='', episode_length='', trailer='', person=None, associated_links=''):
        self.title = title
        self.description = description
        self.season_count = season_count if season_count else 1
        self.still_on = True if still_on == 'Yes' else False
        self.episodes = episodes
        self.episode_length = episode_length
        self.trailer = trailer
        self.person = person
        self.associated_links = associated_links

    def valid(self):
        if self.title is None or self.title.strip() == '':
            return False

        if self.person is None or self.person.strip() == '':
            return False

        return True

    def save(self):
        sql = 'INSERT INTO recommendation VALUES (NULL, "%s", "%s", %d, "%s", "%s", "%s", "%s", "%s", "%s")' %(
            self.title,
            self.description,
            int(self.season_count),
            self.still_on,
            self.episodes,
            self.episode_length,
            self.trailer,
            self.person,
            self.associated_links
        )

        if data_provider.execute_command(sql):
            return True

        return False

    # @todo it will return array contains objects of Recommendation class
    @staticmethod
    def get_all():
        sql = 'SELECT title, description, season_count, still_on, episodes_per_season, episode_length, trailer, person, associated_links FROM recommendation'

        cursors = data_provider.connect().execute(sql)
        rows = cursors.fetchall()
        cursors.close()

        return rows
