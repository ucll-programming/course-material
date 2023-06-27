def test_script(capsys):
    import sayhello

    captured = capsys.readouterr()
    output = captured.out

    assert output == 'Hello!\n', f"Expected output is 'Hello!', instead you printed 'Hello'"
