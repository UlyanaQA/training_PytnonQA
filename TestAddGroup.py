# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

# Test add group. One fixture
@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="group1", header="test group1 header", footer="test grioup1 footer"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

