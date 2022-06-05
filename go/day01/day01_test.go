package main

import "testing"

func TestDay1(t *testing.T) {
	expected := 1692

	positions, err := parse_input()
	if err != nil {
		t.Fatalf("input not parsed correctly: %s", err)
	}

	ans, err := part1(positions)
	if err != nil {
		t.Errorf("part1 threw error: %s", err)
	}

	if ans != expected {
		t.Errorf("part1 returned %d, expected %d", ans, expected)
	}
}

func TestDay2(t *testing.T) {
	expected := 1724

	positions, err := parse_input()
	if err != nil {
		t.Fatalf("input not parsed correctly: %s", err)
	}

	ans, err := part2(positions)
	if err != nil {
		t.Errorf("part2 threw error: %s", err)
	}

	if ans != expected {
		t.Errorf("part2 returned %d, expected %d", ans, expected)
	}
}
