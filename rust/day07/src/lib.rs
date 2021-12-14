use std::fmt::Error;

pub fn part1 () -> Option<u64> {
    
    let _crabs = get_puzzle_input().expect("Error obtaining puzzle input");
    
    None
}

pub fn part2 () -> Option<u64> {
    
    let _crabs = get_puzzle_input().expect("Error obtaining puzzle input");

    None
}

pub fn get_puzzle_input() -> Result<Vec<u32>,Error> {
    
    Ok(std::fs::read_to_string(String::from("input.txt")).expect("Failed to open file")
        .split(',')
        .map(|line| line.parse().unwrap())
        .collect())

}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_works() {
        let rust_answer = part1();
        let python_answer: u64 = 356179;

        match rust_answer {
            Some(x) => assert_eq!(x, python_answer),
            None => panic!("No answer was returned!"),
        }
    }

    #[test]
    fn part2_works() {
        let rust_answer = part2();
        let python_answer: u64 = 99788435;

        match rust_answer {
            Some(x) => assert_eq!(x, python_answer),
            None => panic!("No answer was returned!"),
        }
    }
}
