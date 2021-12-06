use std::fmt::Error;
use std::cmp;

pub struct Point {
    x: u32,
    y: u32,
}

pub struct Line {
    start: Point,
    end: Point,
    style: Direction,
}

pub enum Direction {
    Horizontal(i32),
    Vertical(i32),
    Diagnol(i32, i32),
    Unknown,
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
        
        let start = Point::new(parts[0]);
        let end = Point::new(parts[1]);
        let mut style = Direction::Unknown;

        if start.x == end.x {
            style = Direction::Vertical(if start.x < end.x {1} else {-1});
        }

        else if start.y == end.y {
            style = Direction::Horizontal(if start.y < end.y {1} else {-1});
        }

        else {
            style = Direction::Diagnol(if start.x < end.x {1} else {-1}, if start.y < end.y {1} else {-1});
        }
        
        Line { start, end, style }
    }

    pub fn max_value(&self) -> u32 {
        cmp::max(cmp::max(self.start.x, self.end.y), cmp::max(self.start.x, self.end.y))
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
    
    const MAX_VALUE: usize = 1000;

    if lines.len() == 0 {
        return None
    }

    // let mut max_val = 0;
    // for line in lines {
    //    max_val = cmp::max(max_val, Line::max_value( &line));
    //}    

    let mut counts = [0; (MAX_VALUE + 1) * (MAX_VALUE) + 1];

    for line in lines {
        match line.style {
            Direction::Horizontal(mx) => {

                let diff: i32 = (line.start.x - line.end.x).try_into().unwrap();
                let y_offset: usize = MAX_VALUE * line.start.y as usize;
                for i in 0..(diff.abs() + 1) {
                    counts[(i * mx) as usize + line.start.x as usize + y_offset] += 1;
                }

            },
            Direction::Vertical(my) => {

                let diff: i32 = (line.start.y - line.end.y).try_into().unwrap();
                for i in 0..(diff.abs() + 1) {
                    counts[(((i * my) + line.start.y as i32) * MAX_VALUE as i32) as usize + line.start.x as usize] += 1;
                }
            },
            Direction::Diagnol(mx, my) => {
                if use_diags {

                }
            },
            Direction::Unknown => (),
        };
    }

    Some(counts.iter()
        .filter(|&&x| x >= 2)
        .count().try_into().unwrap())

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
