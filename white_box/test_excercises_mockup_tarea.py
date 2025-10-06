# -*- coding: utf-8 -*-

"""
Mock up testing homework.
"""
import subprocess
import unittest
from unittest.mock import Mock, mock_open, patch

from white_box.mockup_exercises import (
    execute_command,
    perform_action_based_on_time,
    read_data_from_file,
)


class TestReadDataFromFile(unittest.TestCase):
    """
    Read data from file unittest class.
    """

    @patch(
        "white_box.mockup_exercises.open",
        new_callable=mock_open,
        read_data="Hello, world!",
    )
    def test_read_data_success(self, mock_file):
        """
        Should return file content when file exists.
        """
        result = read_data_from_file("fakefile.txt")
        mock_file.assert_called_once_with(
            "fakefile.txt", encoding="utf-8"
        )  # verificar que el archivo se abrio con open correctamente
        self.assertEqual(result, "Hello, world!")

    def test_read_data_file_not_found(self):
        """
        Should raise FileNotFoundError when file does not exist.
        """
        # assertRaises:comprobar que lanza una excepcion FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            read_data_from_file("nonexistent.txt")


class TestExecuteCommand(unittest.TestCase):
    """
    Unit tests for execute_command function.
    """

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_success(self, mock_run):
        """
        Should return stdout when command executes successfully.
        """
        # similar lo que devuelve subprocess.run
        mock_result = Mock()
        mock_result.stdout = "Command executed successfully"
        mock_run.return_value = mock_result

        result = execute_command(["echo", "hello"])
        self.assertEqual(result, "Command executed successfully")

        # verifica que subprocess.run se haya llamado correctamente
        mock_run.assert_called_once_with(
            ["echo", "hello"], capture_output=True, check=False, text=True
        )

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_error(self, mock_run):
        """
        Should raise CalledProcessError when subprocess fails.
        """
        # en vez de devolver un resultado, lanza una excepcion
        # returncode=1 fallo (0=exitoso)
        # cmd="fakecommand" el comando
        # output="Error occurred" el mensaje de error simulado
        mock_run.side_effect = subprocess.CalledProcessError(
            returncode=1, cmd="fakecommand", output="Error occurred"
        )
        # valida que se lanza la excepcion
        with self.assertRaises(subprocess.CalledProcessError):
            execute_command("fakecommand")


class TestPerformActionBasedOnTime(unittest.TestCase):
    """
    Tests for perform_action_based_on_time function.
    """

    # Reemplaza la función time.time() solo durante el test y hace que devuelva 5.
    @patch("white_box.mockup_exercises.time.time", return_value=5)
    def test_action_a_when_time_less_than_10(self, mock_time):
        """
        Should return 'Action A' when current_time < 10.
        """
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action A")
        mock_time.assert_called_once()  # Asegura que time() fue llamado una vez

    @patch("white_box.mockup_exercises.time.time", return_value=10)
    def test_action_b_when_time_greater_than_or_equal_10(self, mock_time):
        """
        Should return 'Action B' when current_time >= 10.
        """
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")
        mock_time.assert_called_once()
