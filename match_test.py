import pytest
from match import Match
from player import Player

xavier = Player('Prof. Xavier')
otto = Player('Dr Octopus')


def test_different_players_have_different_chars():
    t = Match(xavier, otto)
    assert xavier.char != otto.char


def test_no_player_with_none_char():
    t = Match(xavier, otto)
    assert xavier.char != None
    assert otto.char != None


def test_next_player_is_round_robbin():
    t = Match(otto, xavier)
    p1 = t.next_player
    p2 = t.next_player
    assert p1 != p2


def test_players_are_opponents():
    t = Match(otto, xavier)
    p1 = t.next_player
    p2 = t.next_player
    assert p1.opponent == p2
    assert p2.opponent == p1
