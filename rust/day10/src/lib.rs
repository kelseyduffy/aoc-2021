use std::fmt::Error;

pub enum Fault {
    Corrupt(u64),
    Incomplete(u64),
}

pub fn get_puzzle_input() -> Result<Vec<Vec<char>>,Error> {
    Ok(std::fs::read_to_string(String::from("input.txt")).expect("Failed to open file")
        .lines()
        .map(|line| line.chars().collect())
        .collect())
}

pub fn get_scores() -> (u64, u64) {
    score_input(get_puzzle_input().unwrap())
}

pub fn score_input(lines: Vec<Vec<char>>) -> (u64, u64) {
    let mut corrupted_scores = 0;
    let mut incomplete_scores = 0;

    for line in lines {
        match score_line(line) {
            Some(Fault::Corrupt(x)) => corrupted_scores += x,
            Some(Fault::Incomplete(x)) => incomplete_scores += x,
            _ => (),
        };
    }

    (corrupted_scores, incomplete_scores)
}

pub fn score_line(_line: Vec<char>) -> Option<Fault> {
    None
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let (rust_p1, rustp2) = get_scores();
        let (python_p1, pythonp2) = (411471, 3122628974);
        
        assert_eq!(rust_p1, python_p1, "part 1 failed");
        assert_eq!(rustp2, pythonp2, "part 2 failed");
    }
}
