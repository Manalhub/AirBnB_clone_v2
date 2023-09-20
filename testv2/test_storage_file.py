mport unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        # Test if all() returns a dictionary
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_all_with_cls(self):
        # Test if all(cls) returns a dictionary containing only objects of that class
        user = User()
        user.save()
        place = Place()
        place.save()

        result = self.storage.all(User)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 1)
        self.assertIn(user.id, result)
        self.assertNotIn(place.id, result)

    def test_new(self):
        # Test if new() adds a new object to the storage dictionary
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(obj.id, self.storage.all())

    def test_save_and_reload(self):
        # Test if save() and reload() correctly save and reload data
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertEqual(len(self.storage.all()), len(new_storage.all()))
        self.assertIn(obj.id, new_storage.all())

    def test_delete(self):
        # Test if delete() deletes an object from the storage dictionary
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.delete(obj)
        self.assertNotIn(obj.id, self.storage.all())

    def test_reload_nonexistent_file(self):
        # Test if reload() handles the case where the file doesn't exist
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        new_storage = FileStorage()
        new_storage.reload()
        self.assertEqual(len(new_storage.all()), 0)

    def test_reload_empty_file(self):
        # Test if reload() handles the case where the file is empty
        with open("file.json", "w") as f:
            f.write("")
        new_storage = FileStorage()
        new_storage.reload()
        self.assertEqual(len(new_storage.all()), 0)

    def test_reload_invalid_json(self):
        # Test if reload() handles the case where the file contains invalid JSON
        with open("file.json", "w") as f:
            f.write("invalid json")
        new_storage = FileStorage()
        new_storage.reload()
        self.assertEqual(len(new_storage.all()), 0)

if __name__ == '__main__':
    unittest.main()

