from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    message = "message"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(message, None)

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(None, 0)

    assert encrypt_message(message, 0) == "egassem"

    assert encrypt_message(message, 1) == "m_egasse"

    assert encrypt_message(message, 2) == "egass_em"
