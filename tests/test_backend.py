from flask_testing import TestCase
from application import app, db
from application.models import Owners
from flask import url_for, redirect
import uuid
from os import getenv

class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv("DATABASE_URI"),
                SECRET_KEY= str(uuid.uuid4)
                #WTF_CSRF_ENABLED=False


        )
        return app

    def setUp(self):
        db.create_all()
        test = Owners(owner_first_name='Test', owner_last_name='Test', owner_description='Test')
        db.session.add(test)
        db.session.commit()

    def tarDown(self):

        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)



class TestCreate(TestBase):
    def test_owner_add(self):
        with self.client:
            response = self.client.post(
                '/add_owner', 
                data=dict(
                    owner_first_name='Test1', 
                    owner_last_name='Test1', 
                    owner_description='Test1'
                ),
                follow_redirect=True
            ) 
            self.assertIn(b'Test1', response.data)

class TestDelete(TestBase):
    def test_owner_delete(self):
        response = self.client.get(url_for('delete/<int:id>', id=1))
        self.assertNotIn(b'Test', response.data)
    
