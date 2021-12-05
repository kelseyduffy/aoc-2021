use std::fmt::Error;

pub struct Point {
    x: i32,
    y: i32,
}

pub struct Line {
    start: Point,
    end: Point,
}

impl Point {
    pub fn new(input: &str) -> Point {
        let parts: Vec<&str> = input.split(',').collect();
        Point { 
            x: parts[0].parse().unwrap(),
            y: parts[1].parse().unwrap(),
        }
    }
}

impl Line {
    pub fn new(input: &str) -> Line {
        let parts: Vec<&str> = input.split(" -> ").collect();
        Line { 
            start: Point::new(parts[0]), 
            end: Point::new(parts[1]), 
        }
    }
}

pub fn part1() -> Option<i32> {
    process_lines(get_puzzle_input().unwrap(), false)
}

pub fn part2() -> Option<i32> {
    process_lines(get_puzzle_input().unwrap(), true)
}

fn get_puzzle_input() -> Result<Vec<Line>, Error> {
    Ok(std::fs::read_to_string(String::from("input.txt")).expect("Failed to open file")
        .lines()
        .map(|line| Line::new(line))
        .collect())
}

fn process_lines(lines: Vec<Line>, use_diags: bool) -> Option<i32> {
    None
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_works() {
        let rust_result = part1();
        let python_result = 8622;

        match rust_result {
            Some(x) => assert_eq!(x, python_result),
            None => panic!("No answer was returned!")
        }
    }

    #[test]
    fn part2_works() {
        let rust_result = part2();
        let python_result= 22037;

        match rust_result {
            Some(x) => assert_eq!(x, python_result),
            None => panic!("No answer was returned!")
        }
    }
}
