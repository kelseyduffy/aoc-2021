package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type move struct {
	Direction string
	Amount    int
}

func main() {
	moves, err := parse_input()
	if err != nil {
		log.Fatal(err)
	}

	part1_ans, err := part1(moves)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(part1_ans)

	part2_ans, err := part2(moves)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(part2_ans)
}

func parse_input() ([]move, error) {
	f, err := os.Open("input.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)

	var moves []move

	for scanner.Scan() {
		line := scanner.Text()

		parts := strings.Split(line, " ")

		amount, err := strconv.Atoi(parts[1])
		if err != nil {
			return nil, err
		}

		moves = append(moves, move{parts[0], amount})
	}

	return moves, nil
}

func part1(moves []move) (int, error) {
	var depth, horiz int

	for _, thisMove := range moves {
		switch thisMove.Direction {
		case "up":
			depth -= thisMove.Amount
		case "down":
			depth += thisMove.Amount
		case "forward":
			horiz += thisMove.Amount
		default:
			return 0, fmt.Errorf("error parsing instruction of %s", thisMove.Direction)
		}
	}
	return horiz * depth, nil
}

func part2(moves []move) (int, error) {
	var depth, horiz, aim int

	for _, thisMove := range moves {
		switch thisMove.Direction {
		case "up":
			aim -= thisMove.Amount
		case "down":
			aim += thisMove.Amount
		case "forward":
			horiz += thisMove.Amount
			depth += thisMove.Amount * aim
		default:
			return 0, fmt.Errorf("error parsing instruction of %s", thisMove.Direction)
		}
	}
	return horiz * depth, nil
}
