def test_script(capsys):
    import student

    captured = capsys.readouterr()
    output = captured.out

    assert output == 'Hello!\n', f"Expected output is 'Hello!', instead you printed 'Hello'"
