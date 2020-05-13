#!/usr/bin/env python

"""Tests for `pd_db_wrangler` package."""


import unittest
from click.testing import CliRunner

from pd_db_wrangler import pd_db_wrangler
from pd_db_wrangler import cli


class TestPd_db_wrangler(unittest.TestCase):
    """Tests for `pd_db_wrangler` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert "pd_db_wrangler.cli.main" in result.output
        help_result = runner.invoke(cli.main, ["--help"])
        assert help_result.exit_code == 0
        assert "--help  Show this message and exit." in help_result.output
