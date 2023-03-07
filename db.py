import model
import pandas as pd


def select(games):
    """
    Runs a select query on the database

    :param games: model.Games - Games object with the table information
    :return: pandas.DataFrame - Rows returned from the SQL query.
    """
    games_dict = {"id": [], "title": [], "developer": [], "started": [], "finished": []}
    games = model.session.query(games)
    for game in games:
        games_dict["id"].append(game.id)
        games_dict["title"].append(game.title)
        games_dict["developer"].append(game.developer)
        games_dict["started"].append(game.started)
        games_dict["finished"].append(game.finished)

    df = pd.DataFrame(games_dict)
    return df


def add(game):
    model.session.add(game)
    model.session.commit()


def update_title(new_title, title, games):
    game = model.session.query(games).filter(games.title == title).first()
    game.title = new_title
    model.session.commit()


def update_started(title, games, status):
    game = model.session.query(games).filter(games.title == title).first()
    game.started = status
    model.session.commit()


def update_finished(title, games, status):
    game = model.session.query(games).filter(games.title == title).first()
    game.finished = status
    model.session.commit()


def delete(games, title):
    game = model.session.query(games).filter(games.title == title).first()
    model.session.delete(game)
    model.session.commit()
