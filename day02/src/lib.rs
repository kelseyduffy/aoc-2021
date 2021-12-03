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
            Operation::Down(x) => depth += x,
            Operation::Forward(x) => horizontal += x,
            Operation::Up(x) => depth -= x,
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
            Operation::Down(x) => aim += x,
            Operation::Forward(x) => {
                horizontal += x;
                depth += x * aim
            }
            Operation::Up(x) => aim -= x,
        };
    }

    Some((depth * horizontal).into())
}

pub fn get_puzzle_input() -> Result<Vec<Operation>,Error> {
    //std::fs::read_to_string(String::from("input.txt")).expect("Failed to open file")
    //    .lines()
    //    .map(|line| line.split(' '))
    //    .collect()

    let input = std::fs::read_to_string(String::from("input.txt")).expect("Failed to open file");
    let mut ops: Vec<Operation> = Vec::new();

    for line in input.lines() {
        let parts: Vec<&str> = line.split(' ').collect();

        let x: i32 = parts[1].parse().expect("Failed to parse movement amount");
        let dir: &str = &parts[0][..];

        match dir {
            "up" => ops.push(Operation::Up(x)),
            "down" => ops.push(Operation::Down(x)),
            "forward" => ops.push(Operation::Forward(x)),
            _ => (),
        }
    }

    Ok(ops)
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
