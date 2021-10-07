import pytest
import numpy as np

from cs506 import matrix, read

@pytest.mark.parametrize("datapath", [
    ("tests/test_files/matrix_1.csv")
])
def test_4by4_determinant(datapath):
    data = np.array(read.read_csv(datapath))
    result = matrix.get_determinant(data)
    assert result == round(np.linalg.det(data))

@pytest.mark.parametrize("datapath", [
    ("tests/test_files/matrix_2.csv")
])
def test_5by5_determinant(datapath):
    data = np.array(read.read_csv(datapath))
    result = matrix.get_determinant(data)
    assert result == round(np.linalg.det(data))

@pytest.mark.parametrize("datapath", [
    ("tests/test_files/matrix_3.csv")
])
def test_2by2_determinant(datapath):
    data = np.array(read.read_csv(datapath))
    result = matrix.get_determinant(data)
    assert result == round(np.linalg.det(data))

@pytest.mark.parametrize("datapath", [
    ("tests/test_files/invalid_matrix.csv")
])
def test_invalid_matrix(datapath):
    data = np.array(read.read_csv(datapath))
    result = matrix.get_determinant(data)
    assert result == -1