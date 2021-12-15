use std::fmt::Error;

pub fn part1 () -> Option<u32> {
    
    let crabs = get_puzzle_input().expect("Error obtaining puzzle input");
    
    count_movements(crabs, false)
}

pub fn part2 () -> Option<u32> {
    
    let crabs = get_puzzle_input().expect("Error obtaining puzzle input");

    count_movements(crabs, true)
}

pub fn get_puzzle_input() -> Result<Vec<u32>,Error> {
    
    Ok(std::fs::read_to_string(String::from("input.txt")).expect("Failed to open file")
        .split(',')
        .map(|line| line.parse().unwrap())
        .collect())
}

pub fn count_movements(crabs: Vec<u32>, iterative_sum: bool) -> Option<u32> {

    if crabs.len() == 0 {
        return None
    }

    let mut min_fuel = u32::MAX;

    let max_crab = if let Some(x) = crabs.iter().max() {
        x
    } else {
        unreachable!();
    };
    let min_crab = if let Some(x) = crabs.iter().min() {
        x
    } else {
        unreachable!();
    };

    for attack_position in *min_crab as usize..*&((max_crab + 1)) as usize {
        let fuel = crabs
            .iter()
            .map(|crab| {(*crab as i32 - attack_position as i32).abs() as u32})
            .sum();
        
        min_fuel = if fuel < min_fuel {fuel} else {min_fuel};
    }

    Some(min_fuel)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_works() {
        let rust_answer = part1();
        let python_answer: u32 = 356179;

        match rust_answer {
            Some(x) => assert_eq!(x, python_answer),
            None => panic!("No answer was returned!"),
        }
    }

    #[test]
    fn part2_works() {
        let rust_answer = part2();
        let python_answer: u32 = 99788435;

        match rust_answer {
            Some(x) => assert_eq!(x, python_answer),
            None => panic!("No answer was returned!"),
        }
    }
}
