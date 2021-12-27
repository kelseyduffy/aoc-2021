use std::fmt::Error;

pub fn part1() -> Option<u32> {
    let mut cucumbers = get_puzzle_input().unwrap();

    if cucumbers.len() == 0 {
        return None
    }

    if cucumbers[0].len() == 0 {
        return None
    }
    
    let mut something_moved_east = true;
    let mut something_moved_south = true;
    let mut steps = 0;

    while something_moved_east || something_moved_south {
        steps += 1;
        something_moved_east = move_east(&mut cucumbers);
        something_moved_south = move_south(&mut cucumbers);
    }

    Some(steps)
}

pub fn part2() -> Option<&'static str> {
    Some("We saved Christmas!")
}

pub fn get_puzzle_input() -> Result<Vec<Vec<u8>>,Error> {
    Ok(std::fs::read_to_string(String::from("input.txt")).expect("Failed to open file")
        .lines()
        .map(|line| line.bytes().collect())
        .collect())
}

pub fn move_east(cucumbers: &mut Vec<Vec<u8>>) -> bool {

    false
}

pub fn move_south(cucumbers: &mut Vec<Vec<u8>>) -> bool {
    
    false
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_works() {
        let python_result: u32 = 429;
        let rust_result = part1();

        match rust_result {
            Some(x) => assert_eq!(python_result, x),
            None => panic!("No value returned for part 1"),
        }
    }

    #[test]
    fn part2_works() {
        let python_result = String::from("We saved Christmas!");
        let rust_result = part2();
        
        match rust_result {
            Some(x) => assert_eq!(python_result, x),
            None => panic!("Christmas was not saved"),
        }
    }
}
