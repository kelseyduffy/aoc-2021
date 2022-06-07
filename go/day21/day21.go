package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type gameState struct {
	player1Tile  int
	player1Score int
	player2Tile  int
	player2Score int
	player1Turn  bool
}

type outcomes struct {
	player1Wins int
	player2Wins int
}

type simFunc func(state gameState, mem *memoizer) (outcomes)

type memoizer struct {
	f simFunc
	cache map[gameState]outcomes
}

func New(f simFunc) *memoizer {
	return &memoizer{f: f, cache: make(map[gameState]outcomes)}
}

func NonConcurrentGet(state gameState, mem *memoizer) (outcomes) {
	res, ok := mem.cache[state]
	if !ok {
		res = mem.f(state, mem)
		mem.cache[state] = res
	}

	return res
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

	part2C_ans, err := part2Concurrent(starting)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(part2C_ans)
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
	var game gameState = gameState{starting[0], 0, starting[1], 0, true}
	die := 0

	for game.player1Score < winningScore && game.player2Score < winningScore {
		if game.player1Turn {
			for count := 0; count < 3; count++ {
				die++
				game.player1Tile += (die - 1%100) + 1
			}
			game.player1Tile = ((game.player1Tile - 1) % 10) + 1
			game.player1Score += game.player1Tile
			game.player1Turn = false
		} else {
			for count := 0; count < 3; count++ {
				die++
				game.player2Tile += (die - 1%100) + 1
			}
			game.player2Tile = ((game.player2Tile - 1) % 10) + 1
			game.player2Score += game.player2Tile
			game.player1Turn = true
		}
	}
	if game.player1Turn {
		return game.player1Score * die, nil
	} else {
		return game.player2Score * die, nil
	}
}

func part2(starting [2]int) (int, error) {
	
	m := New(simulate)

	startingState := gameState{starting[0], 0, starting[1], 0, true}

	outcome := NonConcurrentGet(startingState, m)

	return outcome.Max(), nil
}

func part2Concurrent(starting [2]int) (int, error) {
	return 0, nil
}

func simulate(state gameState, mem *memoizer) (outcomes) {
	var outcome = outcomes{0,0} 

	for r1:=0; r1 < 4; r1++ {
		for r2:=0; r2 < 4; r2++ {
			for r3:=0; r3 < 4; r3++ {
				if state.player1Turn {
					newP1Tile := state.player1Tile + r1 + r2 + r3
					newP1Tile = ((newP1Tile - 1) % 10) + 1
					newP1Score := state.player1Score + newP1Tile
					if newP1Score >= 21 {
						outcome.player1Wins += 1
					} else {
						nextState := gameState{newP1Tile, newP1Score, state.player2Tile, state.player2Score, false}
						nextOutcomes := NonConcurrentGet(nextState, mem)
						outcome.player1Wins += nextOutcomes.player1Wins
						outcome.player2Wins += nextOutcomes.player2Wins
					}
				} else {
					newP2Tile := state.player2Tile + r1 + r2 + r3
					newP2Tile = ((newP2Tile - 1) % 10) + 1
					newP2Score := state.player2Score + newP2Tile
					if newP2Score >= 21 {
						outcome.player2Wins += 1
					} else {
						nextState := gameState{state.player1Tile, state.player1Score, newP2Tile, newP2Score, true}
						nextOutcomes := NonConcurrentGet(nextState, mem)
						outcome.player1Wins += nextOutcomes.player1Wins
						outcome.player2Wins += nextOutcomes.player2Wins
					}
				}
			}
		}
	}

	return outcome
}
func (res outcomes) Max() int {
	if res.player1Wins > res.player2Wins {
		return res.player1Wins
	} else {
		return res.player2Wins
	}
}