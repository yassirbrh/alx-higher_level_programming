#!/usr/bin/python3
"""
    Defining unittests for base.py.
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_three_bases(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 2)

    def test_None_id(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        base1 = Base()
        base2 = Base(12)
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 1)

    def test_id_public(self):
        baseIns = Base(12)
        baseIns.id = 15
        self.assertEqual(15, baseIns.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        rect = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([rect.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        rect = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([rect.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        rect1 = Rectangle(2, 3, 5, 19, 2)
        rect2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [rect1.to_dictionary(), rect2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_square_type(self):
        sq = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([sq.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        sq = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([sq.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        sq1 = Square(10, 2, 3, 4)
        sq2 = Square(4, 5, 21, 2)
        list_dicts = [sq1.to_dictionary(), sq2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        rect = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        sq = Square(10, 7, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        sq1 = Square(10, 7, 2, 8)
        sq2 = Square(8, 1, 2, 3)
        Square.save_to_file([sq1, sq2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        sq = Square(10, 7, 2, 8)
        Base.save_to_file([sq])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        sq = Square(9, 2, 39, 2)
        Square.save_to_file([sq])
        sq = Square(10, 7, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle_original(self):
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rect1))

    def test_create_rectangle_new(self):
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rect2))

    def test_create_rectangle_is(self):
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertIsNot(rect1, rect2)

    def test_create_rectangle_equals(self):
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dictionary = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dictionary)
        self.assertNotEqual(rect1, rect2)

    def test_create_square_original(self):
        sq1 = Square(3, 5, 1, 7)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sq1))

    def test_create_square_new(self):
        sq1 = Square(3, 5, 1, 7)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sq2))

    def test_create_square_is(self):
        sq1 = Square(3, 5, 1, 7)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertIsNot(sq1, sq2)

    def test_create_square_equals(self):
        sq1 = Square(3, 5, 1, 7)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertNotEqual(sq1, sq2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rect1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(rect2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file([sq1, sq2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(sq1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file([sq1, sq2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(sq2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file([sq1, sq2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        rect = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([rect])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([rect1, rect2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_one_square(self):
        sq = Square(10, 7, 2, 8)
        Square.save_to_file_csv([sq])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        sq1 = Square(10, 7, 2, 8)
        sq2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([sq1, sq2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_name(self):
        sq = Square(10, 7, 2, 8)
        Base.save_to_file_csv([sq])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        sq = Square(9, 2, 39, 2)
        Square.save_to_file_csv([sq])
        sq = Square(10, 7, 2, 8)
        Square.save_to_file_csv([sq])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rect1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rect2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sq1, sq2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(sq1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sq1, sq2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(sq2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([sq1, sq2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
