import unittest
import os
import sys
from io import StringIO
from models import storage
from models.base_model import BaseModel
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_STORAGE = os.getenv("HBNB_TYPE_STORAGE")


class TestBaseModel(unittest.TestCase):
    """
    Test the BaseModel class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Create a new session for each test and load the environment
        variable to use the appropriate storage type.
        """
        if DB_STORAGE == "db":
            cls.engine = create_engine('mysql+mysqldb://hbnb_test:hbnb_test_pwd@localhost/hbnb_test_db')
            Session = sessionmaker(bind=cls.engine)
            cls.session = Session()

        cls.store_all = storage.all
        storage.all = cls.fake_all

        cls.fake_stdout = StringIO()
        sys.stdout = cls.fake_stdout

    @classmethod
    def tearDownClass(cls):
        """
        Restore the original all() method and clean up the fake stdout.
        """
        storage.all = cls.store_all
        sys.stdout = sys.__stdout__

    def setUp(self):
        """
        Create a new BaseModel instance for each test.
        """
        self.model = BaseModel()
        self.model.save()

    def tearDown(self):
        """
        Clean up the session and remove the fake_stdout.
        """
        if DB_STORAGE == "db":
            self.session.close()
            storage._DBStorage__session.remove()
        self.model = None
        self.fake_stdout.close()
        self.fake_stdout = None

    @staticmethod
    def fake_all(*args, **kwargs):
        """
        Fake all() method for storage.
        """
        if DB_STORAGE == "db":
            return TestBaseModel.session.query(BaseModel).all()
        else:
            return {}

    def test_init(self):
        """
        Test BaseModel initialization.
        """
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        """
        Test save method.
        """
        updated_at_before = self.model.updated_at
        self.model.save()
        self.assertNotEqual(updated_at_before, self.model.updated_at)

    def test_to_dict(self):
        """
        Test to_dict method.
        """
        self.assertEqual(type(self.model.to_dict()), dict)
        self.assertTrue("id" in self.model.to_dict())
        self.assertTrue("created_at" in self.model.to_dict())
        self.assertTrue("updated_at" in self.model.to_dict())
        self.assertTrue("__class__" in self.model.to_dict())

    def test_str(self):
        """
        Test __str__ method.
        """
        cls_name = self.model.__class__.__name__
        self.assertIn("[{}] ({})".format(cls_name, self.model.id), str(self.model))

    def test_delete(self):
        """
        Test delete method.
        """
        self.model.delete()
        self.assertNotIn(self.model, storage.all().values())

    @unittest.skipIf(DB_STORAGE == "db", "Only applies to FileStorage")
    def test_save_to_file(self):
        """
        Test saving an object to a JSON file.
        """
        storage.save()
        file_path = storage._FileStorage__file_path
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, 'r') as file:
            content = file.read()
            self.assertTrue(len(content) > 0)
            self.assertIn(self.model.id, content)
            self.assertIn(self.model.__class__.__name__, content)

    @unittest.skipIf(DB_STORAGE == "db", "Only applies to FileStorage")
    def test_reload_from_file(self):
        """
        Test reloading objects from a JSON file.
        """
        storage.save()
        file_path = storage._FileStorage__file_path
        with open(file_path, 'r') as file:
            content = file.read()
        self.assertTrue(len(content) > 0)
        storage.reload()
        new_storage = storage.all()
        self.assertTrue(len(new_storage) > 0)
        self.assertIn(self.model.id, new_storage)
        self.assertEqual(new_storage[self.model.id].__class__, BaseModel)

    def test_has_attr(self):
        """
        Test BaseModel has attributes.
        """
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))

if __name__ == "__main__":
    unittest.main()
