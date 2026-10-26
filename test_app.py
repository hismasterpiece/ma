import pytest

from app import pyramid


def test_pyramid(capsys):
    pyramid(3)

    assert capsys.readouterr().out == "  #\n ###\n#####\n"


def test_pyramid_with_no_rows(capsys):
    pyramid(0)

    assert capsys.readouterr().out == ""


@pytest.mark.parametrize("height", [-1, 1.5, True])
def test_pyramid_rejects_invalid_height(height):
    with pytest.raises(ValueError):
        pyramid(height)