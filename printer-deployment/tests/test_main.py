from src.main import deployment_status, recommend_print_action


def test_non_bonding_text_selects_fuser_path():
    assert recommend_print_action("text does not stick to the paper") == "inspect_or_replace_fuser"


def test_one_sided_duplex_selects_setup_check():
    assert recommend_print_action("duplex job prints one side") == "verify_duplex_setup"


def test_repeated_marks_select_drum_and_rollers():
    assert recommend_print_action("repeated marks on paper") == "inspect_drum_and_feed_rollers"


def test_missing_evidence_blocks_deployment():
    assert deployment_status({"controlled_print": True, "repeat_check": False}) == "BLOCKED"


def test_all_required_checks_pass_ready():
    assert deployment_status({"controlled_print": True, "repeat_check": True}) == "READY"
