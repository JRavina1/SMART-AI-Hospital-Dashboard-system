import unittest
from unittest.mock import Mock, patch

import sys
#sys.path.append("C:\Users\jigne\OneDrive - Brunel University London\FYP\TestingApp\MainDashboard.py")

sys.path.append(r"C:\Users\jigne\OneDrive - Brunel University London\FYP\TestingApp\MainDashboard.py")

# Import the Dashboard class from the MainDashboard module
from MainDashboard import Dashboard


class TestDashboard(unittest.TestCase):
    def setUp(self):
        # Initialize Dashboard with mocked Tk instance
        self.mock_tk = Mock()
        self.dashboard = Dashboard(self.mock_tk)

    def test_login_success(self):      
        # Test login with correct credentials
        self.dashboard.username_entry.get = Mock(return_value="Admin")
        self.dashboard.password_entry.get = Mock(return_value="Hospital123")     
        # Patch messagebox.showerror to prevent actual GUI pop-up
        with patch('tkinter.messagebox.showerror'):
            self.dashboard.login()     
        # Assert that the dashboard frame is created
        self.assertTrue(hasattr(self.dashboard, 'dashboard_frame'))

    def test_login_failure(self):      
        # Test login with incorrect credentials
        self.dashboard.username_entry.get = Mock(return_value="Admin")
        self.dashboard.password_entry.get = Mock(return_value="wrong_password")  
        # Patch messagebox.showerror to prevent actual GUI pop-up
        with patch('tkinter.messagebox.showerror') as mock_showerror:
            self.dashboard.login()     
        # Assert that messagebox.showerror is called
        mock_showerror.assert_called_once()

    # Add more unit tests for other methods in the Dashboard class

if __name__ == '__main__':
    unittest.main()
