import model
import pandas as pd


def select(games):
    """
    Runs a select query on the database

    :param games: model.Games - Games object with information on the games table
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
    """
    Runs an insert query on the database and commits the changes

    :param game: model.Games - Games object with information on the games table
    """
    model.session.add(game)
    model.session.commit()


def update_title(new_title, title, games):
    """
    Runs an update query on the database for the title column and commits the changes

    :param new_title: string - The updated title
    :param title: string - The title to be updated
    :param games: model.Games - Games object with information on the games table
    """
    game = model.session.query(games).filter(games.title == title).first()
    game.title = new_title
    model.session.commit()


def update_started(title, games, status):
    """
    Runs an update query on the database for the started column and commits the changes.

    :param title: string - The title of the game to be updated
    :param games: model.Games - Games object with information on the games table
    :param status: boolean - The updated status for the started column
    """
    game = model.session.query(games).filter(games.title == title).first()
    game.started = status
    model.session.commit()


def update_finished(title, games, status):
    """
    Runs an update query on the database for the finished column and commits the changes.

    :param title: string - The title of the game to be updated.
    :param games: model.Games - Games object with information on the games table
    :param status: boolean - The updated status for the finished column.
    :return:
    """
    game = model.session.query(games).filter(games.title == title).first()
    game.finished = status
    model.session.commit()


def delete(games, title):
    """
    Runs a delete query on the database for a specific row and commits the changes.

    :param games: model.Games - Games object with information on the games table
    :param title: string - The title of the game to be updated.
    """
    game = model.session.query(games).filter(games.title == title).first()
    model.session.delete(game)
    model.session.commit()
