package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type player struct {
	tile  int
	score int
}

type gameState struct {
	players [2]player
	turn    int
}

type simFunc func(state gameState, mem *memoizer) [2]int

type memoizer struct {
	f     simFunc
	cache map[gameState][2]int
}

func New(f simFunc) *memoizer {
	return &memoizer{f: f, cache: make(map[gameState][2]int)}
}

func Get(state gameState, mem *memoizer) [2]int {
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
	var game gameState = gameState{[2]player{{starting[0], 0}, {starting[1], 0}}, 0}
	die := 0

	for game.players[0].score < winningScore && game.players[1].score < winningScore {
		for count := 0; count < 3; count++ {
			die++
			game.players[game.turn].tile += (die - 1%100) + 1
		}
		game.players[game.turn].tile = ((game.players[game.turn].tile - 1) % 10) + 1
		game.players[game.turn].score += game.players[game.turn].tile
		game.turn += 1
		game.turn %= 2
	}

	return game.players[game.turn].score * die, nil
}

func part2(starting [2]int) (int, error) {

	m := New(simulate)

	startingState := gameState{[2]player{{starting[0], 0}, {starting[1], 0}}, 0}

	outcome := Get(startingState, m)

	if outcome[0] > outcome[1] {
		return outcome[0], nil
	} else {
		return outcome[1], nil
	}
}

func simulate(state gameState, mem *memoizer) [2]int {
	outcome := [2]int{0, 0}

	for r1 := 1; r1 < 4; r1++ {
		for r2 := 1; r2 < 4; r2++ {
			for r3 := 1; r3 < 4; r3++ {
				newTile := state.players[state.turn].tile + r1 + r2 + r3
				newTile = ((newTile - 1) % 10) + 1
				newScore := state.players[state.turn].score + newTile
				if newScore >= 21 {
					outcome[state.turn] += 1
				} else {
					nextTurn := (state.turn + 1) % 2
					nextState := gameState{[2]player{{0, 0}, {0, 0}}, nextTurn}
					nextState.players[state.turn].tile = newTile
					nextState.players[state.turn].score = newScore
					nextState.players[nextTurn].tile = state.players[nextTurn].tile
					nextState.players[nextTurn].score = state.players[nextTurn].score
					nextOutcomes := Get(nextState, mem)
					outcome[0] += nextOutcomes[0]
					outcome[1] += nextOutcomes[1]
				}
			}
		}
	}

	return outcome
}
