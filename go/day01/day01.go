package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {

	positions, err := parse_input()
	if err != nil {
		log.Fatal(err)
	}

	part1_ans, err := part1(positions)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(part1_ans)

	part2_ans, err := part2(positions)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(part2_ans)
}

func parse_input() ([]int, error) {

	f, err := os.Open("input.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)

	var nums []int

	for scanner.Scan() {
		num, err := strconv.Atoi(scanner.Text())

		if err != nil {
			return nil, err
		}

		nums = append(nums, num)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return nums, nil
}

func part1(positions []int) (int, error) {

	if len(positions) < 2 {
		return 0, fmt.Errorf("Input int slice had length %d but expected >= 2", len(positions))
	}

	total := 0

	for i := 1; i < len(positions); i++ {
		if positions[i] > positions[i-1] {
			total += 1
		}
	}

	return total, nil
}

func part2(positions []int) (int, error) {

	if len(positions) < 4 {
		return 0, fmt.Errorf("Input int slice had length %d but expected >= 4", len(positions))
	}

	total := 0

	for i := 3; i < len(positions); i++ {
		if positions[i] > positions[i-3] {
			total += 1
		}
	}

	return total, nil
}
