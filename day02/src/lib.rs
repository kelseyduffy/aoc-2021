use std::fmt::Error;

pub enum Operation {
    Up(i32),
    Down(i32),
    Forward(i32),
}

pub fn part1 () -> Option<i64> {

    let mut depth: i32 = 0;
    let mut horizontal: i32 = 0;

    let ops = get_puzzle_input().expect("Error obtaining puzzle input");

    if ops.len() == 0 {
        return None
    }

    for op in ops {
        match op {
            Some(Operation::Down(x)) => depth += x,
            Some(Operation::Forward(x)) => horizontal += x,
            Some(Operation::Up(x)) => depth -= x,
            None => (),
        };
    }

    Some((depth * horizontal).into())
}


pub fn part2 () -> Option<i64> {

    let mut depth: i32 = 0;
    let mut horizontal: i32 = 0;
    let mut aim: i32 = 0;

    let ops = get_puzzle_input().expect("Error obtaining puzzle input");

    if ops.len() == 0 {
        return None
    }

    for op in ops {
        match op {
            Some(Operation::Down(x)) => aim += x,
            Some(Operation::Forward(x)) => {
                horizontal += x;
                depth += x * aim
            }
            Some(Operation::Up(x)) => aim -= x,
            None => (),
        };
    }

    Some((depth * horizontal).into())
}

pub fn get_puzzle_input() -> Result<Vec<Option<Operation>>,Error> {
    
    Ok(std::fs::read_to_string(String::from("input.txt")).expect("Failed to open file")
        .lines()
        .map(|line| parse_line_to_operation(line))
        .collect())

}

fn parse_line_to_operation(line: &str) -> Option<Operation> {
    let parts: Vec<&str> = line.split(' ').collect();

    let x: i32 = parts[1].parse().expect("Failed to parse movement amount");
    let dir: &str = &parts[0][..];

    match dir {
        "up" => Some(Operation::Up(x)),
        "down" => Some(Operation::Down(x)),
        "forward" => Some(Operation::Forward(x)),
        _ => None,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_works() {
        let rust_answer = part1();
        let python_answer: i64 = 2073315;

        match rust_answer {
            Some(x) => assert_eq!(x, python_answer),
            None => panic!("No answer was returned!"),
        }
    }

    #[test]
    fn part2_works() {
        let rust_answer = part2();
        let python_answer: i64 = 1840311528;

        match rust_answer {
            Some(x) => assert_eq!(x, python_answer),
            None => panic!("No answer was returned!"),
        }
    }
}
