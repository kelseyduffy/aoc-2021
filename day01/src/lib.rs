pub fn part1 () -> i32 {

    let offset: usize = 1;

    num_increasing(get_puzzle_input(), offset)
}

pub fn part2 () -> i32 {

    let offset: usize = 3;

    num_increasing(get_puzzle_input(), offset)
}

pub fn get_puzzle_input() -> Vec<i64> {
    std::fs::read_to_string(String::from("input.txt")).expect("Failed to open file")
        .lines()
        .map(|line| line.parse().expect("Failed to parse line to i64"))
        .collect()
}

pub fn num_increasing (nums: Vec<i64>, offset: usize) -> i32 {

    let mut count = 0;

    for i in offset..nums.len() {
        if &nums[i] > &nums[i - offset] {
            count += 1;
        }
    }

    count
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1_works() {
        let rust_answer = part1();
        let python_answer = 1692;

        assert_eq!(rust_answer, python_answer)
    }

    #[test]
    fn part2_works() {
        
        let rust_answer = part2();
        let python_answer = 1724;
        
        assert_eq!(rust_answer, python_answer)            
    }
}
