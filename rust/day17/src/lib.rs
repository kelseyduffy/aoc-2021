use std::fmt::Error;

pub fn part1() -> Option<i32> {
    
    // xmin xmax ymin ymax
    let target_boundaries = get_puzzle_input().unwrap();
    
    if target_boundaries.len() == 0 {
        return None
    }
    
    Some((0..-target_boundaries[2]).fold(0, |a, b| a + b))
}

pub fn part2() -> Option<i32> {
    let target_boundaries = get_puzzle_input().unwrap();
    
    if target_boundaries.len() == 0 {
        return None
    }

    Some(0)
}

pub fn get_puzzle_input() -> Result<Vec<i32>,Error> {
    Ok(std::fs::read_to_string(String::from("input.txt")).expect("Failed to open file")
        .replace("target area: x=","")
        .replace("..",",")
        .replace(" y=","")
        .split(',')
        .map(|x| x.parse().unwrap())
        .collect())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_works() {
        let python_result = 2701;
        let rust_result = part1();

        match rust_result {
            Some(x) => assert_eq!(python_result, x),
            None => panic!("No value returned for part 1"),
        }
    }

    #[test]
    fn part2_works() {
        let python_result = 1070;
        let rust_result = part2();

        match rust_result {
            Some(x) => assert_eq!(python_result, x),
            None => panic!("No value returned for part 2"),
        }
    }
}
