use std::collections::HashSet;
use std::fmt::Error;

pub struct Line {
    input: Vec<HashSet<u8>>,
    output: Vec<HashSet<u8>>,
}

impl Line {
    pub fn new(line: &str) -> Line {
        let (input_string, output_string) = line.trim().split_once(" | ").unwrap();

        let input_parts = input_string.trim().split(' ');
        let output_parts = output_string.trim().split(' ');

        let input: Vec<HashSet<u8>> = input_parts
            .map(|num| string_to_hashset_bytes(num))
            .collect();

        let output: Vec<HashSet<u8>> = output_parts
            .map(|num| string_to_hashset_bytes(num))
            .collect();

        Line {
            input,
            output,
        }
    }

    fn count_1478s(&self) -> i32 {
        println!("{}", self.output.len());
        println!("{}", self.output[0].len());
        self.output
            .iter()
            .filter(|x| [2,3,4,7].contains(&x.len()))
            .count().try_into().unwrap()
    }

    fn decode_output(&self) -> Result<i32,Error> {
        Ok(0)
    } 
}

pub fn part1() -> Option<i32> {
    Some(get_puzzle_input().unwrap().iter()
        .map(|line| line.count_1478s())
        .sum())
}

pub fn part2() -> Option<i32> {
    let lines = get_puzzle_input().unwrap();

    if lines.len() == 0 {
        return None
    }

    Some(lines.iter()
        .map(|line| line.decode_output().unwrap())
        .sum())
}

fn get_puzzle_input() -> Result<Vec<Line>, Error> {
    eprintln!("Getting puzzle input");

    Ok(std::fs::read_to_string(String::from("input.txt")).expect("Failed to open file")
        .lines()
        .map(|line| Line::new(&line))
        .collect())
}

fn string_to_hashset_bytes(input: &str) -> HashSet<u8> {
    let mut letters = HashSet::new();

    for byte in input.bytes() {
        letters.insert(byte);
    }

    letters
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_works() {
        let rust_result = part1();
        let python_result = 521;

        match rust_result {
            Some(x) => assert_eq!(x, python_result),
            None => panic!("No answer was returned!")
        }
    }

    #[test]
    fn part2_works() {
        let rust_result = part2();
        let python_result= 1016804;

        match rust_result {
            Some(x) => assert_eq!(x, python_result),
            None => panic!("No answer was returned!")
        }
    }
}
