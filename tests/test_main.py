from dental_ben.main import main


def test_main(capsys) -> None:
    main()
    captured = capsys.readouterr()
    assert "Hello from Dental-Ben!" in captured.out
