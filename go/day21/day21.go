package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type GameState struct {
	Player1Tile  int
	Player1Score int
	Player2Tile  int
	Player2Score int
	Player1Turn  bool
}

func main() {
	starting, err := parse_input()
	if err != nil {
		log.Fatal(err)
	}

	part1_ans, err := part1(starting)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(part1_ans)

	part2_ans, err := part2(starting)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(part2_ans)
}

func parse_input() ([2]int, error) {

	f, err := os.Open("input.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)

	var nums [2]int

	for i := 0; i < 2; i++ {
		_ = scanner.Scan()

		line := scanner.Text()

		parts := strings.Split(line, ": ")

		position, err := strconv.Atoi(parts[1])
		if err != nil {
			return nums, err
		}

		nums[i] = position
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return nums, nil
}

func part1(starting [2]int) (int, error) {
	winningScore := 1000
	var game GameState = GameState{starting[0], 0, starting[1], 0, true}
	die := 0

	for game.Player1Score < winningScore && game.Player2Score < winningScore {
		if game.Player1Turn {
			for count := 0; count < 3; count++ {
				die++
				game.Player1Tile += (die - 1%100) + 1
			}
			game.Player1Tile = ((game.Player1Tile - 1) % 10) + 1
			game.Player1Score += game.Player1Tile
			game.Player1Turn = false
		} else {
			for count := 0; count < 3; count++ {
				die++
				game.Player2Tile += (die - 1%100) + 1
			}
			game.Player2Tile = ((game.Player2Tile - 1) % 10) + 1
			game.Player2Score += game.Player2Tile
			game.Player1Turn = true
		}
	}
	if game.Player1Turn {
		return game.Player1Score * die, nil
	} else {
		return game.Player2Score * die, nil
	}
}

func part2(starting [2]int) (int, error) {
	return 0, nil
}
