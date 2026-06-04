from oulu_rf.link_budget import fspl_db

def test_fspl():
    assert fspl_db(1,2400) > 90
