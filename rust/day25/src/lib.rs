use itertools::Itertools;
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
    let mut round = 0;

    while something_moved_east || something_moved_south {
        round += 1;
        something_moved_east = move_east(&mut cucumbers);
        something_moved_south = move_south(&mut cucumbers);
    }

    Some(round)
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
    let row_count = cucumbers.len();
    let col_count = cucumbers[0].len();
    let mut newcumbers = vec![vec![b'.'; col_count]; row_count];
    let mut moved = false;

    for (r,c) in (0..row_count).cartesian_product(0..col_count) {
        match cucumbers[r][c] {
            b'>' if cucumbers[r][(c+1)%col_count] == b'.' => {
                newcumbers[r][(c+1)%col_count] = b'>';
                moved = true;
            }
            b'>' => newcumbers[r][c] = b'>',
            b'v' => newcumbers[r][c] = b'v',
            _ => {},
        }
    }

    *cucumbers = newcumbers;
    moved
}

pub fn move_south(cucumbers: &mut Vec<Vec<u8>>) -> bool {
    let row_count = cucumbers.len();
    let col_count = cucumbers[0].len();
    let mut newcumbers = vec![vec![b'.'; col_count]; row_count];
    let mut moved = false;

    for (r,c) in (0..row_count).cartesian_product(0..col_count) {
        match cucumbers[r][c] {
            b'>' => newcumbers[r][c] = b'>',
            b'v' if cucumbers[(r+1)%row_count][c] == b'.' => {
                newcumbers[(r+1)%row_count][c] = b'v';
                moved = true;
            }
            b'v' => newcumbers[r][c] = b'v',
            _ => {},
        }
    }

    *cucumbers = newcumbers;
    moved
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
