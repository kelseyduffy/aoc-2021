use std::fmt::Error;

pub struct Line <'a>{
    input: Vec<&'a [u8]>,
    output: Vec<&'a [u8]>,
}

impl Line <'_> {
    pub fn new(line: &str) -> Line {
        let (input_string, output_string) = line.trim().split_once(" | ").unwrap();
        Line {
            input: input_string.trim().split(' ').map(str::as_bytes).collect(),
            output: output_string.trim().split(' ').map(str::as_bytes).collect(),
        }
    }

    fn count_1478s(&self) -> i32 {
        0
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

fn get_puzzle_input() -> Result<Vec<Line<'static>>, Error> {
    eprintln!("Getting puzzle input");

    Ok(std::fs::read_to_string(String::from("input.txt")).expect("Failed to open file")
        .lines()
        .map(|line| Line::new(&line))
        .collect())
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
